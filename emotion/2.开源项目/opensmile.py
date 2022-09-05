import os
import csv

path = './data/IEMOCAP/IEMOCAP_test.csv'
output_path = './data/IEMOCAP/IEMOCAP_test_IS09.arff'

data = []
with open(path) as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    header = next(csv_reader)        # 读取第一行每一列的标题
    pass
    for row in csv_reader:            # 将csv文件中的数据保存到data中
        data.append([row[0], row[1]])  # 选择某一列加入到data数组中
pass

for file_path, label in data:
    # cmd = f"SMILExtract "\
    #     + '-C "C:\Program Files\opensmile\config\is09-13\IS09_emotion.conf" '\
    #     + f"-I {file_path} "\
    #     + f"-instname {file_path} "\
    #     + f"-lldcsvoutput {output_path} "\
    #     + "-appendcsvlld 1 "\
    #     + "-timestampcsvlld 0 "\
    #     + "-headercsvlld 1 "

    # cmd = f"SMILExtract "\
    #     + '-C "C:\Program Files\opensmile\config\is09-13\IS09_emotion.conf" '\
    #     + f"-I {file_path} "\
    #     + f"-instname {label} "\
    #     + f"-csvoutput {output_path} "\
    #     + "-appendcsv 1 "\
    #     + "-timestampcsv 0 "\
    #     + "-headercsv 1 "

    # cmd = f"SMILExtract "\
    #     + '-C "C:\Program Files\opensmile\config\is09-13\IS09_emotion.conf" '\
    #     + f"-I {file_path} "\
    #     + f"-instname {file_path} "\
    #     + f"-output {output_path} "\
    #     + "-appendarff 0 "\
    #     + "-relation openSMILE_features "\
    #     + "-timestamparff 0 "\
    #     + "-classtype 'numeric' "\
    #     + f"-class {label} "

    cmd = f"SMILExtract "\
        + '-C "C:\Program Files\opensmile\config\is09-13\IS09_emotion.conf" '\
        + f"-I {file_path} "\
        + f"-instname {file_path} "\
        + f"-lldarffoutput {output_path} "\
        + "-appendarfflld 1 "\
        + "-relation openSMILE_features "\
        + "-timestamparfflld 0 "\
        + "-classtype 'numeric' "\
        + f"-class {label} "\
        + "-lldarfftargetsfile  C:\Program Files\opensmile\config\shared\arff_targets.conf.inc"

    # cmd = f"SMILExtract "\
    #     + '-C "C:\Program Files\opensmile\config\is09-13\IS09_emotion.conf" '\
    #     + f"-I {file_path} "\
    #     + f"-instname {label} "\
    #     + f"-lldhtkoutput {output_path} "\
    #     + "-appendhtklld 1 "

    # cmd = f"SMILExtract "\
    #     + '-C "C:\Program Files\opensmile\config\is09-13\IS09_emotion.conf" '\
    #     + f"-I {file_path} "\
    #     + f"-instname {label} "\
    #     + f"-htkoutput {output_path} "\
    #     + "-appendhtk 1 "\
    #     + "-classtype 'numeric' "\
    #     + "-class '5' "

    os.system(cmd)
    # break
