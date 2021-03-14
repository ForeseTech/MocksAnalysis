# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV files
aptitude_test_df = pd.read_csv("aptitude_test.csv")
group_discussion_df = pd.read_csv("group_discussion.csv")
mocks_df = pd.read_csv("mocks.csv")

def func(pct, allvals):
    absolute = round(pct / 100.*np.sum(allvals))
    return "{:d}".format(absolute)

# Set seaborn style
sns.set_style(style="darkgrid")

# Convert department to category datatype
aptitude_test_df["department"] = aptitude_test_df["department"].astype("category")

# Series for the average aptitude test score in each department
average_aptitude_score_department = aptitude_test_df.groupby(["department"])["total_score"].mean().sort_values(ascending=True)
departments = average_aptitude_score_department.index
average_aptitude_scores = average_aptitude_score_department.values

# Create barplot 
plots = sns.barplot(x=departments, y=average_aptitude_scores, color="salmon")

# Annotate the bar graphs
for bar in plots.patches: 
    plots.annotate(format(bar.get_height(), '.2f'),  (bar.get_x() + bar.get_width() / 2,  
                   bar.get_height()), ha='center', va='center', size=15, xytext=(0, 8), 
                   textcoords='offset points') 

# Set values to be displayed on y-axis
plt.yticks(np.arange(5, 55, 5))

# Set x-axis label, y-axis label and title
plt.xlabel("Department")
plt.ylabel("Aptitude Test Score Out Of 50")
plt.title("AVERAGE APTITUDE TEST SCORE - DEPARTMENT WISE")
plt.show()

# Convert department to category datatype
group_discussion_df["department"] = group_discussion_df["department"].astype("category")

# Series for the average GD score in each department
average_gd_score_department = group_discussion_df.groupby(["department"])["total_score"].mean().sort_values(ascending=True)
departments = average_gd_score_department.index
average_gd_scores = average_gd_score_department.values

# Create barplot 
plots = sns.barplot(x=departments, y=average_gd_scores)

# Annotate the bar graphs
for bar in plots.patches: 
    plots.annotate(format(bar.get_height(), '.2f'),  (bar.get_x() + bar.get_width() / 2,  
                   bar.get_height()), ha='center', va='center', size=15, xytext=(0, 8), 
                   textcoords='offset points') 

# Set values to be displayed on y-axis
plt.yticks(np.arange(5, 35, 5))

# Set x-axis label, y-axis label and title
plt.xlabel("Department")
plt.ylabel("Group Discussion Score Out Of 30")
plt.title("AVERAGE GROUP DISCUSSION SCORE - DEPARTMENT WISE")
plt.show()

# Convert student_department, student_section interviewer_name, interviewer_company to category datatype
mocks_df["student_department"] = mocks_df["student_department"].astype("category")
mocks_df["student_section"] = mocks_df["student_section"].astype("category")
mocks_df["interviewer_name"] = mocks_df["interviewer_name"].astype("category")
mocks_df["interviewer_company"] = mocks_df["interviewer_company"].astype("category")

# Convert interview_date to date datatype
mocks_df["interview_date"] = pd.to_datetime(mocks_df["interview_date"])

# Get number of students per department who participated in online MOCK PLACEMENTS
students_per_department = mocks_df.groupby(["student_department"])["registration_number"].nunique()
# Get total number of students who participated in online MOCK PLACEMENTS
total_students = students_per_department.values.sum()
# Normalize the number of students
students_per_department_normalized = students_per_department / total_students
departments = students_per_department_normalized.index
students_percentage = students_per_department_normalized.values

# Create pie chart
plt.pie(students_percentage, labels=departments, normalize=False, shadow=True, autopct=lambda pct: func(pct, students_per_department), startangle=90)
plt.title("NUMBER OF STUDENTS - DEPARTMENT WISE (ONLINE MOCK PLACEMENTS)")
plt.show()

# Series for the average interview score in each department
average_interview_score_department = mocks_df.groupby(["student_department"])["interview_total"].mean().sort_values(ascending=True)
departments = average_interview_score_department.index
average_interview_scores = average_interview_score_department.values

plots = sns.barplot(x=departments, y=average_interview_score)

# Annotate the bar graphs
for bar in plots.patches:

    plots.annotate(
                   format(bar.get_height(), '.2f'),  (bar.get_x() + bar.get_width() / 2,
                   bar.get_height()), ha='center', va='center', size=15, xytext=(0, 8),
                   textcoords='offset points'
                  )
=======
# Create barplot 
plots = sns.barplot(x=departments, y=average_interview_scores)

# Annotate the bar graphs
for bar in plots.patches: 
    plots.annotate(format(bar.get_height(), '.2f'),  (bar.get_x() + bar.get_width() / 2,  
                   bar.get_height()), ha='center', va='center', size=15, xytext=(0, 8), 
                   textcoords='offset points') 

# Set values to be displayed on y-axis
plt.yticks(np.arange(5, 35, 5))

# Set x-axis label, y-axis label and title
plt.xlabel("Department")
plt.ylabel("Interview Score Out Of 30")
plt.title("AVERAGE INTERVIEW SCORE - DEPARTMENT WISE (ONLINE MOCK PLACEMENTS)")
plt.show()

#Deriving the DataFrame for the interview score for each department on 20-02-2021
options = ['20-02-2021']
student_deets_20 = mocks_df[mocks_df['interview_date'].isin(options)] #Selecting only the rows which had interview_date 20-02-2021
average_interview_score_department_20 = student_deets_20.groupby(["student_department"])["interview_total"].mean().sort_values(ascending=True) #Getting the mean of the interview_total group by department
average_interview_score_department_20_NaN = average_interview_score_department_20.fillna(0) #Replacing the NaN values with 0
departments_20 = average_interview_score_department_20.index
average_interview_score_20 = average_interview_score_department_20_NaN.values

print(average_interview_score_department_20_NaN)

#Plotting the graph
sns.set_style(style="darkgrid")
plots = sns.barplot(x=departments_20, y=average_interview_score_20)

# Annotate the bar graphs
for bar in plots.patches:

    plots.annotate(
                   format(bar.get_height(), '.2f'),  (bar.get_x() + bar.get_width() / 2,
                   bar.get_height()), ha='center', va='center', size=15, xytext=(0, 8),
                   textcoords='offset points'
                  )

plt.yticks(np.arange(5, 35, 5))
plt.xlabel("Department")
plt.ylabel("Interview Score Out Of 30")
plt.title("AVERAGE INTERVIEW SCORE - DEPARTMENT WISE (ONLINE MOCK PLACEMENTS - 20/02/2021)")
plt.show()


#Deriving the DataFrame for the interview score for each department on 21-02-2021
options = ['21-02-2021']
student_deets_21 = mocks_df[mocks_df['interview_date'].isin(options)] #Selecting only the rows which had interview_date 21-02-2021
average_interview_score_department_21 = student_deets_21.groupby(["student_department"])["interview_total"].mean().sort_values(ascending=True) #Getting the mean of the interview_total group by department
average_interview_score_department_21_NaN = average_interview_score_department_21.fillna(0) #Replacing the NaN values with 0
departments_21 = average_interview_score_department_21.index
average_interview_score_21 = average_interview_score_department_21_NaN.values

print(average_interview_score_department_21_NaN)

#Plotting the graph
sns.set_style(style="darkgrid")
plots = sns.barplot(x=departments_21, y=average_interview_score_21)

# Annotate the bar graphs
for bar in plots.patches:

    plots.annotate(
                   format(bar.get_height(), '.2f'),  (bar.get_x() + bar.get_width() / 2,
                   bar.get_height()), ha='center', va='center', size=15, xytext=(0, 8),
                   textcoords='offset points'
                  )

plt.yticks(np.arange(5, 35, 5))
plt.xlabel("Department")
plt.ylabel("Interview Score Out Of 30")
plt.title("AVERAGE INTERVIEW SCORE - DEPARTMENT WISE (ONLINE MOCK PLACEMENTS - 21/02/2021)")
=======
# Series for the number of interviews attended by each department
interviews_per_department = mocks_df.groupby(["student_department"])["registration_number"].count()
# Series for the number of students from the department who participated in online MOCK PLACEMENTS
students_per_department = mocks_df.groupby(["student_department"])["registration_number"].nunique()

# Series for the average number of interviews a student attended in each department
average_interview_department = interviews_per_department.divide(students_per_department)
departments = average_interview_department.index
average_interview_student = average_interview_department.values

# Create barplot 
plots = sns.barplot(x=departments, y=average_interview_student)

# Annotate the bar graphs
for bar in plots.patches: 
    plots.annotate(format(bar.get_height(), '.2f'),  (bar.get_x() + bar.get_width() / 2,  
                   bar.get_height()), ha='center', va='center', size=15, xytext=(0, 8), 
                   textcoords='offset points') 

# Set values to be displayed on y-axis
plt.yticks(np.arange(0.0, 2.75, 0.25))

# Set x-axis label, y-axis label and title
plt.xlabel("Department")
plt.ylabel("Number of Interviews Attended")
plt.title("AVERAGE NUMBER OF INTERVIEWS ATTENDED BY A STUDENT - DEPARTMENT WISE (ONLINE MOCK PLACEMENTS)")
plt.show()
