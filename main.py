import pandas as pd
import matplotlib.pyplot as plt

def analyze_sales_data(file_path):

    try:
        # Load the data from the Excel file
        df = pd.read_excel(file_path)
        print("Data loaded successfully:")
        print(df.head()) # Show the first 5 rows of the data

        # Calculate a new column for Total Revenue
        df['Total Revenue'] = df['Quantity Sold'] * df['Price per Unit']

        # Perform basic data analysis
        total_revenue = df['Total Revenue'].sum()
        avg_price = df['Price per Unit'].mean()
        most_sold_product = df.loc[df['Quantity Sold'].idxmax()]
        
        print("\n--- Sales Report ---")
        print(f"Total Revenue: {total_revenue} BDT")
        print(f"Average Price per Unit: {avg_price:.2f} BDT")
        print(f"Most Sold Product: {most_sold_product['Product']} ({most_sold_product['Quantity Sold']} units)")
        
        # Data Visualization
        plt.figure(figsize=(10, 6))
        plt.bar(df['Product'], df['Total Revenue'], color='skyblue')
        plt.title('Total Revenue per Product')
        plt.xlabel('Product')
        plt.ylabel('Total Revenue (BDT)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
if __name__ == "__main__":
    file_name = "day-11.xlsx"
    analyze_sales_data(file_name)