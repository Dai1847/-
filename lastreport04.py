# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 23:11:11 2019

@author: j17009
"""
import numpy as np
from matplotlib import pyplot 
class body:
    def __init__(self,h,w,a):
        self.weight = w
        self.height = h
        self.age = a
        
    def kisotaisya(self):
        s = input("性別を入力")
        if s == "男" or s == "M":
            k = (13.397*self.weight)+(4.799*self.height)-5.677*self.age+88.632
            print(k)
        elif s == "女" or s == "L":
            k = 9.247*self.weight+3.098*self.height-4.33*self.age+447.593
            print(k)
    
    def BMI(self):
        m = self.height/100
        b = self.weight/(m*m)
        print(int(b))
        
class meal(body):
    def BMI(self):
        m = self.height/100
        b = self.weight/(m*m)
        print("あなたのBMIは%dです"%b)
    
    def kisotaisya(self):
        s = input("性別を入力")
        if s == "男" or s == "M":
            k = (13.397*self.weight)+(4.799*self.height)-5.677*self.age+88.632
            return k
        elif s == "女" or s == "L":
            k = 9.247*self.weight+3.098*self.height-4.33*self.age+447.593
            return k

    def mokuhyo(self):
        j = self.kisotaisya()
        print("あなたの基礎代謝は%dです"%j)
        j1 = j * 1.5
        print("あなたの消費カロリーは%d calです"%j1)
        j2 = j1 - (7200/30)
        print("あなたが摂取できるカロリーは%d calです"%j2)
        p = self.weight*2    #摂取グラム数
        p1 = p * 4           #カロリー
        print("あなたがとるべきタンパク質量は%d gです"%p)
        f = self.weight*0.35
        f1 = f * 9
        print("あなたがとるべき脂質量は%d　gです"%f)
        c = j - p1 - f1
        c1 = c / 4
        print("あなたがとるべき糖質量は%d gです"%c1)
    
    def meal_list(self):
        j = self.kisotaisya()
        j1 = j * 1.5
        j2 = j1 - (7200/30)
        p = self.weight*2    #摂取グラム数
        p1 = p * 4           #カロリー
        f = self.weight*0.35
        f1 = f * 9
        c = j - p1 - f1
        c1 = c / 4
        return j2,p,f,c1
        
        
def plot_polar(labels, values, imgname):
    angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
    values = np.concatenate((values, [values[0]]))  # 閉じた多角形にする
    fig = pyplot.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, values, 'o-')  # 外枠
    ax.fill(angles, values, alpha=0.25)  # 塗りつぶし
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)  # 軸ラベル
    ax.set_rlim(0 ,140)     #割合
    pyplot.show(fig)
    pyplot.close(fig)

labels = ["Protein","Carorie","Carb","Fat"]
values = [0,0,0,0]  #一日の摂取量の初期値


m = meal(170,70,20)    #自分の体の情報を身長、体重、年齢の順番で入力
y = list(m.meal_list())

while True:             #摂取量を入力、表示
    values[0]= int(input("タンパク質摂取量を入力(g)"))
    values[1]= int(input("カロリー摂取量を入力(cal)"))
    values[2]= int(input("糖質摂取量を入力(g)"))
    values[3]= int(input("脂質摂取量を入力(g)"))
    #一日の摂取目標を割合で表示
    values[0]= (values[0]/y[1])*100
    values[1]= (values[1]/y[0])*100
    values[2]= (values[2]/y[3])*100
    values[3]= (values[3]/y[2])*100
    plot_polar(labels,values,"rabar.png")
    break
 
m.mokuhyo()
m.BMI()