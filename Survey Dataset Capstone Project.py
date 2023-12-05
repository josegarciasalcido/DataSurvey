import pandas as pd

dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"

# Converting file into data frame
df = pd.read_csv(dataset_url)

print(df.head()) # Display the first few rows of the DataFrame
print(df.shape) # Display # rows and columns
print(df.dtypes) # Display the types of each column
print(df['Age'].mean()) # Average age
print(df['Country'].nunique()) # Unique countries