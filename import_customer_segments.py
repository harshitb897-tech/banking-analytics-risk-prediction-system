import pandas as pd
import mysql.connector

# MySQL connection
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

# Read CSV
df = pd.read_csv("data/customer_segments.csv")

print("CSV loaded successfully!")
print("Total records:", len(df))

query = """
INSERT INTO customer_segments
(
    CustomerID,
    Total_Transactions,
    Total_Transaction_Amount,
    Average_Transaction_Amount,
    Account_Balance,
    Cluster,
    Segment
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

data = [
    (
        row.CustomerID,
        int(row.Total_Transactions),
        float(row.Total_Transaction_Amount),
        float(row.Average_Transaction_Amount),
        float(row.Account_Balance),
        int(row.Cluster),
        row.Segment
    )
    for row in df.itertuples(index=False)
]

batch_size = 1000

for i in range(0, len(data), batch_size):
    cursor.executemany(query, data[i:i + batch_size])
    connection.commit()
    print(f"Imported: {min(i + batch_size, len(data))}/{len(data)}")

cursor.close()
connection.close()

print("\nCustomer data imported successfully!")