from tabulate import tabulate
import pandas as pd
import os

print("欢迎使用辅助记忆工具!")
if "df.csv" in os.listdir("./"):
    df = pd.read_csv("./df.csv", index_col="Unnamed: 0")
else:
    df = pd.DataFrame({"question": [], "times": []})

import tkinter as tk
from tkinter import filedialog

# 实例化
root = tk.Tk()
root.withdraw()

# 获取文件夹路径
f_path = filedialog.askopenfilename()
print('\n获取的文件地址：', f_path)
