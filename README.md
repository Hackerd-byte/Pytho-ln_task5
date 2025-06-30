# Pytho-ln_task5
## 📊 Sales Analysis with Pandas and Matplotlib

This Python script analyzes sales data from a CSV file using Pandas and visualizes the total sales using Matplotlib.

## 📁 File Structure

Sales_analysis.py: Main script for analyzing and plotting the sales data.

CSV File Path: The script expects a file named 100 Sales Records.csv located at
/storage/emulated/0/Download/100 Sales Records.csv


## 🧾 Requirements

Make sure you have the following Python packages installed:
```
pip install pandas matplotlib
```
## 🔍 What It Does

Loads sales data from a CSV file.

Groups the data by Units Sold and calculates the total Unit Price for each group.

Visualizes the result as a bar chart.


## 📈 Output

The output is a bar chart that shows Total Unit Price grouped by Units Sold.

## 🚀 How to Run
```
python Sales_analysis.py
```
Make sure the CSV file is at the correct path before running.

## 📌 Note

If you're using this in Termux or a mobile environment:

Ensure you have GUI display support (like X11 forwarding or a VNC setup), or save the plot to an image file instead of showing it directly.


You can modify the end of the script like this if needed:
```
plt.savefig('sales_chart.png')
```
