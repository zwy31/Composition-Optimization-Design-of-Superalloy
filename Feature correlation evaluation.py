import numpy as np
import matplotlib.pyplot as plt
import math
import xlrd
import xlsxwriter
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_excel(r'C:\Users\hp\PycharmProjects\pythonProject\data01.xls')
a=data.iloc[:, 0:11].corr()
#Drawing Details#
plt.subplots(figsize=(8, 8))
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
sns.heatmap(a, annot=True, vmax=1, square=True, cmap="RdBu", annot_kws={'size':13})
plt.show()
