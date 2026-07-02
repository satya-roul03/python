import pandas as pd
import mysql.connector
#import matplotlib
#matplotlib.use('TkAgg')  # Forces a standard interactive window
import matplotlib.pyplot as plt

try:
    df=pd.read_csv("store_sales.csv");
    print("Success! Data loaded perfectly.");
    print("\n---Here are the columns avilable---");
    print(df.columns.tolist());
    print("\n---Summary Staticstics of numaical value---");
    print(df.describe());
    # --- LOGIC TASK 1: Calculate Global Metrics ---
    total_revenue=df['Total'].sum();
    total_item_sold=df['Quantity'].sum();
    print("========================================");
    print("       TECHBAZAAR KEY METRICS           ");
    print("========================================");
    print(f"Total Revenue genereted: INR ₹ {total_revenue:,}");
    print(f"Total Units Solid: {total_item_sold} units");
    print("========================================\n");
    # --- LOGIC TASK 2: Category Breakdown ---
    category_summary = df.groupby('Category')['Total'].sum().reset_index();
    print("--- REVENUE BY CATEGORY ---");
    print(category_summary.to_string(index=False));
    print("---------------------------\n");
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="S111@" 
    );
    cursor = conn.cursor();
    print("🚀 Connection to MySQL Server successful!");

    # 3. Create the Database Schema
    cursor.execute("CREATE DATABASE IF NOT EXISTS store_analytics_db;");
    cursor.execute("USE store_analytics_db;");
    
    # 4. Create the Target Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS category_performance (
        id INT AUTO_INCREMENT PRIMARY KEY,
        category_name VARCHAR(100) UNIQUE,
        total_sales_inr INT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
    """);
    print("📁 Database and 'category_performance' table are verified/created.");

    # 5. Insert or Update Data Logic
    # Loop over the summary dataframe rows
    for index, row in category_summary.iterrows():
        # Using ON DUPLICATE KEY UPDATE ensures that if you re-run this script, 
        # it updates existing records instead of throwing duplicate entry errors.
        upsert_query = """
        INSERT INTO category_performance (category_name, total_sales_inr) 
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE total_sales_inr = VALUES(total_sales_inr);
        """
        cursor.execute(upsert_query, (row['Category'], int(row['Total'])));

    # 6. Commit transaction to finalize updates
    conn.commit();
    print("✅ Successfully exported metrics from Pandas DataFrame into MySQL Table!");

except mysql.connector.Error as err:
    print(f"❌ Database Error Encountered: {err}");

    # --- LOGIC TASK 3: Filter High-Value Orders ---
    # Logic: Keep rows where Total transaction is greater than 10,000 INR
    high_value_df = df[df['Total'] > 10000];
    print("--- ALERT: HIGH-VALUE TRANSACTIONS (> ₹10,000) ---");
    print(high_value_df[['Order ID', 'Customer Name', 'Product', 'Total']].to_string(index=False));
    print("--------------------------------------------------\n");
    # --- LOGIC TASK 4: Create and Save a Visual Chart ---
    plt.figure(figsize=(7, 4.5));
    # Create a bar chart for category revenue
    plt.bar(category_summary['Category'], category_summary['Total'], color=['#3498db', '#e74c3c', '#2ecc71']);
    # Add visual polish
    plt.title('Revenue Contribution by Product Category', fontsize=12, fontweight='bold')
    plt.xlabel('Category Name', fontsize=10);
    plt.ylabel('Total Sales (INR)', fontsize=10);
    plt.grid(axis='y', linestyle='--', alpha=0.5);
    # Tight layout prevents text cutoff
    plt.tight_layout();
    # Save the plot automatically
    plt.savefig('category_revenue_chart.png');
    print("Visual Chart successfully generated and saved as 'category_revenue_chart.png'!");
    plt.show();
except FileNotFoundError:
    print("Error: Could not find 'store-sales.csv'. Make sure it's in the same folder.");
finally:
    # 7. Clean up resource streams
    if 'cursor' in locals():
        cursor.close();
    if 'conn' in locals() and conn.is_connected():
        conn.close();
        print("🔌 MySQL link safely disconnected.");
