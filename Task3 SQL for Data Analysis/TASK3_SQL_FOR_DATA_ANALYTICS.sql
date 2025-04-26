SELECT SUM(quantity),AVG(unitprice) FROM Ecommerce  WHERE quantity >10 GROUP BY stockcode ORDER BY  AVG(unitprice)
COPY salereport (indexx,Skucode,designno,stock,category,sizee,color) 
FROM 'D:/InternshipElevateLabs/Task3 SQL for Data Analysis/salereport.csv'
WITH (format csv,header)
SELECT * FROM salereport
CREATE TABLE may2022 (
indexx int PRIMARY KEY,
Sku varchar,
StyleId varchar,
Catalogg varchar,
Category varchar,
Weight DECIMAL(10, 2),
TP DECIMAL(10, 2),
MRPOld int,
FinalMRPOld int,
AjioMRP int,
AmazonMRP int,
AmazonFBAMRP int,
FlipkartMRP int,
LimeroadMRP int,
MyntraMRP int,
PaytmMRP int,
SnapdealMRP int
)

COPY may2022 (indexx,Sku,Styleid,catalogg,category,weight,tp,mrpold,
finalmrpold,ajiomrp,amazonmrp,amazonfbamrp,flipkartmrp,limeroadmrp,myntramrp,
paytmmrp,snapdealmrp) 
FROM 'D:/InternshipElevateLabs/Task3 SQL for Data Analysis/may2022.csv'
WITH (format csv,header)

SELECT s.designno,s.stock,s.color,m.category,m.amazonmrp,m.flipkartmrp,m.myntramrp 
FROM salereport as s INNER JOIN may2022 as m ON s.indexx=m.indexxSELECT * FROM may2022
SELECT s.designno,s.stock,s.color,m.category,m.amazonmrp,m.flipkartmrp,m.myntramrp 
FROM salereport as s LEFT JOIN may2022 as m ON s.indexx=m.indexx
SELECT s.designno,s.stock,s.color,m.category,m.amazonmrp,m.flipkartmrp,m.myntramrp 
FROM salereport as s RIGHT JOIN may2022 as m ON s.indexx=m.indexx
SELECT category,SUM(weight) AS Sum_weight,AVG(amazonmrp) AS avg_amazon_mrp ,
AVG(flipkartmrp) AS avg_flipkart_mrp ,AVG(myntramrp) AS avg_myntra_mrp 
FROM may2022 GROUP BY category
CREATE VIEW category_group_by AS
SELECT category,SUM(weight) AS Sum_weight,AVG(amazonmrp) AS avg_amazon_mrp ,
AVG(flipkartmrp) AS avg_flipkart_mrp ,AVG(myntramrp) AS avg_myntra_mrp 
FROM may2022 GROUP BY category
SELECT* FROM salereport
CREATE INDEX idx_stock ON salereport(stock)
SELECT * FROM salereport WHERE stock>10