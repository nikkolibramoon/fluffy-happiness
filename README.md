# **Online Retail Data Analysis**

This project involves analyzing an **Online Retail** dataset for insights into sales trends, customer behavior, and product performance. The data was pre-processed and cleaned before generating visualizations and performing analyses using Jupyter Notebook.

## **Project Structure**

The project is divided into the following steps:

1. **Data Conversion:**
   - A script (`csv-converter.py`) was used to convert the original Excel file (`Online Retail copy.xlsx`) into a CSV format for easier manipulation and analysis. 
   - You can download the original dataset from [here](https://archive.ics.uci.edu/dataset/352/online+retail).
   
2. **Data Cleaning:**
   - The `cleaning-data.py` script was used to clean the dataset by:
     - Removing duplicates.
     - Filling missing values in relevant columns (e.g., `CustomerID` and `Description`).
     - Filtering out rows with negative `Quantity` or `UnitPrice`.
     - Standardizing the format of the `StockCode` column.
     - Converting the `InvoiceDate` column to a valid datetime format.
     - Saving the cleaned data as `cleaned-online-retail.csv`.
     
3. **Data Analysis and Visualization:**
   - The Jupyter Notebook (`analysis.ipynb`) analyzes and visualizes the cleaned data to identify key trends and insights:
     - Total and average sales.
     - Top-selling products.
     - Monthly, quarterly, and yearly sales trends.
     - Hourly sales performance.
     - Repeat customer behavior.
   - The visualizations were created using **Matplotlib** and **Seaborn** for clearer representation of sales patterns.

## **Files in the Project**

- **csv-converter.py**: A script to convert the Excel file into CSV format.
- **cleaning-data.py**: A data-cleaning script for preparing the dataset for analysis.
- **cleaned-online-retail.csv**: The cleaned dataset, generated from the cleaning script.
- **analysis.ipynb**: A Jupyter Notebook used to analyze and visualize the data.
- **requirements.txt**: A file listing the required Python packages for running the scripts and the analysis.

## **Setup Instructions**

### **1. Setting Up the Environment**
1. Clone the repository and navigate to the project folder:
   ```bash
   git clone https://github.com/nikkolibramoon/fluffy-happiness.git
   ```
2. Create a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate 
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### **2. Running the Scripts**

#### **Data Conversion:**
To convert the Excel file to a CSV:
```bash
python csv-converter.py
```
#### **Data Cleaning:**
To clean the dataset and generate a new CSV file:
```bash
python cleaning-data.py
```
#### **Data Analysis:**
To analyze and visualize the cleaned data, open the Jupyter Notebook:
```bash
jupyter notebook analysis.ipynb
```

## **Analysis Highlights**

- **Total Sales**: Displays the overall sales performance.
- **Top-Selling Products**: Identifies the best-performing products by total sales.
- **Sales Trends**: Monthly, quarterly, and yearly sales trends, helping to understand seasonality.
- **Customer Behavior**: Examines repeat customers and the average number of orders.
- **Hourly Sales**: Visualizes sales performance by the hour of the day to understand peak periods.

## **Dependencies**

- **pandas**: For data manipulation and cleaning.
- **matplotlib** and **seaborn**: For visualizations.
- **tabulate**: For printing data in tabular format in the console.
- **Jupyter**: For running interactive notebooks.
- **Python 3.7+**

All dependencies are listed in the `requirements.txt` file.

## **Future Improvements**

- Add more advanced visualizations to identify patterns in customer segmentation.
- Automate forecasting models to predict future sales based on past trends.

## License

[MIT](https://choosealicense.com/licenses/mit/)