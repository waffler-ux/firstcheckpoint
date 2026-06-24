import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
'labels' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
}
df=pd.DataFrame(exam_data)
print("\n" + "="*50 + "start" + "\n")
print(df.head(3))
print("\n" + "="*50 + ">" + "\n")
df.dropna(inplace= True)
print(df)
print("\n" + "="*50 + ">" + "\n")
print(df[['name',f'score']])
print("\n" + "="*50 + ">" + "\n")
f=pd.DataFrame({'name':["suresh"],'score':[15.5],'attempts':[1],'qualify':["yes"]})
g=pd.concat([df,f])
g.drop('attempts',axis=1,inplace=True)
print(g)
print("\n" + "="*50 + ">" + "\n")
g['success']=g['score'].apply(lambda x:1 if x> 10 else 0)
print(g)
print("\n" + "="*50 + "end" + "\n")

