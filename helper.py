from tabulate import tabulate
import pandas as pd
import os


def helper():
    print("指令说明：")
    print("\th:\t帮助")
    print("\tq:\t保存退出")
    print("\t!q:\t不保存退出")
    print("\tsave:\t主动保存")
    print("\t+,_,_:\t加上排序与问题")
    print("\t-,_:\t根据排序删除问题")
    print("\tsort:\t按index排序")
    print("\ts,_:\t显示问题，后接正则表达式（可省略），与记忆次数")
    print("\tc:\t记忆库times清0")
    print("\tcc:\t删除记忆库")
    print("")
    print("\tm,_,_:\t开始记忆模式,使用正则表达式索引,和记忆掩码")
    print("\t\t按enter:\t下一条问题")
    print("\t\tqm:\t退出记忆模式")
    print("\t\tv:\t这个问题已经记住")

print("欢迎使用辅助记忆工具!")
if "df.csv" in os.listdir("./"):
    df = pd.read_csv("df.csv", index_col="Unnamed: 0")
else:
    df = pd.DataFrame({"question": [], "times": []})

def save(df=df):
    df.to_csv("df.csv")
    
# #  pd的输出设置
pd.set_option("display.max_colwidth",100)
pd.set_option('display.colheader_justify', 'left')

def left_align(df: pd.DataFrame):
    left_aligned_df = df.style.set_properties(**{'text-align': 'left'})
    left_aligned_df = left_aligned_df.set_table_styles(
        [dict(selector='th', props=[('text-align', 'left')])]
    )
    return left_aligned_df

while 1:
    print(">>>", end="")
    order = input()
    if order == "":
        continue
    if order == "h":
        helper()
    elif order == "q":
        save()
        print("保存成功，成功退出记忆工具！")
        break
    elif order == "!q":
        print("不保存，成功退出记忆工具！")
        break
    elif order == "save":
        save()
    elif order[0] == "+":
        (index, question) = tuple(order[2:].split(","))
        df.loc[index] = [question, 0]
    elif order[0] == "-":
        index = order[2:]
        df = df.drop(index)
    elif order == "sort":
        df = df.sort_index()
    elif order[0] == "s":
        regStr = ".*"
        if len(order) > 2 and order[1] == ',':
            regStr = order[2:]
        # make print left aglin
        flt = df.filter(regex=regStr, axis=0)
        print(tabulate(flt, headers = 'keys', tablefmt = 'psql'))
    elif order == "c":
        df.times = 0
    elif order == "cc":
        print()
        df = pd.DataFrame({"question": [], "times": []})
    elif order[0] == "m":
        print("进入记忆模式！")
        mask = 0
        regStr = ".*"
        if len(order) > 2:
            maskNreg = order[2:].split(',')
            if len(maskNreg) == 1:
                regStr = maskNreg[0] if maskNreg[0] != '' else ".*"
            elif len(maskNreg) == 2:
                regStr = maskNreg[0] if maskNreg[0] != '' else ".*"
                mask = eval(maskNreg[1]) if maskNreg[1] != '' else 0
            else:
                print("Error:m指令出错!")
                continue
        if len(df) == 0:
            print("Error:记忆库无内容！")
            continue
        while 1:
            flt = df[df.times <= mask].filter(regex=regStr,axis=0)
            if len(flt) == 0:
                print("Error:记忆库无满足条件的记忆内容！")
                break
            qs = flt.sample(n=1)
            print(f"?:\t{qs.question.iloc[0]}\t", end="")
            m_order = input()
            if m_order == "qm":
                print("退出记忆模式！")
                break
            elif m_order == "v":
                df.at[qs.index[0], "times"] += 1
            else:
                continue
