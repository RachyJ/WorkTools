import pandas as pd
import matplotlib.pyplot as plt # 做图表的包
import numpy as np

data = pd.read_csv("D:\Downloads\Download (26).csv")
count = len(data)
count_us = len(data[data['Country']=='United States'])
rate_us = count_us/count
group_country = data.groupby(data['Country', sort="True")
group_product = data.groupby(data['Product'])
group_dwncount = data.groupby(data['History Download Count'])
group_bizEmail = data.groupby(data['Is Company Email'])
print(count)
print(group_country.size())
print(group_product.size())
print(group_dwncount.size())
print(group_bizEmail.size())