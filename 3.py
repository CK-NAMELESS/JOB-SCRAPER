import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("website_traffic_sep2025.csv")
print("原始数据检测前五行\n",df.head(6))

#检查缺失值
print("缺失情况：\n",df.isnull().sum())

#处理缺失值
df["unique_users"]=df["unique_users"].interpolate(methon='linear')
print("处理后unique_users缺失情况检查：\n",df.isnull().sum())
df["avg_session_duration"] = df["avg_session_duration"].fillna(df["avg_session_duration"].mean())
print("处理后avg_session_duration缺失情况检查：\n",df.isnull().sum())
"""df.fillna(method="ffill",inplace=True) 用前一天数据填补"""

#统计数据
total_visits=df["visits"].sum()
print("总人数",total_visits)
total_unique_users=df["unique_users"].sum()
print("总独立用户数",total_unique_users)
mean_avg_session_duration=df["avg_session_duration"].mean()
print("平均数",mean_avg_session_duration)

#制图
plt.figure(figsize=(10,5))
plt.plot(df["date"],df["visits"],marker="o")
plt.title("daily Visits Data")
plt.xlabel("Date")
plt.ylabel("visits")
plt.xticks(rotation=45)#避免标签重叠
plt.show()
