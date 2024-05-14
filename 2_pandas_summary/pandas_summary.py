# Imports CSV data and demos how the data can be summarised.

import pandas as pd
washers = pd.read_csv("washers.csv")
print("\nWashers Info:\n=============")
washers.info()

print("\nDescribe Washers:\n=================")
print(washers.head().to_string())

print("\nDescribe Washers By BrandName:\n==============================")
print(washers[['BrandName']].describe().to_string())

print("\nDescribe Washers by Volume:\n===========================")
print(washers[['Volume']].describe().to_string())

print("\nCount Washers by BrandName:\n===========================")
print(washers['BrandName'].value_counts().to_string())

print("\nCount Washers % by BrandName:\n=============================")
print(washers['BrandName'].value_counts(normalize=True).to_string())

print("\nWashers Mean Volume:\n====================")
print(washers[['Volume']].mean().to_string())

print("\nWashers Mean Volume by BrandName:\n=================================")
print(washers.groupby('BrandName')[['Volume']].mean().to_string())

print("\nWashers Mean Volume by BrandName (sorted):\n==========================================")
print(washers.groupby('BrandName')[['Volume']].mean().sort_values(by='Volume').to_string())

print("\nWashers by BrandName aggregated by different Volume measures:\n=============================================================")
print(washers.groupby('BrandName')[['Volume']].agg(['mean','median','min','max']).to_string())
