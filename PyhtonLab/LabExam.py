# Load the dataset using Pandas and perform the following:
# a) Display the first 8 rows
# b) Display the last 5 rows
# c) Show the dtype and number of non null values in each column
# d) Use Numpy to compute the mean AQI, max PM2.5, and min PM10 values for each city
# Group the dataset by city and calculate the following for each city:
# a) The average AQI
# b) The maximum PM2.5 value
# C) The minimum PM10 value
# Display the result in the form of Dictionary where city has these three statstical information as a list. (Dont use iterrows())



import pandas as pd
import numpy as np
path="AQI_Data.csv"
df = pd.read_csv(path)

#Display the first eight rows
print("First eight rows of the datasheet:-")
print(df.head(8))
print("\n")

#Display the last five rows
print("Last five rows of the datasheet:-")
print(df.tail(5))
print("\n")

# #Display the statistics for all numeric columns
# print("Summary statistics for all numeric columns are:-")
# print(df.describe())
# print("\n")

# Show the dtype and number of non-null values in each column
print("\nData types and non-null values:")
print(df.info())


#Display the mean of AQI, PM2.5 and PM10
# Compute mean AQI, max PM2.5, and min PM10 values for each city
mean_aqi = df.groupby('City')['AQI'].mean().to_numpy()
max_pm25 = df.groupby('City')['PM2.5'].max().to_numpy()
min_pm10 = df.groupby('City')['PM10'].min().to_numpy()

print("\nMean AQI for each city:", mean_aqi)
print("Max PM2.5 for each city:", max_pm25)
print("Min PM10 for each city:", min_pm10)
# AQI_mean = np.mean(df['AQI'])
# PM_max = np.max(df['PM2.5'])
# PM10_min = np.min(df['PM10'])
# print(f"Mean of AQI is {AQI_mean}.")
# print("")
# print(f"Max of PM2.5 is {PM_max}.")
# print("")
# print(f"Max of PM10 is {PM10_min}.")
# print("\n")

# Group the dataset by city and calculate the required statistics
grouped = df.groupby('City').agg({
    'AQI': 'mean',
    'PM2.5': 'max',
    'PM10': 'min'
})

print(grouped)

# Convert the result to a dictionary
result_dict = grouped.apply(lambda row: [row['AQI'].tolist() , row['PM2.5'].tolist() , row['PM10'].tolist()], axis=1).to_dict()

print("\nResult dictionary:")
print(result_dict)




