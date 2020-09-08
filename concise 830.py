from tkinter import *
from datetime import date

interestVal="日利息(万分之)"

def store_interest(sel_in):
    global interestVal
    interestVal=sel_in
    
def Compute_fine():
    # 计算相差日期
    due_date1=list(map(int,due_date_1.get().split('-')))
    date1=list(map(int,date_1.get().split('-')))
    due_date1 = date(due_date1[0], due_date1[1], due_date1[2])
    date1 = date(date1[0], date1[1], date1[2])
    
    paid=float(money_1.get())
        
    diff1=date1-due_date1
    Delay.set("拖欠{}天".format(diff1.days))
    
    # 计算罚金
    if interestVal=="日利息(万分之)":
        day_rate=float(rate.get())/10000.0
    if interestVal=="年利息(百分之)":
        day_rate=float(rate.get())/100.0/365.0
    i1=(max(diff1.days,0))*(max(paid,0))*day_rate
    Interest_1.set("本次滞纳金{}元".format(round(i1,2)))
      

master = Tk()
master.title("滞纳金计算器")
Delay=StringVar();
Tail_Money=StringVar();
Interest_1 = StringVar();
Due_Money=StringVar();
var=StringVar()


Label(master, text="本次缴纳尾款(元)").grid(row=1, sticky=W)
Label(master, text="尾款应缴日期(例:2020-1-1)").grid(row=2, sticky=W)
Label(master, text="实际补足日期").grid(row=3, sticky=W)
Label(master, text="选择").grid(row=4, sticky=W)
Label(master, text="").grid(row=5, sticky=W)
d = Label(master, text="", fg="red",textvariable=Delay).grid(row=3, column=2, sticky=W)
f = Label(master, text="", fg="red",textvariable=Interest_1).grid(row=4, column=2, sticky=W)

dropDownList=["日利息(万分之)","年利息(百分之)"]
dropDown=OptionMenu(master,var,*dropDownList,command=store_interest)
var.set(dropDownList[0])
dropDown.grid(row=4,column=0,sticky=E)
#dropDown.config(background='#09A3BA')
#dropDown["menu"].config(background='#09A3BA')

# 创立变量
money_1=Entry(master)
due_date_1=Entry(master)
date_1=Entry(master)
rate=Entry(master)

# 变量输入
money_1.grid(row=1,column=1)
due_date_1.grid(row=2,column=1)
date_1.grid(row=3, column=1)
rate.grid(row=4, column=1)


b2 = Button(master, text="计算滞纳金", command=Compute_fine)
b2.grid(row=1, column=2, columnspan=2, rowspan=1, sticky=W + E + N + S, padx=5, pady=5)

mainloop()


