import pandas as pd 
import numpy as np
import glob
import re
import os
import argparse

list = glob.glob("C:/Users/in0k0/Desktop/python/python勉強会/auto_cent_correspondence_result/*")
for file in list:
    file1 = pd.read_csv(file)
    file2 = pd.DataFrame(file1)
    name = os.path.splitext(os.path.basename(file))[0]

    TimeNumber = np.arange(0,300)
    for n in TimeNumber:

        ##中心体を対応付けて並べ替え
        #メモ　中心体４つそれぞれデータフレームを用意して格納していき、最後に合わせる？？
        centrosome1 = pd.DataFrame()
        centrosome2 = pd.DataFrame()
        centrosome3 = pd.DataFrame()
        centrosome4 = pd.DataFrame()

        ##最初のFrameの中心体を上から順にcentrosome1~4へ格納
        FirstCent1 = file2[0:1]
        centrosome1 = centrosome1.append(FirstCent1)
        FirstCent2 = file2[1:2]
        centrosome2 = centrosome2.append(FirstCent2)
        FirstCent3 = file2[2:3]
        centrosome3 = centrosome3.append(FirstCent3)
        FirstCent4 = file2[3:4]
        centrosome4 = centrosome4.append(FirstCent4)

        ##min_colを参照して座標を各中心体データフレームへ割り振る
        #まずは繰り返しなしで記述する
        #メモ nを用いて繰り返しにする

        Frame2Cent1 = file2[4:5]
        Frame2Cent1_min = file2.iloc[4,13]
        if Frame2Cent1_min == 'Dis4':
            centrosome1 = centrosome1.append(Frame2Cent1)
            cent1 = centrosome1.copy() 
        elif Frame2Cent1_min == 'Dis3':
            centrosome2 = centrosome2.append(Frame2Cent1)
            cent1 = centrosome2.copy()
        elif Frame2Cent1_min == 'Dis2':
            centrosome3 = centrosome3.append(Frame2Cent1)
            cent1 = centrosome3.copy()
        elif Frame2Cent1_min == 'Dis1':
            centrosome4 = centrosome4.append(Frame2Cent1)
            cent1 = centrosome4.copy()

        Frame2Cent2 = file2[5:6]
        Frame2Cent2_min = file2.iloc[5,13]
        if Frame2Cent2_min == 'Dis4':
            centrosome1 = centrosome1.append(Frame2Cent2)
            cent2 = centrosome1.copy()
        elif Frame2Cent2_min == 'Dis3':
            centrosome2 = centrosome2.append(Frame2Cent2)
            cent2 = centrosome2.copy()
        elif Frame2Cent2_min == 'Dis2':
            centrosome3 = centrosome3.append(Frame2Cent2)
            cent2 = centrosome3.copy()
        elif Frame2Cent2_min == 'Dis1':
            centrosome4 = centrosome4.append(Frame2Cent2)
            cent2 = centrosome4.copy()

        Frame2Cent3 = file2[6:7]
        Frame2Cent3_min = file2.iloc[6,13]
        if Frame2Cent3_min == 'Dis4':
            centrosome1 = centrosome1.append(Frame2Cent3)
            cent3 = centrosome1.copy()
        elif Frame2Cent3_min == 'Dis3':
            centrosome2 = centrosome2.append(Frame2Cent3)
            cent3 = centrosome2.copy()
        elif Frame2Cent3_min == 'Dis2':
            centrosome3 = centrosome3.append(Frame2Cent3)
            cent3 = centrosome3.copy()
        elif Frame2Cent3_min == 'Dis1':
            centrosome4 = centrosome4.append(Frame2Cent3)
            cent3 = centrosome4.copy()

        Frame2Cent4 = file2[7:8]
        Frame2Cent4_min = file2.iloc[7,13]
        if Frame2Cent4_min == 'Dis4':
            centrosome1 = centrosome1.append(Frame2Cent4)
            cent4 = centrosome1.copy()
        elif Frame2Cent4_min == 'Dis3':
            centrosome2 = centrosome2.append(Frame2Cent4)
            cent4 = centrosome2.copy()
        elif Frame2Cent4_min == 'Dis2':
            centrosome3 = centrosome3.append(Frame2Cent4)
            cent4 = centrosome3.copy()
        elif Frame2Cent4_min == 'Dis1':
            centrosome4 = centrosome4.append(Frame2Cent4)
            cent4 = centrosome4.copy()
        
        ##Frame3
        Frame3Cent1 = file2[8:9]
        Frame3Cent1_min = file2.iloc[8,13]
        if Frame3Cent1_min == 'Dis4':
            cent1 = cent1.append(Frame3Cent1)
            print(cent1)
            cent1 = centrosome1.copy()
        elif Frame3Cent1_min == 'Dis3':
            cent2 = cent2.append(Frame3Cent1)
            print(cent2)
            cent1 = centrosome2.copy()
        elif Frame3Cent1_min == 'Dis2':
            cent3 = cent3.append(Frame3Cent1)
            print(cent3)
            cent1 = centrosome3.copy()
        elif Frame3Cent1_min == 'Dis1':
            cent4 = cent4.append(Frame3Cent1)
            print(cent4)
            cent1 = centrosome4.copy()
        
        #print(cent4)
        #print(cent3)
        #print(cent2)
        #print(cent1)