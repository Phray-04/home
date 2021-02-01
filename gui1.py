from tkinter import *  # 用于图形用户界面
from tkinter.messagebox import *  # 用于消息框、对话框
import threading,time   # 用于多线程,倒计时关闭

# 注册界面
def Zc():
    root2 = Tk()  # 实例化
    root2.title('雨教务')  # 软件名字
    root2.geometry('350x350')  # 界面大小
    root2.resizable(0, 0)  # 界面大小不可变
    root.destroy()  # 销毁主界面
    # 注册项标签：昵称，账号，密码，确认密码，身份证号，学号
    labelz0 = Label(root2, text=' 昵称：')
    labelz1 = Label(root2, text='* 账号：')
    labelz2 = Label(root2, text='* 密码：')
    labelz3 = Label(root2, text='确认密码：')
    labelz4 = Label(root2, text='身份证号：')
    labelz5 = Label(root2, text=' 学号：')
    # place坐标布局模式
    labelz0.place(x=25, y=20)
    labelz1.place(x=25, y=60)
    labelz2.place(x=25, y=100)
    labelz3.place(x=20, y=140)
    labelz4.place(x=20, y=180)
    labelz5.place(x=25, y=220)
    # 输入框
    entryz0 = Entry(root2)
    entryz0.place(x=90, y=20)
    entryz1 = Entry(root2)
    entryz1.place(x=90, y=60)
    entryz2 = Entry(root2)
    entryz2.place(x=90, y=100)
    entryz3 = Entry(root2)
    entryz3.place(x=90, y=140)
    entryz4 = Entry(root2)
    entryz4.place(x=90, y=180)
    entryz5 = Entry(root2)
    entryz5.place(x=90, y=220)
    # 按钮（调用响应事件）
    btnz1 = Button(root2, text='立即注册', command='')  # command表示被点击时调用的方法
    btnz1.place(x=120, y=260)
    # 窗口事件循环
    root2.mainloop()


# 登录版块
def reg():
    myAccount = entry1.get()
    myPassword = entry2.get()
    e1_len = len(myAccount)
    e2_len = len(myPassword)

    if myAccount == '燕云祈' and myPassword == '000000':
        # 用户许可协议(10s)计时结束可以点击同意/退出按钮,同意后打开home主页
        root3 = Tk()
        root3.overrideredirect(True)  # 去除掉界面边框(不可手动关闭)
        root3.geometry('410x410')
        # 设置定时关闭页面
        lbTime = Label(root3, fg='black', anchor='w')  # 倒计时时间提示
        lbTime.place(x=200, y=380, width=180)
        lbTime2 = Label(root3,text='用户许可协议')
        lbTime2.place(x=180,y=20)

        def autoClose():  # 倒计时关闭方法(用户许可协议)
            for i in range(10):
                lbTime['text'] = '请选择是否同意用户许可协议{}秒'.format(10 - i)
                time.sleep(1)  # 当秒=1时关闭页面
            root3.destroy()

        # 创建并启动线程
        t = threading.Thread(target=autoClose)
        t.start()

        # 用户许可协议text
        label3=Label(root3,text='重要须知： 迅雷在此特别提醒用户认真本《软件许可协议》\n'
                                '--- 用户应认真阅读本《软件许可协 （下称《协议》）中各\n'
                                '条款，包括免除或者限制迅雷责任的免责及对用户的权利限制。\n'
                                '请您阅并接受或不接受本《协议》（未成应在法定监护人陪同下\n'
                                '"软件"许可使用及相关方的权利义务。户"或"您"是指通过迅雷提供\n'
                                '审阅）。非您接受本《协议》条款，否则权下载、安装或使用本\n'
                                '"软件"及其关服务您的安装使用行为将对本《协议》的接受，并\n'
                                '条款，包括免除或者限制迅雷责任的免责及对用户的权利限制。\n'
                                '同意接受本《协议各项条款的约束。本《》是用户与迅雷公司（下\n'
                                '请您阅并接受或不接受本《协议》（未成应在法定监护人陪同下\n'
                                '称"迅雷"）之间关用户下载、安装、使复制"迅雷客户端"软件, \n'
                                '（以下简称"软件"所订立的协议。本《》描述迅雷与用户之间关于\n'
                                '"软件"许可使用及相关方的权利义务。户"或"您"是指通过迅雷提供\n'
                                '的获取软件授权的途径获得软授权许可和软件产品的个人或单一实体。',bd=4,fg='red',bg='white')
        label3.place(x=10,y=50)

        root3.mainloop()

    elif myAccount == '燕云祈' and myPassword != '000000':
        showinfo(title='注意', message='密码错误')  # messagebox:showinfo/showerror
        entry2.delete(0, e1_len)
    else:
        showwarning(title='注意', message='用户名错误')  # messagebox:askquestion/askyesno/askokcancel/asktrycancel
        entry1.delete(0, e1_len)
        entry2.delete(0, e2_len)


# 主登录界面
root = Tk()
root.geometry('400x350')
root.title('雨教务')
root.resizable(0, 0)

# 登录界面图片
photo = PhotoImage(file='guibg2.png')
theLabel = Label(root, image=photo, compound=CENTER)
theLabel.place(x=0, y=0)
# 定义登录界面
label1 = Label(root, text='用户名:')
label1.place(x=100, y=215)
label2 = Label(root, text='密码:')
label2.place(x=102, y=245)
entry1 = Entry(root)
entry1.place(x=150, y=215)
entry2 = Entry(root)
entry2['show'] = '*'
entry2.place(x=150, y=245)
btn1 = Button(root, text='登录', command=reg)
btn1.place(x=150, y=285)
btn2 = Button(root, text='注册', command=Zc)
btn2.place(x=200, y=285)
btn3 = Button(root, text='退出', command=root.quit)
btn3.place(x=250, y=285)

# 登录身份选择（单选框）
r1 = Checkbutton(root, text='学生')
r2 = Checkbutton(root, text='教师')
r3 = Checkbutton(root, text='游客')
r1.place(x=180, y=320)
r2.place(x=240, y=320)
r3.place(x=120, y=320)

root.mainloop()  # 窗口循环接收下一个事件；继承于Misc类;写在最后！

# 完成此项目至少需要：GUI tkinter、MYSQL数据库、网络编程

# MYSQL数据库、Python操作数据库、爬虫、GUI Tkinter
# tk和ttk/类和对象/基于控件的界面切换/VIP视频播放器（爬虫）/网络编程（聊天室计划）/平台可移植性

''' 
tkinter终归只是一个界面工具，
要实现和其他功能（包括爬虫、正则表达式...）等等的按钮事件绑定
本程序基于篇 Python Tkinter 包实现对GUI的功能练习，实现一个学生管理系统。功能涵盖：（下拉）菜单选项内容，按钮执行任务，登录操作(界面切换），图片背景，插入图片
# tkinter 是对Python包的练习可视化工具，先实践后理论

    检索数据库：进行匹配，匹配成功则登陆成功，本界面关闭，开启个人主页；否则显示登录失败；
    注册：开启注册界面，将信息录入数据库，进入个人主页
     TKinter的核心组件(按钮）共21个：
 Toplevel 新顶层窗口、Label 标签、Button 按钮、 Canvas 画布、Checkbutton 复选、
 Entry 输入框、 Frame 框架、LabelFrame 边框容器、 Listbox 列表框、Menu 菜单、
 Menubutton 菜单项、Message 显示多行文本（消息控件）、OptionMenu 可选菜单、 PaneWindow 、
  Radiobutton 单选、 Scale 输入限定范围的数字区间、Scrollbar 滚动条、
  Spinbox 指定输入范围（的输入框）、
  Text 文本、Bitmap、 Image 图像
  使用时第一个参数都是父窗口,后面跟着组件的属性
  
  # 先看大致刷一遍tkinter的基础知识，再具体实现小功能，再以帮助文档为辅助开发本大型程序，有不会的去百度，做软件之前，先把软件目标架构图画出来，再逐一实现功能
'''

''' 组件排列方式:pack()自动包装；grid()网格化布局；place坐标位置布局
常用grid布局：
row行，column列（编号从0开始）
sticky参数用N/S/W/E表示上下左右（决定该组件的开始方向）
# rowspan跨越的行数，columnspan跨越的列数；ipadx/ipady边距
# 一段程序只能用同一种布局方式

# 按钮绑定方式：command属性声明(不加任何标点符号）/bind方法
'''

# <Button-1> 表示⿏标左键单击，其中的 1 换成 3 表示右 键被单击
'''bind.class绑定类别；
例：w.bind_class(“Entry”, “<Control-V>”, my_paste)
类名 + 事件类型 + 相应操作 ——Ctrl+V 表示粘贴
# unbind解除绑定
'''
# <KeyPress-A> 表示 A 键被按下，其中的 A 可以换成其他 的键位。
# 单选/复选按钮、文本域、Canvas画布、Toplevel新顶层窗口
# 其他标准对话框：simpledialog(简单对 话框)，commondialog(⼀般 对话框)，filedialog(⽂件对话框)
