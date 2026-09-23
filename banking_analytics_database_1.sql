create database banking_analytics;
show databases;
USE banking_analytics;
CREATE TABLE customer_segments (
    CustomerID VARCHAR(20) PRIMARY KEY,
    Total_Transactions INT,
    Total_Transaction_Amount DECIMAL(15,2),
    Average_Transaction_Amount DECIMAL(15,2),
    Account_Balance DECIMAL(15,2),
    Cluster INT,
    Segment VARCHAR(50)
);
SHOW TABLES;
SELECT COUNT(*) AS total_customers
FROM customer_segments;
SELECT 
    Segment,
    COUNT(*) AS Total_Customers
FROM customer_segments
GROUP BY Segment
ORDER BY Total_Customers DESC;
SELECT
    Segment,
    COUNT(*) AS Total_Customers,
    ROUND(AVG(Account_Balance), 2) AS Avg_Account_Balance,
    ROUND(AVG(Total_Transaction_Amount), 2) AS Avg_Total_Transaction_Amount,
    ROUND(AVG(Average_Transaction_Amount), 2) AS Avg_Transaction_Amount
FROM customer_segments
GROUP BY Segment
ORDER BY Avg_Total_Transaction_Amount DESC;
