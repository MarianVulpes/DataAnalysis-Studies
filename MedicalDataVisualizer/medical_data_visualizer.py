import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Activities\MedicalDataVisualizer\medical_examination.csv', header=0)

print("Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.")
def is_overweight(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return (bmi > 25).astype(int)

df['overweight'] = df.apply(lambda row: is_overweight(row['weight'], row['height']), axis=1)
# 0 = NOT Overweight // 1 = Ovewrweight
view = df['overweight']
print(view)

print("Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.")
df['cholesterol'] = df['cholesterol'].replace({1: 0, 2: 1, 3: 1})
df['gluc'] = df['gluc'].replace({1: 0, 2: 1, 3: 1})
chgl = df[['cholesterol', 'gluc']]
print(chgl)

print("Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). The dataset should be split by 'Cardio' so there is one chart for each cardio value.")
melted_df = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
sns.catplot(x='variable', hue='value', col='cardio', kind='count', data=melted_df)
plt.show()

print("Clean the data.")
print("Data before:")
print(f"{df.ap_lo.max()} is the max diastolic blood pressure BEFORE.")
print(f"{df.weight.max()} is the max weight BEFORE.")
print(f"{df.weight.min()} is the min weight BEFORE.")
print(f"{df.height.max()} is the max height BEFORE.")
print(f"{df.height.min()} is the min height BEFORE.")
# Filter out diastolic pressure higher than systolic
df = df[df['ap_lo'] <= df['ap_hi']]

# Filter out height less than the 2.5th percentile and more than the 97.5th percentile
height_lower_bound = df['height'].quantile(0.025)
height_upper_bound = df['height'].quantile(0.975)
df = df[(df['height'] >= height_lower_bound) & (df['height'] <= height_upper_bound)]

# Filter out weight less than the 2.5th percentile and more than the 97.5th percentile
weight_lower_bound = df['weight'].quantile(0.025)
weight_upper_bound = df['weight'].quantile(0.975)
df = df[(df['weight'] >= weight_lower_bound) & (df['weight'] <= weight_upper_bound)]

print("\nData after:")
print(f"{df.ap_lo.max()} is the max diastolic blood pressure AFTER.")
print(f"{df.weight.max()} is the max weight AFTER.")
print(f"{df.weight.min()} is the min weight AFTER.")
print(f"{df.height.max()} is the max height AFTER.")
print(f"{df.height.min()} is the min height AFTER.")

numeric_columns = df.select_dtypes(include=['float64', 'int64', 'int32']).columns
correlation_matrix = df[numeric_columns].corr()
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, mask=mask, cmap='coolwarm', vmax=1, vmin=-1, annot=True, fmt=".2f", linewidths=.5)
plt.show()