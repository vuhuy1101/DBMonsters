from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error
from types import *




app = Flask(__name__)

@app.route("/") 
def hello():
        return render_template('index.html')


# @app.rout('/test', methods = ['GET']
# def test():

@app.route("/test")
def test():
        db = mysql.connector.connect(host='localhost', database='movedb', user='root', password='157b')
        cur = db.cursor()
        cur.execute("select s.city, p.category, t.year, sum(f.dollar_sales)"+
                " AS total_sales from Product p, Time t, Store s,`sales fact` f"+
                " where p.product_key = f.product_key"+
                " AND s.store_key = f.store_key"+
                " AND t.time_key = f.time_key"+
                " group by s.city, p.category, t.year order by t.year, s.city, p.category")
        
        results = cur.fetchall()
        field_names = [str(i[0]) for i in cur.description]
        print(field_names)
        

        a="<table border='1'>" + "<tr>"
        for column_heading in field_names:
                a += "<th>"+ column_heading +"</th>"
        a+= "</tr>"


        for row in results:
                i=0
                a+="<tr>"
                for column_heading in field_names:
                        insert_element = row[i]
                        a+="<td>"+str(insert_element)+"</td>"
                        i+=1
                a+="</tr>"
                

        
        
        return(a)





                

def connect():
        try:
                conn = mysql.connector.connect(host='localhost',
                        database='movedb',
                        user='root',
                        password='157b')
                if conn.is_connected():
                        print('Connected to MySQL database')

        except Error as e:
                print(e)

        finally:
                conn.close()



if __name__ == "__main__":
        app.run(debug=True)
        connect()
