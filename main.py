# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utilities import change_width, show_values

# Attach a text label above each bar, displaying its value
def annotate_bar(bars):
  for bar in bars:
    height = bar.get_height()
    plt.annotate('{}'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom')


# Read CSV files
students_df = pd.read_csv("csv/students.csv")
aptitude_test_df = pd.read_csv("csv/aptitude_test.csv")
group_discussion_df = pd.read_csv("csv/group_discussion.csv")
mocks_df = pd.read_csv("csv/mocks.csv")

# Set style and palette
sns.set_theme(style="darkgrid", palette="husl")


# Convert department and preference to category datatype
students_df["department"] = students_df["department"].astype("category")
students_df["preference"] = students_df["preference"].astype("category")

'''
/*********************************************************************************/
PIE CHART FOR NUMBER OF STUDENTS PER DEPARTMENT WHO PARTICIPATED IN MOCK PLACEMENTS
/*********************************************************************************/
'''

# Number of students per department who participated in MOCK PLACEMENTS
students_per_department = students_df["department"].value_counts()
# Total number of students who participated in MOCK PLACEMENTS 
total_students = np.sum(students_per_department.values)

students_per_department = students_df["department"].value_counts(normalize=True)
departments = students_per_department.index
num_of_students = students_per_department.values

# Create pie chart
plt.pie(num_of_students, labels=departments, normalize=False, shadow=True, autopct=lambda pct: show_values(pct, total_students), startangle=90)
plt.title("NUMBER OF STUDENTS WHO PARTICIPATED IN MOCK PLACEMENTS - DEPARTMENT WISE")
plt.show()

'''
/******************************************************************************************************************/
GROUPED BAR PLOT FOR NUMBER OF STUDENTS PER DEPARTMENT WHO PARTICIPATED IN MOCK PLACEMENTS CATEGORIZED BY PREFERENCE
/******************************************************************************************************************/
'''

# Number of students who participated in OFFLINE and ONLINE MOCK PLACEMENTS
students_offline_department = students_df[students_df["preference"] == "Offline"]["department"].value_counts().sort_index()
students_online_department  = students_df[students_df["preference"] == "Online"]["department"].value_counts().sort_index()

num_students_offline = students_offline_department.values
num_students_online  = students_online_department.values

# Width of each bar
bar_width = 0.25

# Set position of bar on X axis
r1 = np.arange(len(departments))
r2 = [x + bar_width for x in r1]

# Plot the bar graph
bar1 = plt.bar(r1, num_students_offline, width=bar_width, label="Offline")
bar2 = plt.bar(r2, num_students_online, width=bar_width, label="Online")

# Label both the bar plots
annotate_bar(bar1)
annotate_bar(bar2)

# Add xticks on the middle of the group bars
plt.xticks([r + bar_width for r in range(len(num_students_offline))], sorted(departments))
plt.yticks(np.arange(0, 120, 20))

plt.xlabel("Department")
plt.ylabel("Count Of Students")
plt.title("COUNT OF STUDENTS WHO PARTICIPATED IN ONLINE AND OFFLINE MOCK PLACEMENTS - DEPARTMENT WISE")

plt.legend()
plt.show()

# Convert department to category datatype
aptitude_test_df["department"] = aptitude_test_df["department"].astype("category")

'''
/*****************************************************/
BAR PLOT FOR AVERAGE APTITUDE TEST SCORE PER DEPARTMENT
/*****************************************************/
'''

# Series for the average aptitude test score in each department
average_aptitude_score_department = aptitude_test_df.groupby(["department"])["total_score"].mean().sort_values(ascending=True)
departments = average_aptitude_score_department.index
average_aptitude_scores = average_aptitude_score_department.values

# Create barplot 
plot = sns.barplot(x=departments, y=average_aptitude_scores)

# Annotate the bar graphs
for bar in plot.patches: 
    plot.annotate(format(bar.get_height(), '.2f'),  (bar.get_x() + bar.get_width() / 2,  
                   bar.get_height()), ha='center', va='center', size=15, xytext=(0, 8), 
                   textcoords='offset points') 

# Set bar width
change_width(plot, 0.5)

# Set values to be displayed on y-axis
plt.yticks(np.arange(5, 55, 5))

plt.xlabel("Department")
plt.ylabel("Aptitude Test Score Out Of 50")
plt.title("AVERAGE APTITUDE TEST SCORE - DEPARTMENT WISE")

plt.show()

# Convert department to category datatype
group_discussion_df["department"] = group_discussion_df["department"].astype("category")

'''
/********************************************************/
BAR PLOT FOR AVERAGE GROUP DISCUSSION SCORE PER DEPARTMENT
/********************************************************/
'''

# Series for the average GD score in each department
average_gd_score_department = group_discussion_df.groupby(["department"])["total_score"].mean().sort_values(ascending=True)
departments = average_gd_score_department.index
average_gd_scores = average_gd_score_department.values

# Create barplot 
plot = sns.barplot(x=departments, y=average_gd_scores)

# Annotate the bar graphs
for bar in plot.patches: 
    plot.annotate(format(bar.get_height(), '.2f'),  (bar.get_x() + bar.get_width() / 2,  
                   bar.get_height()), ha='center', va='center', size=15, xytext=(0, 8), 
                   textcoords='offset points') 

# Set bar width
change_width(plot, 0.5)

# Set values to be displayed on y-axis
plt.yticks(np.arange(5, 35, 5))

plt.xlabel("Department")
plt.ylabel("Group Discussion Score Out Of 30")
plt.title("AVERAGE GROUP DISCUSSION SCORE - DEPARTMENT WISE")

plt.show()

# Convert student_department, interviewer_name, interviewer_company to category datatype
mocks_df["student_department"] = mocks_df["student_department"].astype("category")
mocks_df["interviewer_name"] = mocks_df["interviewer_name"].astype("category")
mocks_df["interviewer_company"] = mocks_df["interviewer_company"].astype("category")

# Convert interview_date to date datatype
mocks_df["interview_date"] = pd.to_datetime(mocks_df["interview_date"])

'''
/**************************************************/
BAR PLOT FOR AVERAGE INTERVIEW SCORE PER DEPARTMENT
/**************************************************/
'''

# Series for the average interview score in each department
average_interview_score_department = mocks_df.groupby(["student_department"])["interview_total"].mean().sort_values(ascending=True)
departments = average_interview_score_department.index
average_interview_scores = average_interview_score_department.values

# Create barplot 
plot = sns.barplot(x=departments, y=average_interview_scores)

# Annotate the bar graphs
for bar in plot.patches: 
    plot.annotate(format(bar.get_height(), '.2f'),  (bar.get_x() + bar.get_width() / 2,  
                   bar.get_height()), ha='center', va='center', size=15, xytext=(0, 8), 
                   textcoords='offset points') 

# Set bar width
change_width(plot, 0.37)

# Set values to be displayed on y-axis
plt.yticks(np.arange(5, 35, 5))

plt.xlabel("Department")
plt.ylabel("Interview Score Out Of 30")
plt.title("AVERAGE INTERVIEW SCORE - DEPARTMENT WISE (ONLINE MOCK PLACEMENTS)")

plt.show()

'''
/***************************************************************/
BAR PLOT FOR AVERAGE NUMBER OF INTERVIEWS ATTENDED PER DEPARTMENT
/***************************************************************/
'''

# Series for the number of interviews attended by each department
interviews_per_department = mocks_df.groupby(["student_department"])["registration_number"].count()
# Series for the number of students from the department who participated in online MOCK PLACEMENTS
students_per_department = mocks_df.groupby(["student_department"])["registration_number"].nunique()

# Series for the average number of interviews a student attended in each department
average_interview_department = interviews_per_department.divide(students_per_department)
departments = average_interview_department.index
average_interview_student = average_interview_department.values

# Create barplot 
plot = sns.barplot(x=departments, y=average_interview_student)

# Annotate the bar graphs
for bar in plot.patches: 
    plot.annotate(format(bar.get_height(), '.2f'),  (bar.get_x() + bar.get_width() / 2,  
                   bar.get_height()), ha='center', va='center', size=15, xytext=(0, 8), 
                   textcoords='offset points') 

# Set bar width
change_width(plot, 0.35)

# Set values to be displayed on y-axis
plt.yticks(np.arange(0.0, 2.75, 0.25))

plt.xlabel("Department")
plt.ylabel("Number of Interviews Attended")
plt.title("AVERAGE NUMBER OF INTERVIEWS ATTENDED BY A STUDENT - DEPARTMENT WISE (ONLINE MOCK PLACEMENTS)")

plt.show()
