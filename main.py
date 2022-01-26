import pandas as pd 
import csv


df = pd.read_csv("final2.csv")
print(df.shape)#for getting the number of rows and columns

del df["distance"]
del df["mass"]
del df["star_name"]
del df["radius"]
del df["luminosity"]
print(df.shape)

df = df.rename({
    "Unnamed":"temporary", 
    "Unnamed: 0":"index"
},axis = "columns")

print(list(df))
df.to_csv("main.csv")
