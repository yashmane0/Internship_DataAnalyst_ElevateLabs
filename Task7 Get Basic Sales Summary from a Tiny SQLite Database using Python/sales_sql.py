import sqlite3
import csv
import pandas as pd
import matplotlib.pyplot as plt


conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales_data_sample (
        ordernumber INTEGER,
        quantityordered INTEGER,
        priceeach REAL,
        orderlinenumber INTEGER,
        sales REAL,
        orderdate TEXT,
        status TEXT,
        qtr_id INTEGER,
        month_id INTEGER,
        year_id INTEGER,
        productline TEXT,
        msrp REAL,
        productcode TEXT,
        customername TEXT,
        phone TEXT,
        addressline1 TEXT,
        addressline2 TEXT,
        city TEXT,
        state TEXT,
        postalcode TEXT,
        country TEXT,
        territory TEXT,
        contactlastname TEXT,
        contactfirstname TEXT,
        dealsize TEXT
        
    )
''')

with open('D:/InternshipElevateLabs/Task7 Get Basic Sales Summary from a Tiny SQLite Database using Python/sales_data_sample.csv', 'r') as file:
    dr = csv.DictReader(file)
    rows = [(int(row['ordernumber']), int(row['quantityordered']), 
             float(row['priceeach']), int(row['orderlinenumber']), 
             float(row['sales']), row['orderdate'], row['status'], 
             int(row['qtr_id']),int(row['month_id']), int(row['year_id']),
             row['productline'],float(row['msrp']),row['productcode'],
             row['customername'],row['phone'],row['addressline1'],row['addressline2'],
             row['city'],row['state'],row['postalcode'],row['country'],row['territory'],
             row['contactlastname'],row['contactfirstname'],row['dealsize']) for row in dr]

cursor.executemany("INSERT INTO sales_data_sample (ordernumber, quantityordered, priceeach, orderlinenumber,sales,orderdate,status,qtr_id,month_id,year_id,productline,msrp,productcode,customername,phone,addressline1,addressline2,city,state,postalcode,country,territory,contactlastname,contactfirstname,dealsize)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
conn.commit()


cursor.execute("SELECT SUM(quantityordered) AS total_qty, SUM(quantityordered * sales) AS total_revenue FROM sales_data_sample")
result = cursor.fetchone()

print("Total Quantity Sold:", result[0])
print("Total Revenue: $", result[1])
query = "SELECT productcode, SUM(quantityordered) AS total_qty, SUM(quantityordered * sales) AS revenue FROM sales_data_sample GROUP BY productline"

df = pd.read_sql_query(query, conn)
print(df)
df.plot(kind='bar', x='productcode', y='revenue')
plt.title('Revenue by Product')
plt.xlabel('ProductCode')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# plt.savefig("sales_chart.png")

conn.close()
