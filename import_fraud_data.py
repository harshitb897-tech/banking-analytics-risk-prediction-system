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

df = pd.read_csv("data/credit_card_fraud.csv")

print("CSV loaded successfully!")
print("Total records:", len(df))

query = """
INSERT INTO fraud_detection
(
    Time, V1, V2, V3, V4, V5, V6, V7, V8, V9,
    V10, V11, V12, V13, V14, V15, V16, V17, V18, V19,
    V20, V21, V22, V23, V24, V25, V26, V27, V28,
    Amount, Class
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""

data = [
    tuple(row)
    for row in df.itertuples(index=False, name=None)
]

batch_size = 5000

for i in range(0, len(data), batch_size):
    cursor.executemany(query, data[i:i + batch_size])
    connection.commit()
    print(f"Imported: {min(i + batch_size, len(data))}/{len(data)}")

cursor.close()
connection.close()

print("\nFraud data imported successfully!")
print("Total records imported:", len(data))