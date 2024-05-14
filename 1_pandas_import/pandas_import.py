# Demo different ways to import data with the pandas package.

import pandas

members = ["Brazil", "Russia", "India", "China", "South Africa"]
brics1 = pandas.Series(members)
print("Pandas Series:\n==============")
print(brics1.to_string())

members = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
        "gdp": [2750, 1658, 3202, 15270, 370],
        "literacy":[.944, .997, .721, .964, .943],
        "expectancy": [76.8, 72.7, 68.8, 76.4, 63.6],
        "population": [210.87, 143.96, 1367.09, 1415.05, 57.4]}
brics2 = pandas.DataFrame(members)
print("\nPandas DataFrame:\n=================")
print(brics2.to_string())

members = [["Brazil", "Brasilia", 2750, 0.944, 76.8, 210.87],
                     ["Russia", "Moscow", 1658, 0.997, 72.7, 143.96],
                     ["India", "New Delhi", 3202, 0.721, 68.8, 1367.09],
                     ["China", "Beijing", 15270, 0.964, 76.4, 1415.05],
                     ["South Africa", "Pretoria", 370, 0.943, 63.6, 57.4]]
labels = ["country", "capital", "gdp", "literacy", "expectancy", "population"]
brics3 = pandas.DataFrame(members, columns=labels)
print("\nPandas DataFrame:\n=================")
print(brics3.to_string())

brics4 = pandas.read_csv("brics.csv")
print("\nPandas DataFrame from CSV:\n==========================")
print(brics4.to_string())

brics5 = pandas.read_excel("brics.xlsx")
print("\nPandas DataFrame from Excel:\n============================")
print(brics5.to_string())

brics6 = pandas.read_excel("brics.xlsx", sheet_name="Summits")
print("\nPandas DataFrame from specific Excel sheet:\n===========================================")
print(brics6.to_string())