USE banking_analytics;

-- 1. Segment-wise customer count
SELECT
    Segment,
    COUNT(*) AS Total_Customers
FROM customer_segments
GROUP BY Segment
ORDER BY Total_Customers DESC;


-- 2. Segment-wise financial analysis
SELECT
    Segment,
    COUNT(*) AS Total_Customers,
    ROUND(AVG(Account_Balance), 2) AS Avg_Account_Balance,
    ROUND(AVG(Total_Transaction_Amount), 2) AS Avg_Total_Transaction_Amount,
    ROUND(AVG(Average_Transaction_Amount), 2) AS Avg_Transaction_Amount
FROM customer_segments
GROUP BY Segment
ORDER BY Avg_Total_Transaction_Amount DESC;


-- 3. Top 10 high-value customers
SELECT
    CustomerID,
    Segment,
    Total_Transactions,
    Total_Transaction_Amount,
    Average_Transaction_Amount,
    Account_Balance
FROM customer_segments
ORDER BY Total_Transaction_Amount DESC
LIMIT 10;


-- 4. Top 10 customers by account balance
SELECT
    CustomerID,
    Segment,
    Account_Balance,
    Total_Transactions,
    Total_Transaction_Amount
FROM customer_segments
ORDER BY Account_Balance DESC
LIMIT 10;


-- 5. Cluster-wise customer analysis
SELECT
    Cluster,
    Segment,
    COUNT(*) AS Total_Customers,
    ROUND(AVG(Account_Balance), 2) AS Avg_Account_Balance,
    ROUND(AVG(Total_Transaction_Amount), 2) AS Avg_Transaction_Amount
FROM customer_segments
GROUP BY Cluster, Segment
ORDER BY Cluster;


-- 6. Overall banking customer statistics
SELECT
    COUNT(*) AS Total_Customers,
    ROUND(AVG(Account_Balance), 2) AS Overall_Avg_Balance,
    ROUND(AVG(Total_Transaction_Amount), 2) AS Overall_Avg_Transaction,
    ROUND(SUM(Total_Transaction_Amount), 2) AS Total_Transaction_Value
FROM customer_segments;
USE banking_analytics;
CREATE TABLE loan_prediction (
    Loan_ID VARCHAR(20) PRIMARY KEY,
    Gender VARCHAR(20),
    Married VARCHAR(20),
    Dependents VARCHAR(20),
    Education VARCHAR(30),
    Self_Employed VARCHAR(30),
    ApplicantIncome DECIMAL(12,2),
    CoapplicantIncome DECIMAL(12,2),
    LoanAmount DECIMAL(12,2),
    Loan_Amount_Term INT,
    Credit_History DECIMAL(5,2),
    Property_Area VARCHAR(30),
    Loan_Status VARCHAR(10)
);
USE banking_analytics;

SHOW TABLES;
TRUNCATE TABLE customer_segments;
USE banking_analytics;

SELECT COUNT(*) FROM customer_segments;
SELECT * 
FROM customer_segments
LIMIT 10;
SELECT Cluster, Segment, COUNT(*) AS Customers
FROM customer_segments
GROUP BY Cluster, Segment;
USE banking_analytics;

CREATE TABLE credit_risk (
    person_age INT,
    person_income DECIMAL(12,2),
    person_home_ownership VARCHAR(20),
    person_emp_length DECIMAL(5,2),
    loan_intent VARCHAR(30),
    loan_grade VARCHAR(5),
    loan_amnt DECIMAL(12,2),
    loan_int_rate DECIMAL(6,2),
    loan_status INT,
    loan_percent_income DECIMAL(6,4),
    cb_person_default_on_file VARCHAR(5),
    cb_person_cred_hist_length INT
);
show tables;
USE banking_analytics;

CREATE TABLE fraud_detection (
    Time DECIMAL(15,3),
    V1 DECIMAL(20,10),
    V2 DECIMAL(20,10),
    V3 DECIMAL(20,10),
    V4 DECIMAL(20,10),
    V5 DECIMAL(20,10),
    V6 DECIMAL(20,10),
    V7 DECIMAL(20,10),
    V8 DECIMAL(20,10),
    V9 DECIMAL(20,10),
    V10 DECIMAL(20,10),
    V11 DECIMAL(20,10),
    V12 DECIMAL(20,10),
    V13 DECIMAL(20,10),
    V14 DECIMAL(20,10),
    V15 DECIMAL(20,10),
    V16 DECIMAL(20,10),
    V17 DECIMAL(20,10),
    V18 DECIMAL(20,10),
    V19 DECIMAL(20,10),
    V20 DECIMAL(20,10),
    V21 DECIMAL(20,10),
    V22 DECIMAL(20,10),
    V23 DECIMAL(20,10),
    V24 DECIMAL(20,10),
    V25 DECIMAL(20,10),
    V26 DECIMAL(20,10),
    V27 DECIMAL(20,10),
    V28 DECIMAL(20,10),
    Amount DECIMAL(15,2),
    Class INT
);
show tables;