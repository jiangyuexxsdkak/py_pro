#!/usr/bin/env python
# -*- coding:utf-8 -*-
#####目标：有700+个文件，每个文件有超过10000+的数据，数据分4列，取每个文件中最后一列的最大值,并将排名前6的文件取出来

import os
import pandas
import shutil #拷贝文件


#读取txt文件
# f_a = pandas.read_table(r"D:\example_data\2017.07.18.09.36.46.txt",encoding="gbk")#注意编码问题

#剔除开头8行，尾部2行
# f_a = pandas.read_table(r"D:\example_data\2017.07.18.09.36.46.txt",encoding="gbk",skiprows=8,skipfooter = 2,engine="python")

#使用分隔符区分列 报错
#f_a = pandas.read_table(r"D:\example_data\2017.07.18.09.36.46.txt",encoding="gbk",skiprows=8,skipfooter = 2,engine="python",sep="\s+")

#指定列名称
# f_a = pandas.read_table(r"D:\example_data\2017.07.18.09.36.46.txt",encoding="gbk",skiprows=8,skipfooter = 2,engine="python",
#                         sep="\s+",names = ["col1","col2","col3","col4"],decimal=".")

#缺省值处理(用0替换NAN)
# f_a = f_a.fillna(0)
# print(type(f_a))

#DataFrame 表格，取第四列最大值
# max_num = f_a["col4"].max()
# print(max_num)


def get_all_txt(dir_name):
    """
    获取文件夹（目录）下所有的txt文件名称
    :param dir_name:文件夹（目录）
    :return:
    """

    txt_files = []
    # 判断路径是否为文件夹（目录）
    if not os.path.isdir(dir_name):
        return txt_files
    #遍历文件夹（目录），并追加txt文件到列表中
    for i in os.listdir(dir_name): #遍历指定的文件夹包含的文件或文件夹的名字
        if not os.path.isdir(i):
            if i[-4:] == '.txt':
                txt_files.append(i) #列出所有txt文件的名称
    return txt_files


def get_data_max_colname(file_name,col_name):
    """
    获取file_name表格文件中列名称为col_name的列最大值
    :param filename:文件名称
    :param col_name:列名称
    :return:
    """
    #pandas读取数据
    f_a = pandas.read_table(file_name,encoding="gbk",skiprows=8,skipfooter=2,engine="python",
                            sep="\s+",names=["col1","col2","col3","col4"],decimal=".")
    # 缺省值处理(用0替换NAN)
    f_a = f_a.fillna(0)
    # DataFrame 表格，取指定列的最大值
    max_num = f_a[col_name].max()
    return max_num



def copy_files_2_dir(src_dir_name,src_files,tgt_dir_name):
    """
    移动特定文件到文件夹
    :param src_dir_name: 源文件夹名称
    :param src_files:源文件名称
    :param tgt_dir_name:目标文件夹
    :return:
    """
    os.makedirs(tgt_dir_name,exist_ok=False)#创建目标文件夹
    for i in src_files:
        file_src = os.path.join(src_dir_name,i)
        shutil.copyfile(file_src,os.path.join(tgt_dir_name,i))



if __name__ == "__main__":
    max_nums = []
    file_name_list = []

    #获取所有的文件名称
    txt_files = get_all_txt(r'D:\example_data')
    for i in txt_files:
        #给每个文件加路径前缀
        file_path = os.path.join('D:\example_data',i)
        #计算所有文件中第4列的最大值
        max_file_col = get_data_max_colname(file_path,"col4")
        #最大值计入最大值列表
        max_nums.append(max_file_col)
        #文件名称计入文件名列表
        file_name_list.append(i)
    #最大值传入序列并匹配行（匹配索引）
    sr = pandas.Series(data=max_nums,index=file_name_list)
    #按值进行降序排列
    sorted_max_nums = sr.sort_values(ascending=False)

    #取前6行数据（最大的6个数据）和对应的文件名称
    top6_data = sorted_max_nums.head(6)
    print(top6_data)
    top6_filename = list(top6_data.index)
    print(to   p6_filename)
    #拷贝文件
    copy_files_2_dir(r'D:\example_data',top6_filename,r'D:\example_data\tgt_name')
















