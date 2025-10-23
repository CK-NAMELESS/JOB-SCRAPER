import pandas as pd
import matplotlib.pyplot as plt
#创建文件
data={"Date":["2025-10-1","2025-10-2","2025-10-3","2025-10-4"],"Sales":[100,150,120,90],"Cost":[50,75,60,45]}
df=pd.DataFrame(data)
print(df)
df.to_csv("sales_data.csv",index=False)
df_read=pd.read_csv("sales_data.csv")
print(df_read)
#过滤数据
filtered_df=df[df_read["Sales"]>100]
print(filtered_df)
#排序
sorted_df=df.sort_values(["Sales"],ascending=False)
print(sorted_df)
#制图
plt.plot(df["Date"],df["Sales"],color="blue",marker="o")
plt.plot(df["Date"],df["Cost"],color="red",marker="o")
plt.title("Sales and Cost Data")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend(["Cost","Sales"])
plt.show()

