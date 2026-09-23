import pandas as pd
import mysql.connector

password = input("Enter MySQL root password: ")

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password=password,
    database="banking_analytics"
)

cursor = connection.cursor()

df = pd.read_csv("data/credit_risk.csv")

# Handle missing values
df["person_emp_length"] = df["person_emp_length"].fillna(
    df["person_emp_length"].median()
)

df["loan_int_rate"] = df["loan_int_rate"].fillna(
    df["loan_int_rate"].median()
)

print("CSV loaded successfully!")
print("Total records:", len(df))

query = """
INSERT INTO credit_risk
(
    person_age,
    person_income,
    person_home_ownership,
    person_emp_length,
    loan_intent,
    loan_grade,
    loan_amnt,
    loan_int_rate,
    loan_status,
    loan_percent_income,
    cb_person_default_on_file,
    cb_person_cred_hist_length
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

data = [
    (
        int(row.person_age),
        float(row.person_income),
        row.person_home_ownership,
        float(row.person_emp_length),
        row.loan_intent,
        row.loan_grade,
        float(row.loan_amnt),
        float(row.loan_int_rate),
        int(row.loan_status),
        float(row.loan_percent_income),
        row.cb_person_default_on_file,
        int(row.cb_person_cred_hist_length)
    )
    for row in df.itertuples(index=False)
]

batch_size = 5000

for i in range(0, len(data), batch_size):
    cursor.executemany(query, data[i:i + batch_size])
    connection.commit()
    print(f"Imported: {min(i + batch_size, len(data))}/{len(data)}")

cursor.close()
connection.close()

print("\nCredit risk data imported successfully!")
print("Total records imported:", len(data))