# Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utilities import change_width, show_values

# Attach a text label above each vertical bar, displaying its value
def annotate_bar(bars):
    for bar in bars:
        height = bar.get_height()
        plt.annotate(
            "{}".format(height),
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


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

"""
/**************************************************************************************************/
PIE CHART FOR NUMBER OF STUDENTS WHO PARTICIPATED IN MOCK PLACEMENTS CATEGORIZED BY MODE PREFERENCE
/**************************************************************************************************/
"""

# Number of interviews held on 20/01/2021 and 21/02/2021
num_of_students_mode = students_df["preference"].value_counts()
# Total number of students who participated in MOCK PLACEMENTS
total_students = np.sum(num_of_students_mode.values)

# Number of interviews held on 20/01/2021 and 21/02/2021
num_of_students_mode = (
    students_df["preference"].value_counts(normalize=True).sort_index()
)
modes = num_of_students_mode.index
num_of_students = num_of_students_mode.values

# Create pie chart
plt.pie(
    num_of_students,
    labels=modes,
    normalize=False,
    shadow=True,
    autopct=lambda pct: show_values(pct, total_students),
    startangle=90,
)
plt.title("NUMBER OF STUDENTS WHO PARTICIPATED IN MOCK PLACEMENTS - MODE WISE")
plt.show()

"""
/*********************************************************************************/
PIE CHART FOR NUMBER OF STUDENTS PER DEPARTMENT WHO PARTICIPATED IN MOCK PLACEMENTS
/*********************************************************************************/
"""

# Number of students per department who participated in MOCK PLACEMENTS
students_per_department = students_df["department"].value_counts()
# Total number of students who participated in MOCK PLACEMENTS
total_students = np.sum(students_per_department.values)

students_per_department = students_df["department"].value_counts(normalize=True)
departments = students_per_department.index
num_of_students = students_per_department.values

# Create pie chart
plt.pie(
    num_of_students,
    labels=departments,
    normalize=False,
    shadow=True,
    autopct=lambda pct: show_values(pct, total_students),
    startangle=90,
)
plt.title("NUMBER OF STUDENTS WHO PARTICIPATED IN MOCK PLACEMENTS - DEPARTMENT WISE")
plt.show()

"""
/**********************************************************************************************************************/
GROUPED BAR PLOT FOR NUMBER OF STUDENTS PER DEPARTMENT WHO REGISTERED FOR MOCK PLACEMENTS CATEGORIZED BY INTERVIEW MODE
/**********************************************************************************************************************/
"""

# Number of students who participated in OFFLINE and ONLINE MOCK PLACEMENTS
students_offline_department = (
    students_df[students_df["preference"] == "Offline"]["department"]
    .value_counts()
    .sort_index()
)
students_online_department = (
    students_df[students_df["preference"] == "Online"]["department"]
    .value_counts()
    .sort_index()
)

num_students_offline = students_offline_department.values
num_students_online = students_online_department.values

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
plt.xticks(
    [r + bar_width for r in range(len(num_students_offline))], sorted(departments)
)
plt.yticks(np.arange(0, 120, 20))

plt.xlabel("Department")
plt.ylabel("Count Of Students")
plt.title(
    "COUNT OF STUDENTS WHO PARTICIPATED IN ONLINE AND OFFLINE MOCK PLACEMENTS - DEPARTMENT WISE"
)

plt.legend()
plt.show()

# Convert department to category datatype
aptitude_test_df["department"] = aptitude_test_df["department"].astype("category")

"""
/*****************************************************/
BAR PLOT FOR AVERAGE APTITUDE TEST SCORE PER DEPARTMENT
/*****************************************************/
"""

# Series for the average aptitude test score in each department
average_aptitude_score_department = (
    aptitude_test_df.groupby(["department"])["total_score"]
    .mean()
    .sort_values(ascending=True)
)
departments = average_aptitude_score_department.index
average_aptitude_scores = average_aptitude_score_department.values

# Create barplot
plot = sns.barplot(x=departments, y=average_aptitude_scores)

# Annotate the bar graphs
for bar in plot.patches:
    plot.annotate(
        format(bar.get_height(), ".2f"),
        (bar.get_x() + bar.get_width() / 2, bar.get_height()),
        ha="center",
        va="center",
        size=15,
        xytext=(0, 8),
        textcoords="offset points",
    )

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

"""
/********************************************************/
BAR PLOT FOR AVERAGE GROUP DISCUSSION SCORE PER DEPARTMENT
/********************************************************/
"""

# Series for the average GD score in each department
average_gd_score_department = (
    group_discussion_df.groupby(["department"])["total_score"]
    .mean()
    .sort_values(ascending=True)
)
departments = average_gd_score_department.index
average_gd_scores = average_gd_score_department.values

# Create barplot
plot = sns.barplot(x=departments, y=average_gd_scores)

# Annotate the bar graphs
for bar in plot.patches:
    plot.annotate(
        format(bar.get_height(), ".2f"),
        (bar.get_x() + bar.get_width() / 2, bar.get_height()),
        ha="center",
        va="center",
        size=15,
        xytext=(0, 8),
        textcoords="offset points",
    )

# Set bar width
change_width(plot, 0.5)

# Set values to be displayed on y-axis
plt.yticks(np.arange(5, 35, 5))

plt.xlabel("Department")
plt.ylabel("Group Discussion Score Out Of 30")
plt.title("AVERAGE GROUP DISCUSSION SCORE - DEPARTMENT WISE")

plt.show()

# Convert student_department, interviewer to category datatype
mocks_df["student_department"] = mocks_df["student_department"].astype("category")
mocks_df["interview_mode"] = mocks_df["interview_mode"].astype("category")

mocks_online_df = mocks_df[mocks_df["interview_mode"] == "Online"]
mocks_offline_df = mocks_df[mocks_df["interview_mode"] == "Offline"]

mocks_20_df = mocks_df[mocks_df["interview_date"] == "20-02-2021"]
mocks_21_df = mocks_df[mocks_df["interview_date"] == "21-02-2021"]
mocks_27_df = mocks_df[mocks_df["interview_date"] == "27-02-2021"]
mocks_28_df = mocks_df[mocks_df["interview_date"] == "28-02-2021"]

"""
/*********************************************************/
PIE CHART FOR NUMBER OF INTERVIEWS CONDUCTED ON EACH DATE
/*********************************************************/
"""

# Number of interviews held on each date
number_of_interviews_date = mocks_df["interview_date"].value_counts()
# Total number of students who participated in MOCK PLACEMENTS
total_interviews = np.sum(number_of_interviews_date.values)

# Number of interviews held on each date
number_of_interviews_date = mocks_df["interview_date"].value_counts(normalize=True)
dates = number_of_interviews_date.index
num_of_interviews = number_of_interviews_date.values

# Create pie chart
plt.pie(
    num_of_interviews,
    labels=dates,
    normalize=False,
    shadow=True,
    autopct=lambda pct: show_values(pct, total_interviews),
    startangle=90,
)
plt.title("NUMBER OF INTERVIEWS CONDUCTED DURING MOCK PLACEMENTS - DATE WISE")
plt.show()

"""
/*****************************************************************************************/
GROUPED BAR PLOT FOR AVERAGE INTERVIEW SCORE PER DEPARTMENT CATEGORIZED BY INTERVIEW MODE
/*****************************************************************************************/
"""

# Series for the average interview score in each department
average_interview_score_department_online = mocks_online_df.groupby(
    ["student_department"]
)["interview_total"].mean()

average_interview_score_department_offline = mocks_offline_df.groupby(
    ["student_department"]
)["interview_total"].mean()

average_interview_scores_online = (
    average_interview_score_department_online.values.round(2)
)
average_interview_scores_offline = (
    average_interview_score_department_offline.values.round(2)
)

# Width of each bar
bar_width = 0.40

# Set position of bar on X axis
r1 = np.arange(len(departments))
r2 = [x + bar_width for x in r1]

# Plot the bar graph
bar1 = plt.bar(r1, average_interview_scores_offline, width=bar_width, label="Offline")
bar2 = plt.bar(r2, average_interview_scores_online, width=bar_width, label="Online")

# Label both the bar plots
annotate_bar(bar1)
annotate_bar(bar2)

# Add xticks on the middle of the group bars
plt.xticks(
    [r + bar_width for r in range(len(num_students_offline))], sorted(departments)
)
plt.yticks(np.arange(0, 35, 5))

plt.xlabel("Department")
plt.ylabel("Interview Score Out Of 30")
plt.title("AVERAGE INTERVIEW SCORE - DEPARTMENT WISE")

plt.legend()
plt.show()

"""
/*******************************************************************************************************************/
GROUPED BAR PLOT FOR AVERAGE NUMBER OF INTERVIEWS ATTENDED BY A STUDENT PER DEPARTMENT CATEGORIZED BY INTERVIEW MODE
/*******************************************************************************************************************/
"""

# Series for the number of interviews attended by each department in online MOCK PLACEMENTS
interviews_per_department_online = mocks_online_df.groupby(["student_department"])[
    "registration_number"
].count()

# Series for the number of interviews attended by each department in online MOCK PLACEMENTS
interviews_per_department_offline = mocks_offline_df.groupby(["student_department"])[
    "registration_number"
].count()

# Series for the number of students from the department who participated in online MOCK PLACEMENTS
students_per_department_online = mocks_online_df.groupby(["student_department"])[
    "registration_number"
].nunique()

# Series for the number of students from the department who participated in offline MOCK PLACEMENTS
students_per_department_offline = mocks_offline_df.groupby(["student_department"])[
    "registration_number"
].nunique()

# Series for the average number of interviews a student attended in each department in online MOCK PLACEMENTS
average_interview_department_online = interviews_per_department_online.divide(
    students_per_department_online
)

# Series for the average number of interviews a student attended in each department in offline MOCK PLACEMENTS
average_interview_department_offline = interviews_per_department_offline.divide(
    students_per_department_offline
)

# Width of each bar
bar_width = 0.385

# Set position of bar on X axis
r1 = np.arange(len(departments))
r2 = [x + bar_width for x in r1]

# Plot the bar graph
bar1 = plt.bar(
    r1,
    average_interview_department_offline.values.round(2),
    width=bar_width,
    label="Offline",
)
bar2 = plt.bar(
    r2,
    average_interview_department_online.values.round(2),
    width=bar_width,
    label="Online",
)

# Label both the bar plots
annotate_bar(bar1)
annotate_bar(bar2)

# Add xticks on the middle of the group bars
plt.xticks(
    [r + bar_width for r in range(len(num_students_offline))], sorted(departments)
)
plt.yticks(np.arange(0, 4, 1))


plt.xlabel("Department")
plt.ylabel("Number of Interviews Attended")
plt.title("AVERAGE NUMBER OF INTERVIEWS ATTENDED BY A STUDENT - DEPARTMENT WISE")

plt.legend()
plt.show()

"""
/*********************************************************/
BAR PLOT FOR AVERAGE SCORE AWARDED BY EACH HR ON 20/02/2021
/*********************************************************/
"""

average_interview_score_20 = mocks_20_df.groupby(["interviewer"])[
    "interview_total"
].mean()
interviewer_20 = average_interview_score_20.index
average_score_20 = average_interview_score_20.values

plot = sns.barplot(x=average_score_20, y=interviewer_20)

for bar in plot.patches:
    plot.text(
        0.75 + bar.get_width(),
        bar.get_y() + 0.55 * bar.get_height(),
        "{:1.2f}".format(bar.get_width()),
        ha="center",
        va="center",
    )

plt.xticks(np.arange(0, 35, 5))
plt.xlabel("Interview Score Out Of 30")
plt.ylabel("Interviewer")
plt.title("AVERAGE SCORE AWARDED BY EACH HR ON 20/02/2021")

plt.show()

"""
/*********************************************************/
BAR PLOT FOR AVERAGE SCORE AWARDED BY EACH HR ON 21/02/2021
/*********************************************************/
"""

average_interview_score_21 = mocks_21_df.groupby(["interviewer"])[
    "interview_total"
].mean()
interviewer_21 = average_interview_score_21.index
average_score_21 = average_interview_score_21.values

plot = sns.barplot(x=average_score_21, y=interviewer_21)

for bar in plot.patches:
    plot.text(
        0.75 + bar.get_width(),
        bar.get_y() + 0.55 * bar.get_height(),
        "{:1.2f}".format(bar.get_width()),
        ha="center",
        va="center",
    )

plt.xticks(np.arange(0, 35, 5))
plt.xlabel("Interview Score Out Of 30")
plt.ylabel("Interviewer")
plt.title("AVERAGE SCORE AWARDED BY EACH HR ON 21/02/2021")

plt.show()

"""
/*********************************************************/
BAR PLOT FOR AVERAGE SCORE AWARDED BY EACH HR ON 27/02/2021
/*********************************************************/
"""

average_interview_score_27 = mocks_27_df.groupby(["interviewer"])[
    "interview_total"
].mean()
interviewer_27 = average_interview_score_27.index
average_score_27 = average_interview_score_27.values

plot = sns.barplot(x=average_score_27, y=interviewer_27)

for bar in plot.patches:
    plot.text(
        0.75 + bar.get_width(),
        bar.get_y() + 0.55 * bar.get_height(),
        "{:1.2f}".format(bar.get_width()),
        ha="center",
        va="center",
    )

plt.xticks(np.arange(0, 35, 5))
plt.xlabel("Interview Score Out Of 30")
plt.ylabel("Interviewer")
plt.title("AVERAGE SCORE AWARDED BY EACH HR ON 27/02/2021")

plt.show()

"""
/*********************************************************/
BAR PLOT FOR AVERAGE SCORE AWARDED BY EACH HR ON 28/02/2021
/*********************************************************/
"""

average_interview_score_28 = mocks_28_df.groupby(["interviewer"])[
    "interview_total"
].mean()
interviewer_28 = average_interview_score_28.index
average_score_28 = average_interview_score_28.values

plot = sns.barplot(x=average_score_28, y=interviewer_28)

for bar in plot.patches:
    plot.text(
        0.75 + bar.get_width(),
        bar.get_y() + 0.55 * bar.get_height(),
        "{:1.2f}".format(bar.get_width()),
        ha="center",
        va="center",
    )

plt.xticks(np.arange(0, 35, 5))
plt.xlabel("Interview Score Out Of 30")
plt.ylabel("Interviewer")
plt.title("AVERAGE SCORE AWARDED BY EACH HR ON 28/02/2021")

plt.show()

"""
/*******************************************************************/
BAR PLOT FOR NUMBER OF STUDENTS INTERVIEWED BY EACH HR ON 20/02/2021
/*******************************************************************/
"""

students_per_interviewer_20 = mocks_20_df["interviewer"].value_counts()
interviewer_20 = students_per_interviewer_20.index
num_of_students_20 = students_per_interviewer_20.values

# Create barplot
plot = sns.barplot(x=num_of_students_20, y=interviewer_20)

# Annotate the bar graphs
for bar in plot.patches:
    plot.text(
        0.22 + bar.get_width(),
        bar.get_y() + 0.55 * bar.get_height(),
        "{:1.0f}".format(bar.get_width()),
        ha="center",
        va="center",
    )

plt.xticks(np.arange(0, 30, 5))
plt.xlabel("Number Of Students Interviewed")
plt.ylabel("Interviewer")
plt.title("NUMBER OF STUDENTS INTERVIEWED BY EACH HR ON 20/02/2021")

plt.show()

"""
/*******************************************************************/
BAR PLOT FOR NUMBER OF STUDENTS INTERVIEWED BY EACH HR ON 21/02/2021
/*******************************************************************/
"""

students_per_interviewer_21 = mocks_21_df["interviewer"].value_counts()
interviewer_21 = students_per_interviewer_21.index
num_of_students_21 = students_per_interviewer_21.values

# Create barplot
plot = sns.barplot(x=num_of_students_21, y=interviewer_21)

# Annotate the bar graphs
for bar in plot.patches:
    plot.text(
        0.25 + bar.get_width(),
        bar.get_y() + 0.55 * bar.get_height(),
        "{:1.0f}".format(bar.get_width()),
        ha="center",
        va="center",
    )

plt.xticks(np.arange(0, 30, 5))
plt.xlabel("Number Of Students Interviewed")
plt.ylabel("Interviewer")
plt.title("NUMBER OF STUDENTS INTERVIEWED BY EACH HR ON 21/02/2021")

plt.show()

"""
/*******************************************************************/
BAR PLOT FOR NUMBER OF STUDENTS INTERVIEWED BY EACH HR ON 27/02/2021
/*******************************************************************/
"""

students_per_interviewer_27 = mocks_27_df["interviewer"].value_counts()
interviewer_27 = students_per_interviewer_27.index
num_of_students_27 = students_per_interviewer_27.values

# Create barplot
plot = sns.barplot(x=num_of_students_27, y=interviewer_27)

# Annotate the bar graphs
for bar in plot.patches:
    plot.text(
        0.25 + bar.get_width(),
        bar.get_y() + 0.55 * bar.get_height(),
        "{:1.0f}".format(bar.get_width()),
        ha="center",
        va="center",
    )

plt.xticks(np.arange(0, 30, 5))
plt.xlabel("Number Of Students Interviewed")
plt.ylabel("Interviewer")
plt.title("NUMBER OF STUDENTS INTERVIEWED BY EACH HR ON 27/02/2021")

plt.show()

"""
/*******************************************************************/
BAR PLOT FOR NUMBER OF STUDENTS INTERVIEWED BY EACH HR ON 28/02/2021
/*******************************************************************/
"""

students_per_interviewer_28 = mocks_28_df["interviewer"].value_counts()
interviewer_28 = students_per_interviewer_28.index
num_of_students_28 = students_per_interviewer_28.values

# Create barplot
plot = sns.barplot(x=num_of_students_28, y=interviewer_28)

# Annotate the bar graphs
for bar in plot.patches:
    plot.text(
        0.25 + bar.get_width(),
        bar.get_y() + 0.55 * bar.get_height(),
        "{:1.0f}".format(bar.get_width()),
        ha="center",
        va="center",
    )

plt.xticks(np.arange(0, 30, 5))
plt.xlabel("Number Of Students Interviewed")
plt.ylabel("Interviewer")
plt.title("NUMBER OF STUDENTS INTERVIEWED BY EACH HR ON 28/02/2021")

plt.show()
