
import pandas as pd
import math

data = {
    "Name": ["Ali", "Sara", "Omar", "Sara", None, "Lina"],
    "Age": [25, 30, None, 30, 28, 200],
    "Department": ["IT", "HR", "IT", "HR", "Sales", "Marketing"],
    "Salary": [50000, 60000, 55000, 60000, None, 70000]
}

df = pd.DataFrame(data)

# df.info()
f=0
for i in df.index:
    for g in df.loc[i]:
        if pd.isnull(g):
            f=f+1
print("there are",f,"missing values.")
print("\n" + "="*50 + ">" + "\n")
print(df)
print("\n" + "="*50 + ">" + "\n")
p=df["Salary"].min()
print("the missing salary is : ",p,".")
print("\n" + "="*50 + ">" + "\n")
for x in df.index:
    if df.loc[x,"Age"] > 100 :
        df.drop(x,inplace=True)
new_index=df.reset_index()
print(new_index)