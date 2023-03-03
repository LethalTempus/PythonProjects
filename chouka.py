import tkinter as tk
import random


class chouka():

    
    def __init__(self) -> None:
        self.canvasSetup()
        self.widgetSetup()


    def canvasSetup(self):
        self.root = tk.Tk()
        self.root.geometry("700x700")
        self.root.title("zzl")
        self.root.resizable(0,0)
        self.coinnum = tk.IntVar()
        self.sixtrack = tk.IntVar()
        self.ran1list = tk.StringVar()
        self.ran2list = tk.StringVar()
        self.ran3list = tk.StringVar()
        self.ran4list = tk.StringVar()
        self.ran5list = tk.StringVar()
        self.ran6list = tk.StringVar()
        self.ran7list = tk.StringVar()
        self.ran8list = tk.StringVar()
        self.ran9list = tk.StringVar()
        self.ran10list = tk.StringVar()


    def widgetSetup(self):
        self.txt0 = tk.Label(self.root, text = "zzl币持有数量").pack()
        self.txttotal = tk.Label(self.root, textvariable = self.coinnum).pack()
        self.linetxt = tk.Label(self.root, text = "").pack()
        self.txt1 = tk.Label(self.root, text = "600zzl币").pack()
        self.danchou = tk.Button(self.root,command = lambda: self.xunfang(1))
        self.danchou.pack()
        self.danchou.config(text = "寻访一次")
        self.txt2 = tk.Label(self.root, text = "6000zzl币").pack()
        self.shilian = tk.Button(self.root,command = lambda: self.xunfang(10))
        self.shilian.pack()
        self.shilian.config(text = "寻访十次")
        self.tx14t = tk.Label(self.root, text = "").pack()
        self.tx0t = tk.Label(self.root, text = "已抽没出6星数:").pack()
        self.tx11t = tk.Label(self.root, textvariable = self.sixtrack).pack()
        self.tx12t = tk.Label(self.root, text = "").pack()
        self.tx13t = tk.Label(self.root, text = "以下为本次抽卡结果").pack()
        self.tx1t = tk.Label(self.root, textvariable = self.ran1list)
        self.tx2t = tk.Label(self.root, textvariable = self.ran2list)
        self.tx3t = tk.Label(self.root, textvariable = self.ran3list)
        self.tx4t = tk.Label(self.root, textvariable = self.ran4list)
        self.tx5t = tk.Label(self.root, textvariable = self.ran5list)
        self.tx6t = tk.Label(self.root, textvariable = self.ran6list)
        self.tx7t = tk.Label(self.root, textvariable = self.ran7list)
        self.tx8t = tk.Label(self.root, textvariable = self.ran8list)
        self.tx9t = tk.Label(self.root, textvariable = self.ran9list)
        self.tx10t = tk.Label(self.root, textvariable = self.ran10list)
        self.tx1t.pack()
        self.tx2t.pack()
        self.tx3t.pack()
        self.tx4t.pack()
        self.tx5t.pack()
        self.tx6t.pack()
        self.tx7t.pack()
        self.tx8t.pack()
        self.tx9t.pack()
        self.tx10t.pack()


    def xunfang(self,numin):
        self.coinnum.set(self.coinnum.get() - 600 * numin)
        ranlist = []
        ranlist1 = ["能天使","黑","安洁莉娜","银灰","莫斯提马","夜莺","星熊","陈","阿","煌","麦哲伦","赫拉格","斯卡蒂","塞雷娅","闪灵","艾雅法拉","伊芙利特","推进之王","刻俄柏","风笛","傀影","温蒂","早露","铃兰","棘刺","森蚺","史尔特尔","瑕光","泥岩","山","空弦","嗟峨","异客","凯尔希","卡涅利安","帕拉斯","水月","琴柳","远牙","焰尾","灵知","老鲤","澄闪","菲亚梅塔","号角","艾丽妮"]
        while numin != 0:
            self.sixtrack.set(self.sixtrack.get() + 1)
            A = random.randint(1,100)
            if self.six_star():
                B = random.choice(ranlist1)
                ranlist.append(B)
                self.sixtrack.set(0)
            elif A == 1 or A == 2:
                B = random.choice(ranlist1)
                ranlist.append(B)
                self.sixtrack.set(0)
            elif A <= 10:
                ranlist.append("5星")
            elif A <= 60:
                ranlist.append("4星")
            else:
                ranlist.append("3星")
            numin -= 1
        if len(ranlist) == 1:
            self.ran1list.set(ranlist[0])
            self.tx2t.pack_forget()
            self.tx3t.pack_forget()
            self.tx4t.pack_forget()
            self.tx5t.pack_forget()
            self.tx6t.pack_forget()
            self.tx7t.pack_forget()
            self.tx8t.pack_forget()
            self.tx9t.pack_forget()
            self.tx10t.pack_forget()
        if len(ranlist) == 10:
            self.ran1list.set(ranlist[0])
            self.ran2list.set(ranlist[1])
            self.ran3list.set(ranlist[2])
            self.ran4list.set(ranlist[3])
            self.ran5list.set(ranlist[4])
            self.ran6list.set(ranlist[5])
            self.ran7list.set(ranlist[6])
            self.ran8list.set(ranlist[7])
            self.ran9list.set(ranlist[8])
            self.ran10list.set(ranlist[9])
            self.tx1t.pack()
            self.tx2t.pack()
            self.tx3t.pack()
            self.tx4t.pack()
            self.tx5t.pack()
            self.tx6t.pack()
            self.tx7t.pack()
            self.tx8t.pack()
            self.tx9t.pack()
            self.tx10t.pack()
            

    def six_star(self):
        if self.sixtrack.get() > 50:
            self.prob = (2 + (self.sixtrack.get() - 50)*2)/100
            a_list = [True, False]
            distribution = [self.prob, 1 - self.prob]
            yes_no = random.choices(a_list, distribution)
            return yes_no[0]
             

UI = chouka()
UI.root.mainloop()
