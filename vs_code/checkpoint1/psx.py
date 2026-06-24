import pandas as pd 
students = {
    "Name": ["Ali", "Sara", "Omar", "Lina"],
    "Grade": [15, 18, 12, 17],
    "Age": [20, 21, 19, 22]
}
td=pd.DataFrame(students,index=["A","B","C","D"])
print(td.loc["B"])
print(td.iloc[2])
r=td.drop("Age",axis=1)
print(r)