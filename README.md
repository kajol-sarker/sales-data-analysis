# Python Advanced Projects: Excel/CSV File Analyzer

### Project Overview

This project is the first in the "Python Advanced Projects" series, focusing on data analysis. It's a command-line tool that analyzes sales data from an Excel or CSV file. The application uses the powerful **Pandas** and **Matplotlib** libraries to read data, perform basic statistical analysis, and visualize the results in a graphical format. This project provides a foundational understanding of data science concepts and is a crucial step towards building real-world data-driven applications.

### Features

-   **Data Loading:** Automatically loads data from a `.csv` or `.xlsx` file into a Pandas DataFrame.
-   **Data Cleaning:** Checks for missing values in the dataset.
-   **Statistical Analysis:** Calculates key metrics such as total revenue, average sales, and identifies the most sold product.
-   **Data Visualization:** Generates a bar chart using Matplotlib to visually represent the total revenue per product.
-   **Error Handling:** Includes robust error handling to manage scenarios where the specified file is not found.

### Prerequisites

Before running the script, you need to install the required libraries. Use `pip` to install them:

```bash
pip install pandas matplotlib openpyxl
```

Example Output
Upon successful execution, the program will print a sales report to the console and display a bar chart in a new window.

Console Output:

Data loaded successfully:
    Product  Quantity Sold  Price per Unit
0    Laptop            150           50000
1     Mouse            250             500
2  Keyboard            180            1200
3   Monitor            120           15000
4 Headphone            200            2500

--- Missing Values ---
Product           0
Quantity Sold     0
Price per Unit    0
dtype: int64

--- Sales Report ---
Total Revenue: 9,066,000 Taka
Average Quantity Sold: 180.00 units
Most Sold Product: Mouse


Graphical Output:

Author
[kajol-sarker] - [https://github.com/kajol-sarker]

