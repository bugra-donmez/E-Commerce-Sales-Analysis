# 🛒 E-Commerce Sales Analysis Pipeline

A comprehensive Data Engineering project that analyzes large-scale retail data to optimize marketing strategies and uncover business insights.

## 📌 Project Overview
This project transforms raw sales data (12 months of split CSV files) into actionable insights using a modular Python pipeline. It simulates a real-world scenario where data needs to be extracted, cleaned, and visualized to answer critical business questions.

**Key Business Questions Answered:**
* What was the best month for sales?
* Which city sold the most product?
* What is the optimal time to display advertisements?

## 🛠️ Technologies Used
* **Python 3.x**
* **Pandas:** For Data Manipulation (ETL)
* **Matplotlib:** For Data Visualization
* **OS Module:** For File Handling

## 📂 Project Structure
```text
E-Commerce-Analysis/
│
├── SalesData/                  # Raw CSV files (Data Source)
├── main.py                     # The ETL Pipeline (Run this file)
├── SalesAnalysis.ipynb         # Prototyping and Exploratory Data Analysis (EDA)
└── README.md                   # Project Documentation
```

## 🚀 How to Run
* **Clone the repository.**
* **Install dependencies:** pip install pandas matplotlib
*  **Run the pipeline:** python main.py

## 📊 Insights & Results
* **Best Month:** December showed the highest sales activity (Holiday Season effect).
* **Top City:** San Francisco led in total revenue.
* **Peak Hours:** Customer activity peaks around **11:00 AM** and **7:00 PM (19:00)**.


### 👨‍💻 Author's Note: My Journey to Data Engineering
As a Computer Engineering student targeting a career in Data Engineering, I built this project to move beyond theoretical tutorials and practice **real-world data manipulation**.

In this project, I focused on:
* **Cleaning dirty data:** Handling missing values (`NaN`), incorrect headers, and type conversions.
* **Building a Pipeline:** Refactoring raw code into modular functions (`load`, `clean`, `analyze`) for scalability.
* **Problem Solving:** Converting business questions into SQL-like logic using Pandas.

*Data Source provided by Keith Galli.*