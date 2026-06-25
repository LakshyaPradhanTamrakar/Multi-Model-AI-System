
import numpy as np
import pandas as pd

marks = pd.Series([85, 90, 78, 92, 88], name="Marks")
print(marks)
print("Mean marks:", marks.mean())

data = {
    "Name": ["Rahul", "Aman", "Sneha", "Vikram", "Riya"],
    "Age": [20, 22, 21, 23, 20],
    "Marks": [85, 90, 78, 92, 88],
    "City": ["Indore", "Bhopal", "Indore", "Pune", "Bhopal"],
}
df = pd.DataFrame(data)
print(df)

print(df.loc[0:2])
print(df.iloc[0:2, 0:2])
print(df["Name"])

print(df[df["Marks"] > 85])
print(df[df["City"] == "Indore"])

df["Grade"] = df["Marks"].apply(lambda x: "A" if x >= 85 else "B")
print(df)

print(df.groupby("City")["Marks"].mean())

df_with_nan = df.copy()
df_with_nan.loc[2, "Marks"] = np.nan
print(df_with_nan)
print(df_with_nan.isnull().sum())

df_filled = df_with_nan.copy()
df_filled["Marks"] = df_filled["Marks"].fillna(df_filled["Marks"].mean())
print(df_filled)
