import pandas as pd
import numpy as np

df = pd.read_csv("device_log.csv", na_values=["", "np.nan"])
print("原始数据:\n", df)

df["Voltage"] = df["Voltage"].mask(df["Voltage"] > df["Voltage"].quantile(0.9), df["Voltage"][df["Voltage"] <= 10].mean())
df["Voltage"] = df["Voltage"].fillna(df["Voltage"].mean())

mean_voltage = df["Voltage"].mean()
max_voltage = df["Voltage"].max()
print("处理后数据:\n", df)
print("均值:", mean_voltage, "最大值:", max_voltage)

grouped_mean = df.groupby("Device")["Voltage"].mean()
print("按设备均值:\n", grouped_mean)

