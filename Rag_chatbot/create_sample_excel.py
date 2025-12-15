#!/usr/bin/env python3
"""
Create sample Excel and CSV files for testing RAG system
"""

import pandas as pd
import os

# Create documents directory if it doesn't exist
os.makedirs("documents", exist_ok=True)

# Sample data 1: Health Information
health_data = {
    'Condition': ['Diabetes', 'Hypertension', 'Heart Disease', 'Obesity', 'Asthma'],
    'Symptoms': [
        'Increased thirst, frequent urination, extreme fatigue',
        'High blood pressure, headaches, chest pain',
        'Chest pain, shortness of breath, fatigue',
        'Excess weight, joint pain, difficulty breathing',
        'Wheezing, coughing, chest tightness'
    ],
    'Treatment': [
        'Insulin therapy, diet control, exercise',
        'Blood pressure medications, lifestyle changes',
        'Heart medications, surgery if needed, lifestyle changes',
        'Diet modification, exercise, behavioral therapy',
        'Inhalers, avoid triggers, medications'
    ],
    'Prevention': [
        'Healthy diet, regular exercise, weight management',
        'Low sodium diet, regular exercise, stress management',
        'Healthy diet, exercise, no smoking',
        'Balanced diet, physical activity, portion control',
        'Avoid allergens, maintain good air quality'
    ]
}

# Sample data 2: Product Information
product_data = {
    'Product_Name': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smart Watch'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Wearables'],
    'Price': [999, 699, 399, 199, 299],
    'Rating': [4.5, 4.2, 4.0, 4.7, 4.3],
    'Stock': [25, 50, 30, 100, 45],
    'Description': [
        'High performance laptop with 16GB RAM and SSD',
        'Latest smartphone with advanced camera features',
        'Lightweight tablet perfect for reading and browsing',
        'Noise-cancelling headphones with premium sound',
        'Fitness tracking smartwatch with health monitoring'
    ]
}

# Sample data 3: Employee Information
employee_data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['John Smith', 'Sarah Johnson', 'Mike Davis', 'Emily Brown', 'David Wilson'],
    'Department': ['IT', 'HR', 'Finance', 'Marketing', 'IT'],
    'Position': ['Developer', 'Manager', 'Analyst', 'Specialist', 'Architect'],
    'Salary': [75000, 85000, 65000, 60000, 95000],
    'Experience_Years': [3, 7, 4, 2, 10],
    'Location': ['New York', 'California', 'Texas', 'Florida', 'New York']
}

# Create Excel file with multiple sheets
with pd.ExcelWriter('documents/sample_data.xlsx', engine='openpyxl') as writer:
    pd.DataFrame(health_data).to_excel(writer, sheet_name='Health_Info', index=False)
    pd.DataFrame(product_data).to_excel(writer, sheet_name='Products', index=False)
    pd.DataFrame(employee_data).to_excel(writer, sheet_name='Employees', index=False)

# Create separate CSV files
pd.DataFrame(health_data).to_csv('documents/health_conditions.csv', index=False)
pd.DataFrame(product_data).to_csv('documents/product_catalog.csv', index=False)

print("✅ Sample files created successfully!")
print("\nCreated files:")
print("📊 documents/sample_data.xlsx (3 sheets: Health_Info, Products, Employees)")
print("📄 documents/health_conditions.csv")
print("📄 documents/product_catalog.csv")
print("\n🎯 You can now ask questions like:")
print("- What are diabetes symptoms?")
print("- What products are available?") 
print("- Who works in IT department?")
print("- What is the price of laptop?")
print("- What are treatment options for hypertension?")