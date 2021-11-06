import pandas as pd
CA_df = pd.read_csv("CAimpatient.csv", header= 0, nrows=25, na_values=["Invalid" , "n.a."])
print(CA_df)

NY_df = pd.read_csv("NYimpatient.csv", header= 0, na_values=["Invalid" , "n.a."])
print(NY_df)
print("-------------------------------------")
print(NY_df.groupby(["Hospital County"]).count())
print(CA_df.groupby(["Discharges"]).sum())



#print(df.aggregate(['patcnty1']))