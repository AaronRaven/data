# Overview

I wrote this program to learn how to do data analysis with Python. While I studied R in the last module, I chose Python for this module to continue my data analysis journey.


[Software Demo Video](https://www.youtube.com/watch?v=wMQuNlAeNOQ)

# Data Analysis Results
I have used data set called [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

Program features 10 questions and answers. Below are my 3 favorite conclusions.
Question 1: What is the average score (for math, reading, and writing) for students who completed the test preparation course vs those who didn't?
Average scores for students who completed the test preparation course:
math score       70.0
reading score    74.0
writing score    74.0
Average scores for students who did not complete the test preparation course:
math score       64.0
reading score    67.0
writing score    65.0
This means that students who have prepared for tests had higher grades.

Question 7: Which parental level of education has the highest sum of writing scores?
Parental level of education with the highest sum of writing scores: some college
This means that children of educated parents have higher academic success.

Question 10: What is the correlation between the students' math scores and their reading scores?
The correlation between math scores and reading scores is 0.82
There is a strong positive relationship between math scores and reading scores.
This means that if students have good math scores, their reading scores are also high and vice versa

# Development Environment

I have used Pycharm to write the code and Visual Studio Code to submit it on git. 

I wrote it with Python. I have used Pandas for main analysis and sklearn for K clustering.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Pandas documentation](https://pandas.pydata.org/docs/)
* [Pandas Tutorial on W3Schools](https://www.w3schools.com/python/pandas/default.asp)

# Future Work

There are quite a few things that I could improve in the future. Here are some of them:
* Enhance Clustering: Currently, the clustering is done based on average grades. I could improve this by considering other factors that influence these grades, such as parental level of education, lunch type, and whether or not the student completed the test preparation course.
* Add  Visualizations: The current program doesn’t provide any visualizations. Adding visualizations like bar charts, histograms, or scatter plots could help better understand the data and the results of the analysis.
* Incorporate More Machine Learning Models: Right now, the program uses K-Means for clustering. In the future, I could add more machine learning models to predict student performance or to find hidden patterns in the data. This could include decision trees, random forest, or even neural networks for more advanced analysis.