# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
# Load the dataset
df = pd.read_csv('StudentsPerformance.csv')

# Question 1: What is the average score (for math, reading, and writing) for students who have completed the test preparation course vs those who didn't?
# This code filters the dataframe for students who completed the test preparation course, calculates the average scores, rounds them to the nearest whole number,
# does the same for students who did not complete the course, and calculates the difference between the two averages
df_prep = df[df['test preparation course'] == 'completed']
avg_prep = df_prep[['math score', 'reading score', 'writing score']].mean().round()
df_no_prep = df[df['test preparation course'] == 'none']
avg_no_prep = df_no_prep[['math score', 'reading score', 'writing score']].mean().round()
difference = avg_prep - avg_no_prep

print("Average scores for students who completed the test preparation course:")
print(avg_prep)
print("\nAverage scores for students who did not complete the test preparation course:")
print(avg_no_prep)
print("\nDifference in average scores:")
print(difference)

# Question 2: Which race/ethnicity has the highest average math score?
# This code groups the dataframe by race/ethnicity, calculates the average math score for each group, and identifies the group with the highest average
df_grouped = df.groupby('race/ethnicity').mean()
highest_math = df_grouped['math score'].idxmax()
print("\nRace/ethnicity with the highest average math score:", highest_math)


# Question 3: How many students have a math score above 90?
# This code filters the dataframe for students with a math score above 90 and counts the number of such students
high_math_students = df[df['math score'] > 90].shape[0]
print("\nNumber of students with a math score above 90:", high_math_students)

# Question 4: Convert the scores into grades (A, B, C, D, F) and find out the distribution of grades among students.
# This code defines a function to convert scores into grades, applies this function to the math scores to create a new column of math grades, and calculates the distribution of math grades
def convert_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
df['math grade'] = df['math score'].apply(convert_to_grade)
grade_distribution = df['math grade'].value_counts()
print("\nDistribution of math grades:")
print(grade_distribution)

# Question 5: Can we cluster students based on their performance in math, reading, and writing? What characteristics do students in each cluster share?
# This code applies the K-Means clustering algorithm to the scores, adds the cluster labels to the dataframe, and prints the average scores for each cluster
# Round the scores to the nearest whole number
df_rounded = df.round({'math score': 0, 'reading score': 0, 'writing score': 0})
# This code applies the K-Means clustering algorithm to the scores, adds the cluster labels to the dataframe, and prints the average scores for each cluster
kmeans = KMeans(n_clusters=3)
df_rounded['cluster'] = kmeans.fit_predict(df_rounded[['math score', 'reading score', 'writing score']])
cluster_averages = df_rounded.groupby('cluster')[['math score', 'reading score', 'writing score']].mean()

# Print the average scores for each cluster, rounded to the nearest whole number
print("Average scores for each cluster (rounded to the nearest whole number):")
print(cluster_averages.round())

# Question 6: What is the average reading score for students whose parents have a bachelor's degree?
# This code filters the dataframe for students whose parents have a bachelor's degree and calculates the average reading score
df_bachelors = df[df['parental level of education'] == "bachelor's degree"]
avg_reading_bachelors = df_bachelors['reading score'].mean()
print("\nAverage reading score for students whose parents have a bachelor's degree:", avg_reading_bachelors)

# Question 7: Which parental level of education has the highest sum of writing scores?
# This code groups the dataframe by parental level of education, calculates the sum of writing scores for each group, and identifies the group with the highest sum
df_grouped = df.groupby('parental level of education').sum()
highest_writing = df_grouped['writing score'].idxmax()
print("\nParental level of education with the highest sum of writing scores:", highest_writing)

# Question 8: What is the average math score for students who have standard lunch?
# This code filters the dataframe for students who have standard lunch and calculates the average math score
df_standard = df[df['lunch'] == 'standard']
avg_math_standard = df_standard['math score'].mean()

print("\nAverage math score for students who have standard lunch:", round(avg_math_standard, 2))


# Question 9: Convert the scores into pass/fail and find out the number of students who passed in all three subjects.
# This code defines a function to convert scores into pass/fail, applies this function to the scores to create new columns of pass/fail results, and counts the number of students who passed in all three subjects
def convert_to_pass_fail(score):
    return 'Pass' if score >= 60 else 'Fail'
df['math result'] = df['math score'].apply(convert_to_pass_fail)
df['reading result'] = df['reading score'].apply(convert_to_pass_fail)
df['writing result'] = df['writing score'].apply(convert_to_pass_fail)
pass_all_subjects = df[(df['math result'] == 'Pass') & (df['reading result'] == 'Pass') & (df['writing result'] == 'Pass')].shape[0]
print("\nNumber of students who passed in all three subjects:", pass_all_subjects)

# Question 10: What is the correlation between the students' math scores and their reading scores?
# This code calculates the correlation between the students' math scores and their reading scores
correlation = df['math score'].corr(df['reading score'])
print("\nThe correlation between math scores and reading scores is", round(correlation, 2))

# Interpretation of the correlation
if correlation > 0.7:
    print("There is a strong positive relationship between math scores and reading scores.")
elif correlation > 0.3:
    print("There is a moderate positive relationship between math scores and reading scores.")
elif correlation > 0:
    print("There is a weak positive relationship between math scores and reading scores.")
elif correlation > -0.3:
    print("There is a weak negative relationship between math scores and reading scores.")
elif correlation > -0.7:
    print("There is a moderate negative relationship between math scores and reading scores.")
else:
    print("There is a strong negative relationship between math scores and reading scores.")