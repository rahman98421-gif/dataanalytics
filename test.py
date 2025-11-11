import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\rahma\Downloads\data_with_canceled_appointments.csv")
print(df)

print("Data Info:")
df.info()
print("\nData Description:")
print(df.describe())
print(df.head())

print("Total doctor:", df["Doctor"].unique())
print("type:", df["VisitType"].unique())
print("VisitType:", df["VisitType"].unique())

print("AppointmentDateTime (min):", df['AppointmentDateTime'].max)
print("AppointmentDateTime (min):", df['AppointmentDateTime'].min)
print(df)

# nulldatas:

print("null datas:")
print(df.isnull().sum())

# attened_Patient:

attened_Patient= df[df['CanceledAppointment'] ==False]

print(attened_Patient)


# missed_appointments:

missed_appointments= df[df['MissedAppointment'] == True]

print(missed_appointments)

# clean_visited_Patient:

clean_visited_Patient= df[df['AppointmentDateTime'] >="2025-11-10"]

print(clean_visited_Patient)

# canceld appointments:

canceld_appointments= df[df['CanceledAppointment'] ==True]

print(canceld_appointments)

# count of gender:

gender_counts = df['Gender'].value_counts()

print(gender_counts)


# Diagnosis:

Diagnosis = df[(df['Diagnosis'] == "level")]
print(Diagnosis)
Diagnosis = df[(df['Diagnosis'] == "range")]
print(Diagnosis)
Diagnosis = df[(df['Diagnosis'] == "interesting")]
print(Diagnosis)

# VisitType and Diagnosis:

VisitType = df[(df['VisitType'] == "Checkup") & (df['Diagnosis'] =="level")]
print(VisitType)

from sqlalchemy import create_engine
username="root"
password="root"
host="localhost"
port="3306"
database="yasin"

engine=create_engine(f"mysql+pymysql://root:root@localhost:3306/yasin")
table_name="std"
df.to_sql(table_name,engine,if_exists='replace',index=False)
print("\nData successfully saved to MySQL table:",table_name)