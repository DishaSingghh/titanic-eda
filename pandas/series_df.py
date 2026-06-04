import pandas as pd
data1=[1,2,3,4,5]
data2={"a":1,"b":2,"c":3,"d":4,"e":5}
s2=pd.Series(data2)#no index neede dict key value pairs 
print(s2)
s1=pd.Series(data1,index=["a","b","c","d","e"])
print(s1)

#dataframe
data={"Names":["Alice","Bob"],"Age":[19,30],"Salary":[50000000,6000000]}
df=pd.DataFrame(data,index=["emp1","emp2"])
print(df)
#add a col
df["job"]=["manager","developer"]
print(df)
#add a row
newrow=pd.DataFrame({"Names":"Charlie","Age":25,"Salary":7000000,"job":"designer"},index=["emp3"])
df=pd.concat([df,newrow])
print(df)
