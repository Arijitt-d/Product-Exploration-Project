# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:03:34 2025

@author: Arijit
"""

import pandas as pd

#reading the csv files
Orders_df =pd.read_csv("C:\\Users\\Arijit\\OneDrive\\Documents\\NOTES\\Python\\22.06.2024\\JAR Assignment\\Order_Details_19795F61CF.csv")
print(Orders_df["Order ID"])
Orders_details_df =pd.read_csv("C:\\Users\\Arijit\\OneDrive\\Documents\\NOTES\\Python\\22.06.2024\\JAR Assignment\\List_of_Orders_55FFC79CF8.csv")

#check for null values
print(Orders_details_df["Order ID"])
print(Orders_df.isnull().any(axis=1))
print(Orders_details_df.isnull().any(axis=1))

#import seaborn and matplotlib for the purpose visualization and plotting
import seaborn as sb
import matplotlib.pyplot as plt

#plotting heat map for null values if its there
sb.heatmap(Orders_details_df.isnull(), cmap="viridis", cbar=False, yticklabels=False)
plt.show()

sb.heatmap(Orders_df.isnull(), cmap="viridis", cbar=False, yticklabels=False)
plt.show()

#dropping rows having null values
Orders_details_df=Orders_details_df.dropna()
Orders_df=Orders_df.dropna()

#merging orders table and order details tables in orders_data_df dataframe
Orders_data_df = pd.merge(Orders_df, Orders_details_df, on="Order ID", how="left")
print(Orders_data_df)
Orders_data_df.to_csv("C:\\Users\\Arijit\\OneDrive\\Documents\\NOTES\\Python\\22.06.2024\\JAR Assignment\\Orders_data.csv", index=False)

#calculating the total sales per category
total_sales_by_category_df = Orders_data_df.groupby("Category")["Amount"].sum().reset_index()
print(total_sales_by_category_df)

#exporting the total sales by category data to a csv file
total_sales_by_category_df.to_csv("C:\\Users\\Arijit\\OneDrive\\Documents\\NOTES\\Python\\22.06.2024\\JAR Assignment\\total_sales_by_category.csv", index=False)


# Plot bar chart for total sales by category data
plt.figure(figsize=(10, 5))
sb.barplot(x="Category", y="Amount", data=total_sales_by_category_df, palette="deep")

#calculating avg profit in each category
avg_profit_per_order_df = Orders_data_df.groupby("Category")["Profit"].mean().reset_index()
avg_profit_per_order_df.rename(columns={"Profit": "Avg_Profit_Per_Order"}, inplace=True)
print(avg_profit_per_order_df)

#calculating net profit in each category
profit_df= Orders_data_df.groupby("Category")["Profit"].sum().reset_index()

#merging the profit_df dataframe with total sales by category data
total_category_data_df =pd.merge(total_sales_by_category_df,profit_df, how="inner")
print(total_category_data_df)

#merging avg profit per order data in total category data dataframe
Final_category_data_df = pd.merge(total_category_data_df, avg_profit_per_order_df, on="Category", how="inner")
print(Final_category_data_df)

#merging all the parameters into a single dataframe: Final_category_data_df
Final_category_data_df['Profit_percentage'] = (Final_category_data_df['Profit'] / Final_category_data_df['Amount']) * 100
#total_category_data_df.rename(columns={"Profit": "Avg_Profit_Per_Order"}, inplace=True)
print(Final_category_data_df)


#finding the top performing category with the maximum sales
max_sales= Final_category_data_df.query("Amount == Amount.max()")['Category'].values[0]
print("Category with maximum sales:",max_sales)

#finding the top performing category with the maximum avg profit per order
max_avg_profit= Final_category_data_df.query("Avg_Profit_Per_Order == Avg_Profit_Per_Order.max()")['Category'].values[0]
print("Category with maximum avg profit per order:",max_sales)






















