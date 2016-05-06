from flask import Flask, request, render_template
#import mysql.connector
#from mysql.connector import Error
import MySQLdb
from types import *


app = Flask(__name__)

@app.route("/") 
def hello():
        return render_template('index.html')


# @app.rout('/test', methods = ['GET']
# def test():

@app.route("/test")
def test():
        #db = mysql.connector.connect(host='localhost', database='movedb', user='root', password='157b')
        db =  MySQLdb.connect("127.0.0.1","root","","GroceryDB")
        cur = db.cursor()
        
        if request.args.get('product') != None:
                product = request.args.get('product')
                productAttr = request.args.get('productAttr')
        if request.args.get('store') != None:
                store = request.args.get('store')
                storeAttr = request.args.get('storeAttr')
        if request.args.get('time') != None:
                time = request.args.get('time')
                timeAttr = request.args.get('timeAttr')
        if request.args.get('promotion') != None:
                promotion = request.args.get('promotion')
                promotionAttr = request.args.get('promotionAttr')

                
                
        
        #cur.execute("select s.city, p.category, t.year, sum(f.dollar_sales)"+
        #        " AS total_sales from Product p, Time t, Store s,`sales_fact` f"+
        #        " where p.product_key = f.product_key"+
        #        " AND s.store_key = f.store_key"+
        #        " AND t.time_key = f.time_key"+
        #        " group by s.city, p.category, t.year order by t.year, s.city, p.category")
        
        print("select %s.%s, %s.%s, %s.%s, sum(f.dollar_sales)" %(store, storeAttr, product, productAttr, time, timeAttr) +
        " AS total_sales from %s p, %s t, %s s,`sales_fact` f" %(product, time, store) +
        " where p.product_key = f.product_key"+
        " AND s.store_key = f.store_key"+
        " AND t.time_key = f.time_key")
        
        cur.execute("select %s.%s, %s.%s, %s.%s, sum(f.dollar_sales)" %(store, storeAttr, product, productAttr, time, timeAttr) +
        " AS total_sales from %s, %s, %s,`sales_fact` f" %(product, time, store) +
        " where Product.product_key = f.product_key"+
        " AND Store.store_key = f.store_key"+
        " AND Time.time_key = f.time_key"+
        " group by %s.%s, %s.%s, %s.%s order by %s.%s, %s.%s, %s.%s" %(store, storeAttr, product, productAttr, time, timeAttr, time, timeAttr, store, storeAttr, product, productAttr))
        
        results = cur.fetchall()
        field_names = [str(i[0]) for i in cur.description]
        print(field_names)

        #a = operations()
        a ="<table class='table table-hover' id='displayTable'>" + "<thead><tr>"
        for column_heading in field_names:
                a += "<th>"+ column_heading +"</th>"
        a+= "</tr></thead>"


        for row in results:
                i=0
                a+="<tr>"
                for column_heading in field_names:
                        insert_element = row[i]
                        a+="<td>"+str(insert_element)+"</td>"
                        i+=1
                a+="</tr>"
        a+= "</table>"
                

        #return(a)
        return render_template('operations.html', variable=a)


@app.route("/operations")
def operations():
        return render_template('operations.html')



             
def connect():
        try:
                conn = mysql.connector.connect(host='localhost',
                        database='groceryDB',
                        user='root',
                        password='')
                if conn.is_connected():
                        print('Connected to MySQL database')

        except Error as e:
                print(e)

        finally:
                conn.close()



if __name__ == "__main__":
        app.run(debug=True)
        connect()
