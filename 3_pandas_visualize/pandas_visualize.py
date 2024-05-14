
import matplotlib.pyplot as plt
import pandas as pd
vehicles = pd.read_csv("vehicles.csv")
print("\nImported data sample:\n=====================")
print(vehicles.head().to_string())


vehicles.plot(kind='scatter',x='citympg',y='co2emissions').figure.show()

vehicles['co2emissions'].plot(kind='hist').figure.show()

vehicles.pivot(columns = 'drive', values = 'co2emissions')

vehicles.pivot(columns = 'drive', values = 'co2emissions').plot(kind='box', figsize=(10,6)).figure.show()


vehicles.groupby('year')['drive'].value_counts()


vehicles.groupby('year')['drive'].value_counts().unstack()


vehicles.groupby('year')['drive'].value_counts().unstack().plot(kind='bar',stacked=True,figsize=(10,6)).figure.show()


