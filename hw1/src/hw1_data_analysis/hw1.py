# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("bicycle_data.csv")
print(df.head())

# %%
print(df.info())

# %%
df["Date"] = pd.to_datetime(df["Date"])
print(df.info())

# %%
df["Total East and West"] = (
    df["Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"] 
    + df["Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"]
)
df["Date_Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year
print(df.head())

# %%
df_2016 = df[df["Year"] == 2016].copy()
print(df_2016.head())

# %%
missing_count = df_2016.isnull().any(axis=1).sum()
print(missing_count)

# %%
hourly_counts = df_2016.groupby("Date_Hour")["Total East and West"].sum()
hourly_counts.plot()
plt.xlabel("Hour of the Day")
plt.ylabel("Total Bicycle Counts")
plt.show()
plt.savefig("counts_by_hour.png")

# %%determine what is (on average) the busiest hour of the day.
busiest_hour = df_2016.groupby("Date_Hour")["Total East and West"].mean()
print("Busiest hour of the day:", busiest_hour.idxmax())
