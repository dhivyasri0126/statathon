import pandas as pd
#series
k = pd.Series([10,20,30,40])
k.name = "calories"
index = ['apple','banana','strawberry','orange']
k.index = index

print(k) #to print values and index 

s = pd.Series([10,20,30,40])
print(s) #to print 
print(s[0:2]) #to print from to whereand label based indexing
print(s.iloc[3]) #location based indexing
print(s.index) # to print index
print(s.values) #to print all values
