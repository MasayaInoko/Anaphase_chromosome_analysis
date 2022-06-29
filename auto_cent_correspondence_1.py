import pandas as pd 
import numpy as np
import glob
import re
import os
import argparse

list = glob.glob("C:/Users/in0k0/Desktop/python/python勉強会/auto_cent_correspondence/*")
for file in list:
    file1 = pd.read_csv(file)
    file2 = pd.DataFrame(file1)
    name = os.path.splitext(os.path.basename(file))[0]
    #print(name)

    ##距離の計算結果のデータフレーム用
    test0 = pd.DataFrame()
    test1 = pd.DataFrame()
    test2 = pd.DataFrame()
    test3 = pd.DataFrame()
    test4 = pd.DataFrame()

    ##列checkに1が入っている行を選択
    check = file2[file2["check"]==1]
    ##列checkに1が入っている行をデータフレームとする
    checkFile = pd.DataFrame(check)
    #print(checkFile)
    #checkFile2 = checkFile.reset_index().set_index('Number')
    checkFile2 = checkFile.set_index('Number')
    ##ファイルとして出力
    #checkFile2.to_csv("C:/Users/in0k0/Desktop/python/python勉強会/auto_cent_correspondence_result/{}_result.csv".format(name),index=False,encoding = "utf_8_sig")

    ##Frameごとに繰り返し処理にする
    FrameNumber = np.arange(0,300)
    for n in FrameNumber:
        ##同じFrameのセットのみを取り出す
        FrameSet1 = checkFile[checkFile["Frame"]==n]
        FrameSet2 = checkFile[checkFile["Frame"]==n+1]
        #print(FrameSet2)

        m = 0

        ##もし指定したFrameNumberが存在しなければ次のFrameNumberへ
        if FrameSet2.empty:
            DropIndex1 = FrameSet1.index[FrameSet1["Frame"]==n+1].tolist()
            FrameSet1.drop(index=DropIndex1)
        elif FrameSet1.empty:
            DropIndex2 = FrameSet2.index[FrameSet2["Frame"]==n+1].tolist()
            FrameSet2.drop(index=DropIndex2)
        else:
            FrameSet1File = pd.DataFrame(FrameSet1)
            FrameSet2File = pd.DataFrame(FrameSet2)        
            df = pd.concat([FrameSet1File, FrameSet2File])

            ##距離を計算（中心体一つ目）
            Xvalue = df.iloc[4*(m+1), 2]
            Yvalue = df.iloc[4*(m+1), 3]
            Zvalue = df.iloc[4*(m+1), 6]
            Frame = df.iloc[4*(m+1), 7]
            index1 = df.index[(df["X"]==Xvalue) & (df["Y"]==Yvalue) & (df["Slice"]==Zvalue) & (df["Frame"]==Frame)].tolist()
            number1 = df.loc[index1, "Number"]
            test0 = np.append(test0,number1)

            diffx1 = df.iloc[4*(m+1), 2] - df.iloc[4*m, 2]  #見やすくするにはdf.iloc[4*(m+1), 2]をXvalueに書き換えるのがありか
            diffy1 = df.iloc[4*(m+1), 3] - df.iloc[4*m, 3]
            diffz1 = df.iloc[4*(m+1), 6] - df.iloc[4*m, 6]
            diffx2 = df.iloc[4*(m+1), 2] - df.iloc[4*m+1, 2]
            diffy2 = df.iloc[4*(m+1), 3] - df.iloc[4*m+1, 3]
            diffz2 = df.iloc[4*(m+1), 6] - df.iloc[4*m+1, 6]
            diffx3 = df.iloc[4*(m+1), 2] - df.iloc[4*m+2, 2]
            diffy3 = df.iloc[4*(m+1), 3] - df.iloc[4*m+2, 3]
            diffz3 = df.iloc[4*(m+1), 6] - df.iloc[4*m+2, 6]
            diffx4 = df.iloc[4*(m+1), 2] - df.iloc[4*m+3, 2]
            diffy4 = df.iloc[4*(m+1), 3] - df.iloc[4*m+3, 3]
            diffz4 = df.iloc[4*(m+1), 6] - df.iloc[4*m+3, 6]

            dis1 = (diffx1**2+diffy1**2+diffz1**2)**0.5
            test1 = np.append(test1,dis1)
            dis2 = (diffx2**2+diffy2**2+diffz2**2)**0.5
            test2 = np.append(test2,dis2)
            dis3 = (diffx3**2+diffy3**2+diffz3**2)**0.5
            test3 = np.append(test3,dis3)
            dis4 = (diffx4**2+diffy4**2+diffz4**2)**0.5
            test4 = np.append(test4,dis4)

            ##距離を計算（中心体二つ目~四つ目）
            Xvalue2 = df.iloc[4*(m+1)+1, 2]
            Yvalue2 = df.iloc[4*(m+1)+1, 3]
            Zvalue2 = df.iloc[4*(m+1)+1, 6]
            Frame2 = df.iloc[4*(m+1)+1, 7]
            index2 = df.index[(df["X"]==Xvalue2) & (df["Y"]==Yvalue2) & (df["Slice"]==Zvalue2) & (df["Frame"]==Frame2)].tolist()
            number2 = df.loc[index2, "Number"]
            test0 = np.append(test0,number2)

            dis1_2 = ((df.iloc[4*(m+1)+1,2]-df.iloc[4*m,2])**2+(df.iloc[4*(m+1)+1,3]-df.iloc[4*m,3])**2+(df.iloc[4*(m+1)+1,6]-df.iloc[4*m,6])**2)**0.5
            test1 = np.append(test1,dis1_2)
            dis2_2 = ((df.iloc[4*(m+1)+1,2]-df.iloc[4*m+1,2])**2+(df.iloc[4*(m+1)+1,3]-df.iloc[4*m+1,3])**2+(df.iloc[4*(m+1)+1,6]-df.iloc[4*m+1,6])**2)**0.5
            test2 = np.append(test2,dis2_2)
            dis3_2 = ((df.iloc[4*(m+1)+1,2]-df.iloc[4*m+2,2])**2+(df.iloc[4*(m+1)+1,3]-df.iloc[4*m+2,3])**2+(df.iloc[4*(m+1)+1,6]-df.iloc[4*m+2,6])**2)**0.5
            test3 = np.append(test3,dis3_2)
            dis4_2 = ((df.iloc[4*(m+1)+1,2]-df.iloc[4*m+3,2])**2+(df.iloc[4*(m+1)+1,3]-df.iloc[4*m+3,3])**2+(df.iloc[4*(m+1)+1,6]-df.iloc[4*m+3,6])**2)**0.5
            test4 = np.append(test4,dis4_2)

            Xvalue3 = df.iloc[4*(m+1)+2, 2]
            Yvalue3 = df.iloc[4*(m+1)+2, 3]
            Zvalue3 = df.iloc[4*(m+1)+2, 6]
            Frame3 = df.iloc[4*(m+1)+2, 7]
            index3 = df.index[(df["X"]==Xvalue3) & (df["Y"]==Yvalue3) & (df["Slice"]==Zvalue3) & (df["Frame"]==Frame3)].tolist()
            number3 = df.loc[index3, "Number"]
            test0 = np.append(test0,number3)

            dis1_3 = ((df.iloc[4*(m+1)+2,2]-df.iloc[4*m,2])**2+(df.iloc[4*(m+1)+2,3]-df.iloc[4*m,3])**2+(df.iloc[4*(m+1)+2,6]-df.iloc[4*m,6])**2)**0.5
            test1 = np.append(test1,dis1_3)
            dis2_3 = ((df.iloc[4*(m+1)+2,2]-df.iloc[4*m+1,2])**2+(df.iloc[4*(m+1)+2,3]-df.iloc[4*m+1,3])**2+(df.iloc[4*(m+1)+2,6]-df.iloc[4*m+1,6])**2)**0.5
            test2 = np.append(test2,dis2_3)
            dis3_3 = ((df.iloc[4*(m+1)+2,2]-df.iloc[4*m+2,2])**2+(df.iloc[4*(m+1)+2,3]-df.iloc[4*m+2,3])**2+(df.iloc[4*(m+1)+2,6]-df.iloc[4*m+2,6])**2)**0.5
            test3 = np.append(test3,dis3_3)
            dis4_3 = ((df.iloc[4*(m+1)+2,2]-df.iloc[4*m+3,2])**2+(df.iloc[4*(m+1)+2,3]-df.iloc[4*m+3,3])**2+(df.iloc[4*(m+1)+2,6]-df.iloc[4*m+3,6])**2)**0.5
            test4 = np.append(test4,dis4_3)

            Xvalue4 = df.iloc[4*(m+1)+3, 2]
            Yvalue4 = df.iloc[4*(m+1)+3, 3]
            Zvalue4 = df.iloc[4*(m+1)+3, 6]
            Frame4 = df.iloc[4*(m+1)+3, 7]
            index4 = df.index[(df["X"]==Xvalue4) & (df["Y"]==Yvalue4) & (df["Slice"]==Zvalue4) & (df["Frame"]==Frame4)].tolist()
            number4 = df.loc[index4, "Number"]
            test0 = np.append(test0,number4)

            dis1_4 = ((df.iloc[4*(m+1)+3,2]-df.iloc[4*m,2])**2+(df.iloc[4*(m+1)+3,3]-df.iloc[4*m,3])**2+(df.iloc[4*(m+1)+3,6]-df.iloc[4*m,6])**2)**0.5
            test1 = np.append(test1,dis1_4)
            dis2_4 = ((df.iloc[4*(m+1)+3,2]-df.iloc[4*m+1,2])**2+(df.iloc[4*(m+1)+3,3]-df.iloc[4*m+1,3])**2+(df.iloc[4*(m+1)+3,6]-df.iloc[4*m+1,6])**2)**0.5
            test2 = np.append(test2,dis2_4)
            dis3_4 = ((df.iloc[4*(m+1)+3,2]-df.iloc[4*m+2,2])**2+(df.iloc[4*(m+1)+3,3]-df.iloc[4*m+2,3])**2+(df.iloc[4*(m+1)+3,6]-df.iloc[4*m+2,6])**2)**0.5
            test3 = np.append(test3,dis3_4)
            dis4_4 = ((df.iloc[4*(m+1)+3,2]-df.iloc[4*m+3,2])**2+(df.iloc[4*(m+1)+3,3]-df.iloc[4*m+3,3])**2+(df.iloc[4*(m+1)+3,6]-df.iloc[4*m+3,6])**2)**0.5
            test4 = np.append(test4,dis4_4)

            m = m + 1

    ##距離計算結果ひとつのデータフレームに
    #print(test0)
    DisFile = pd.DataFrame({"Number":test0})
    #print(test1)
    DisFile["Dis4"] = test1
    DisFile["Dis3"] = test2
    DisFile["Dis2"] = test3
    DisFile["Dis1"] = test4

    ##各行でDistance4~1の中から最小値を計算、データフレームに追加
    min = DisFile[["Dis4","Dis3","Dis2","Dis1"]].min(axis=1)
    DisFile["min"] = min
    min_col = DisFile[["Dis4","Dis3","Dis2","Dis1"]].idxmin(axis=1)
    DisFile["min_col"] = min_col
    #print(DisFile)
    #DisFile2 = DisFile.reset_index().set_index('Number')
    DisFile2 = DisFile.set_index('Number')

    ##距離計算結果データフレームとcheckFileデータフレームを結合
    Result = pd.concat([checkFile2, DisFile2], axis=1) 

    #Test2File = pd.DataFrame(test2)
    Result.to_csv("C:/Users/in0k0/Desktop/python/python勉強会/auto_cent_correspondence_result/{}_result2.csv".format(name), index=False)
    #Test2File.to_csv("C:/Users/in0k0/Desktop/python/python勉強会/auto_cent_correspondence_result/test2.csv", index=False)