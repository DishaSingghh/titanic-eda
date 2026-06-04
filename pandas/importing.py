import pandas as pd
#csv
df = pd.read_csv('train.csv',index_col="PassengerId")
print(df)
#if json
# df=pd.read_json("relative/absoutepath")

#selection by column
#print(df[["PassengerId","Survived"]].to_string) for non  truncated data
print(df[["Survived","Name"]])


#selsction by row
print(df.loc[5,["Name","Survived"]])#by index label


# print(df.iloc["PassengerId"])
#filtering
print(df[(df["Age"]>30) & (df["Pclass"]==1)])#filtering by age and class

#aggregate functions
print(df["Age"].mean())#mean age
print(df.mean(numeric_only=True))#mean of all numeric columns
print(df.sum(numeric_only=True))
print(df["Age"].median())#median age    


