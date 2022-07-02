import pandas as pd
import os


def helper():
    print("指令说明：")
    print("\th:\t帮助")
    print("\tq:\t退出")
    print("\t+_+_:\t加上问题")
    print("\t-_:\t删除问题")
    print("\ts:\t显示所有问题，与记忆次数")
    print("\tc:\t记忆库times清0")
    print("\tcc:\t删除记忆库")
    print("")
    print("\tm_:\t开始记忆模式,后为记忆掩码")
    print("\t\t按enter:\t下一条问题")
    print("\t\tqm:\t退出记忆模式")
    print("\t\tv:\t这个问题已经记住")


print("欢迎使用辅助记忆工具!")
if "df.csv" in os.listdir("./"):
    df = pd.read_csv("df.csv", index_col="Unnamed: 0")
else:
    df = pd.DataFrame({"question": [], "times": []})
while 1:
    print(">>>", end="")
    order = input()
    if order == "":
        continue
    if order == "h":
        helper()
    elif order == "q":
        print("成功退出记忆工具！")
        df.to_csv("df.csv")
        break
    elif order[0] == "+":
        (index, question) = tuple(order[1:].split("+"))
        df.loc[index] = [question, 0]
    elif order[0] == "-":
        index = order[1:]
        df = df.drop(index)
    elif order == "s":
        print(df)
    elif order == "c":
        df.times = 0
    elif order == "cc":
        df = pd.DataFrame({"question": [], "times": []})
    elif order[0] == "m":
        print("进入记忆模式！")
        mask = 0
        if order == "m":
            mask = 0
        else:
            mask = eval(order[1:])
        if len(df) == 0:
            print("error:记忆库无内容！")
            continue
        while 1:
            if len(df[df["times"] <= mask]) == 0:
                print("error:记忆库无满足条件的记忆内容！")
                break
            qs = df.sample(n=1)
            if qs.times.iloc[0] > mask:
                continue
            print(f"?:\t{qs.question.iloc[0]}\t", end="")
            m_order = input()
            if m_order == "qm":
                print("退出记忆模式！")
                break
            elif m_order == "v":
                df.at[qs.index[0], "times"] += 1
            elif m_order == "x":
                continue
            else:
                continue
