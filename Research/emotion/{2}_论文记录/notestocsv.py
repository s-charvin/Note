import os
from turtle import pd
import pandas as pd


if __name__ == '__main__':
    dirpath = "./"

    files = [l for l in os.listdir(
        dirpath) if '.md' in l]
    filenames = [""]*len(files)
    highlight = [""]*len(files)
    recordHighlight = False
    abstract = [""]*len(files)
    recordAbstract = False
    for i, file in enumerate(files):
        if "}_.md" in file or "{999}_" in file or '}_@' in file:
            continue
        filenames[i] = file[:-3]
        with open(dirpath + file, encoding='utf-8') as f:
            content = f.readlines()
            for line in content:
                if "# 重点" in line:
                    recordHighlight = True
                    continue
                if recordHighlight and line != "\n":
                    if "# " not in line:
                        highlight[i] = highlight[i]+line.replace("- ", "—— ")
                    else:
                        recordHighlight = False
                if "# 摘要" in line:
                    recordAbstract = True
                    continue
                if recordAbstract and line != "\n":
                    if "# " not in line:
                        abstract[i] = abstract[i]+line
                    else:
                        recordAbstract = False

    dict = {"论文": filenames, '重点': highlight, '摘要': abstract}

    df = pd.DataFrame(dict)
    df.sort_values(by="论文")
    # 保存 dataframe
    df.to_csv('论文记录.csv', index=False, encoding='gb18030')
