import pandas as pd
import mysql.connector

password = input("Enter MySQL root password: ")

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password=password,
    database="banking_analytics",
    connection_timeout=60
)

cursor = connection.cursor()

df = pd.read_csv("data/loan_data.csv")
df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(
    df["Loan_Amount_Term"].median()
)

print("CSV loaded successfully!")
print("Total records:", len(df))

query = """
INSERT INTO loan_prediction
(
    Loan_ID,
    Gender,
    Married,
    Dependents,
    Education,
    Self_Employed,
    ApplicantIncome,
    CoapplicantIncome,
    LoanAmount,
    Loan_Amount_Term,
    Credit_History,
    Property_Area,
    Loan_Status
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

data = [
    (
        row.Loan_ID,
        row.Gender,
        row.Married,
        row.Dependents,
        row.Education,
        row.Self_Employed,
        float(row.ApplicantIncome),
        float(row.CoapplicantIncome),
        float(row.LoanAmount),
        int(row.Loan_Amount_Term),
        float(row.Credit_History),
        row.Property_Area,
        row.Loan_Status
    )
    for row in df.itertuples(index=False)
]

cursor.executemany(query, data)
connection.commit()

print("\nLoan data imported successfully!")
print("Total records imported:", len(data))

cursor.close()
connection.close()