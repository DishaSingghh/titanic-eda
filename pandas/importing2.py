import pandas as pd
data= pd.read_csv('train.csv',index_col="PassengerId")
df=pd.DataFrame(data)
passengerId=int(input("enter id"))
try:
    print(df.loc[passengerId,["Name","Survived"]])
except KeyError:
    print("PassengerId not found in the dataset")

