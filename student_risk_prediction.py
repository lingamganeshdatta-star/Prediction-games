import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data={
     "Maths":np.random.randint(40,100,50),
     "Science":np.random.randint(40,100,50),
     "English":np.random.randint(40,100,50),
     "History":np.random.randint(40,100,50),
     "Attendace":np.random.randint(50,100,50),
     "DisciplinaryCase":np.random.randint(0,3,50)
    }
df = pd.DataFrame(data)
print("dataset preview:\n",df.head())
df["AverageScore"]=df[["Maths","Science","English","History"]].mean(axis=1)
df["AttendanceStatus"]=np.where(df["Attendace"]<75,"Low","Good")


print(df.dtypes)
df["RiskScore"]=(
    (75-df["Attendace"]) +  
    df["DisciplinaryCase"]+
    (60-df["AverageScore"])*15
)
    
    
print(df["RiskScore"].head(10))
print("Min:",df["RiskScore"].min())
print("Max:",df["RiskScore"].max())

conditions=[
    df["RiskScore"]>=70,
    (df["RiskScore"]<70)&(df["RiskScore"]>=60),
    df["RiskScore"]<60
    ]
choices=["HIGH","MIDIUM","LOW"]
df["RiskLevel"]=np.select(conditions,choices,default="UNKNOWN")
print("\nRisk Level Distributiion:\n",df["RiskLevel"].value_counts())



plt.figure()
df["RiskLevel"].value_counts().plot(kind="bar")
plt.title("Student Dropout Risk Leveks")
plt.xlabel("RiskLevel")
plt.ylabel("Number of Students")
plt.show()


plt.figure()
plt.scatter(df["Attendace"],df["AverageScore"])
plt.title("Attendace vs Average Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Score")
plt.show()


plt.figure()
df.groupby("RiskLevel")["Attendace"].plot(kind="bar")
plt.title("Avarage Score by Attendance Status")
plt.xlabel("Attendance Status")
plt.ylabel("Average score")
plt.show()
