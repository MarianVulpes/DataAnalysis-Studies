import pandas as pd

df = pd.read_csv("adult.data", names=['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'], skipinitialspace=True)

print("How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)")
race_counts = df['race'].value_counts()
print(race_counts)

print("\nWhat is the average age of men?")
average_men_age = df[df['sex'] == "Male"]["age"].mean()
print(f"{average_men_age:.2f}  years old.")

print("\nWhat is the percentage of people who have a Bachelor's degree?")
bachelor_percent = (df[df["education"] == "Bachelors"].shape[0] / df.shape[0]) * 100
print(f"{bachelor_percent:.2f} percent.")

print("\nWhat percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?")
high_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
high_salary_with_education = (high_education[high_education['salary'] == '>50K'].shape[0] / high_education.shape[0]) * 100
print(f"{high_salary_with_education:.2f} percent.")

print("\nWhat percentage of people without advanced education make more than 50K?")
low_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
high_salary_without_education = (low_education[low_education['salary'] == '<=50K'].shape[0] / low_education.shape[0]) * 100
print(f"{high_salary_without_education:.2f} percent.")

print("\nWhat is the minimum number of hours a person works per week?")
print(f"{df['hours-per-week'].min()} hours per week.")

print("\nWhat percentage of the people who work the minimum number of hours per week have a salary of more than 50K?")
minimun_hours_week = df[df['hours-per-week'] == 1]
rich_doing_nothing = (minimun_hours_week[minimun_hours_week['salary'] == '>50K'].shape[0] / minimun_hours_week.shape[0]) * 100
print(f"{rich_doing_nothing} percent of employees work 1 hour per week.")


print("\nWhat country has the highest percentage of people that earn >50K and what is that percentage?")
countries_percent = (df[df['salary'] =='>50K']['native-country'].value_counts(ascending=False) / df['native-country'].value_counts() * 100).sort_values(ascending=False)
print(f"{countries_percent.index[0]} is the country with highest percentage of people earning >50K, being {countries_percent.iloc[0]:.2f}")

print("\nIdentify the most popular occupation for those who earn >50K in India.")
popular_occupation_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts(ascending=False)
print(f"{popular_occupation_india.index[0]} is the most popular occupation in India.")