# @Time     :  2018/12/26
# @Author   :  Kunming.Zhang
# @Function :  将热电偶温度导出，分析温度曲线
# @使用方式 ： python readtemlog.py 解析的文件名.csv  
# @注意     ： 解析文件与readtemlog.py要放在一个文件夹下
import re
import time
import csv
import os
import sys
from datetime import datetime
from matplotlib import pyplot as plt

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False   # 解决保存图像是负号'-'显示为方块的问题
    filename = sys.argv[1]
    with open(filename,'r')as file:
        reader = csv.reader(file)
        header_row = next(reader)
        dates,hights =[],[]
        for row in reader:
            dates.append(datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S"))
            hights.append(float(row[2]))
        fig=plt.figure(dpi=128,figsize=(10,6))
        #将列表hights传个plot()方法
        plt.plot(dates,hights,c='red')
        #设置图形的格式
        plt.title(filename+'的芯片表面温度',fontsize=24)
        plt.xlabel('时间',fontsize=16)
        #绘制斜线日期标签
        fig.autofmt_xdate()
        plt.ylabel('摄氏度℃',fontsize=16)
        plt.tick_params(axis='both',which='major',labelsize=13)
        plt.show()