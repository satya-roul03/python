import mysql.connector

try:
    # Establish the connection
    mydb = mysql.connector.connect(
        host="localhost",           # Or the IP/hostname of your MySQL server
        user="root",       # Replace with your MySQL username
        password="Satya123@",   # Replace with your MySQL password
        database="satya"    # Optional: specify a database to connect to
    )

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # Create a database if it doesn't exist (optional, if you didn't specify in connect)
    # mycursor.execute("CREATE DATABASE IF NOT EXISTS test_database")
    # mydb.database = "test_database" # Set the database after creation

    # Create a table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            address VARCHAR(255)
        )
    """)

    # Insert data
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John Doe", "Highway 21")
    mycursor.execute(sql, val)
    mydb.commit() # Commit changes to the database

    print(f"{mycursor.rowcount} record inserted.")

    # Insert multiple records
    sql_multiple = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val_multiple = [
        ("Peter", "Lowstreet 4"),
        ("Amy", "Apple St 652"),
        ("Hannah", "Mountain 21")
    ]
    mycursor.executemany(sql_multiple, val_multiple)
    mydb.commit()

    print(f"{mycursor.rowcount} records inserted.")

    # Select data
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()

    print("\nCustomer data:")
    for x in myresult:
        print(x)

    # Update data
    update_sql = "UPDATE customers SET address = %s WHERE name = %s"
    update_val = ("Valley 345", "John Doe")
    mycursor.execute(update_sql, update_val)
    mydb.commit()
    print(f"\n{mycursor.rowcount} record updated.")

    # Delete data
    delete_sql = "DELETE FROM customers WHERE name = %s"
    delete_val = ("Amy",)
    mycursor.execute(delete_sql, delete_val)
    mydb.commit()
    print(f"\n{mycursor.rowcount} record deleted.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'mycursor' in locals() and mycursor:
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("MySQL connection closed.")