CREATE TABLE details (
Foreign key (orderID) References orders(orderid),
Amount int,
Profit int,
Quantity int,
Category varchar,
Subcategory varchar,
Paymentmode	varchar
)
SELECT * FROM details
CREATE TABLE orders(
orderid varchar PRIMARY KEY,
orderdate Date,
customername varchar,
states varchar,
city varchar
)
SELECT * FROM orders

COPY orders(orderid,orderdate,customername,states,city)
FROM 'D:/InternshipElevateLabs/Task6 Sales Trend Analysis Using Aggregations/Orders.csv'
WITH (format CSV, HEADER)
COPY details(orderID,Amount,Profit,Quantity,Category,Subcategory,Paymentmode)
FROM 'D:/InternshipElevateLabs/Task6 Sales Trend Analysis Using Aggregations/Details.csv'
WITH(format CSV,header)

SELECT EXTRACT(MONTH FROM orderdate) AS order_month
FROM orders	
SELECT COUNT(DISTINCT orderid) AS order_count_unique,EXTRACT(MONTH FROM orderdate) AS order_month	 
FROM orders GROUP BY EXTRACT(MONTH FROM orderdate)
SELECT SUM(amount),category FROM details GROUP BY category
SELECT EXTRACT(MONTH FROM orderdate) AS order_month, COUNT(DISTINCT orderid) AS order_count_unique 
FROM orders GROUP BY EXTRACT(MONTH FROM orderdate) ORDER BY order_month
SELECT AVG(d.profit) AS avg_profit,AVG(d.quantity) AS avg_quantity,
COUNT(DISTINCT d.orderid) AS order_count_unique,d.subcategory,EXTRACT(MONTH FROM o.orderdate) AS order_month 
FROM details as d INNER JOIN orders AS o ON d.orderid=o.orderid GROUP BY d.subcategory,
EXTRACT(MONTH FROM o.orderdate),d.profit,d.amount ORDER BY d.profit,d.amount
SELECT * FROM details LIMIT 10
