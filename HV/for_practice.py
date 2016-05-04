from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error
from types import *





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
        




def main():
        test()
        





if  __name__ =='__main__':main()
