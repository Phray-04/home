# -*- codeing = utf-8 -*-
# Time : 2021  |  environment : Windows10 X64
# Author : 云祈
# Software : PyCharm  |  Language : Python

from tkinter import *
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

# 主窗口
root_1 = Tk()
root_1.geometry('1000x550')
root_1.title('雨教务')
root_1.resizable(0, 0)

# --------------------------------------------------------------------------------------

# 框架1 :个人主页
frame1 = Frame(root_1, bd=1, width=200, height=150, relief='groove', cursor='plus')
frame1.place(x=0, y=0)  # cursor鼠标放在框架上的变化："circle""clock""cross""dotbox""exchange""fleur""heart""heart""man""mouse"
# 主页头像(图片）
photo = PhotoImage(file="guit1.png")  # file：t图片路径
imgLabel = Label(frame1, image=photo)  # 把图片整合到标签类中
imgLabel.place(x=20, y=30)  # 自动对齐
# 用户名
w1 = Label(frame1, text='燕云祈', font=('', 10), fg='black', padx='1', pady='1')
w1.place(x=90, y=40)  # 字体：underline下划线，overstrike删除线，slant（normal/italic）斜体，
# 学校
w2 = Label(frame1, text='湖北理工学院')
w2.place(x=90, y=65)  # justify对齐方式:LEFT/RIGHT

# 个人信息
w3 = Label(frame1, text='个人信息 >')  # 点击个人信息开始编辑页面
w3.place(x=60, y=100)  # justify对齐方式:LEFT/RIGHT

# ------------------------------------------------------------------------

# 框架2 :教务信息
frame2 = Frame(root_1, bd=1, width=200, height=400, relief='groove', cursor='cross')  # bd边框粗细
frame2.place(x=0, y=150)  # relief五种边框：ridge凸出，groove普通，raised淡边，sunken凹进

# 树状图
tree = ttk.Treeview(frame2)
tree.place(x=0, y=270)
# 添加一级树枝
treeF1 = tree.insert("", 0, "中国", text="中国CHA", values="F1")  # image/open/tags
treeF2 = tree.insert("", 1, "美国 ", text="美国USA", values="F2")
treeF4 = tree.insert("", 2, "英国", text="英国UK", values="F3")
# 二级树枝
treeF1_1 = tree.insert(treeF1, 0, "黑龙江", text="中国黑龙江", values="F1_1")
treeF1_2 = tree.insert(treeF1, 1, "吉林", text="中国吉林", values="F1_2")
treeF1_3 = tree.insert(treeF1, 2, "辽宁", text="中国辽宁", values="F1_3")
treeF2_1 = tree.insert(treeF2, 0, "重庆", text="中国重庆", values="F1_1")
treeF2_2 = tree.insert(treeF2, 1, "海南", text="中国海南", values="F1_2")
treeF2_3 = tree.insert(treeF2, 2, "广东", text="中国广东", values="F1_3")
# 三级树枝
treeF1_1_1 = tree.insert(treeF1_1, 0, "哈尔滨市", text="中国哈尔滨市")
treeF1_1_2 = tree.insert(treeF1_1, 1, "广州市", text="中国广州市")

# ------------------------------------------------------------------------

# 框架3 :学生数据
frame3 = Frame(root_1, bd=1, bg='linen', width=400, height=280, relief='groove')
frame3.place(x=200, y=0)

# 滚动条
scrollBar = Scrollbar(frame3)
# scrollBar.pack(side=RIGHT, fill=Y)
scrollBar.place(x=375, y=0)


# 数据可视化
def numpy1():
    root = Tk()
    root.title("在tkinter中使用matplotlib")
    fig = plt.figure(figsize=(8, 6))
    ax = fig.gca(projection='3d')

    X, Y, Z = axes3d.get_test_data(0.05)
    ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
    cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
    # 将绘制的图形显示到tkinter:创建属于root的canvas画布,并将图f置于画布上
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()  # 注意show方法已经过时了,这里改用draw
    canvas.get_tk_widget().pack(side=TOP,  # 上对齐
                                fill=BOTH,  # 填充方式
                                expand=YES)

    ax.set_xlabel('X')
    ax.set_xlim(-40, 40)
    ax.set_ylabel('Y')
    ax.set_ylim(-40, 40)
    ax.set_zlabel('Z')
    ax.set_zlim(-100, 100)
    plt.show()

    root.mainloop()

# 按钮
btn1 = Button(frame3, text='绩点可视化', command=numpy1)
btn1.place(x=310, y=230)

# 进度条
# 一个实时记录进度条的值
# def print_value(v):  # 传入值v
#     scale.config(label='你选择的程度是:' + v)
# scale添加label和command

scale = Scale(frame3, bd=0, from_="1", to="100", orient=HORIZONTAL, length=300,
              showvalue=1, resolution=0.1, bg='linen')
scale.set(62)  # 初始值
scale.place(x=0, y=220)

# 表格数据
tree1 = ttk.Treeview(frame3, yscrollcommand=scrollBar.set, show="headings")  # show改变表头样式
tree1.place(x=0, y=0)

tree1["columns"] = ("数字逻辑", "数据结构", "体重", "年龄", "性别")  # 定义1列
tree1.column("数字逻辑", width=74, anchor='center')
tree1.column("数据结构", width=74, anchor='center')
tree1.column("体重", width=74, anchor='center')
tree1.column("年龄", width=74, anchor='center')
tree1.column("性别", width=74, anchor='center')

tree1.heading("数字逻辑", text="程序设计")  # 表头
tree1.heading("数据结构", text="数据结构")
tree1.heading("体重", text="操作系统")
tree1.heading("年龄", text="组成原理")
tree1.heading("性别", text="计算机网络")

tree1.insert('', 0, values=("10", "223", "332", "24", "25"))  # 数据(待化简)
tree1.insert('', 1, values=("6", "7", "8", "9", "10"))
tree1.insert('', 2, values=("11", "12", "13", "14", "15"))
tree1.insert('', 3, values=("16", "17", "18", "19", "20"))
tree1.insert('', 4, values=("16", "17", "18", "19", "20"))
tree1.insert('', 5, values=("16", "17", "18", "19", "20"))
tree1.insert('', 6, values=("16", "17", "18", "19", "20"))
tree1.insert('', 7, values=("16", "17", "18", "19", "20"))
tree1.insert('', 8, values=("17", "17", "18", "19", "20"))
tree1.insert('', 9, values=("18", "17", "18", "19", "20"))
tree1.insert('', 10, values=("19", "17", "18", "19", "20"))
tree1.insert('', 11, values=("20", "17", "18", "19", "20"))

# ------------------------------------------------------------------------

# 框架4: 参数区
frame4 = Frame(root_1, bd=1, bg='aliceblue', width=800, height=270, relief='groove')
frame4.place(x=200, y=270)

# 状态栏
labelf4 = Label(frame4, text='UTF-8', bg='aliceblue')
labelf4.place(x=750, y=250)

# 画布
canvas = Canvas(frame4, height=200, width=800, bg='white')
# 图像
image_canvas1 = PhotoImage(file='canimg1.png')
imagecan = canvas.create_image(400, 0, anchor='nw', image=image_canvas1)  # x/y锚点,方位

# 画图
x0, y0, x1, y1 = 50, 60, 70, 80
lines1 = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')

canvas.place(x=0, y=0)

# ------------------------------------------------------------------------

# 框架5: 显示区
frame5 = Frame(root_1, bd=1, width=400, height=270, relief='groove')
frame5.place(x=600, y=0)

# 面板PaneWindow(上下左右)
pwf5 = PanedWindow(frame5, width=400, height=270, orient='vertical', sashrelief='raised')  # 分割线样式:sunken/flat/raised
pwf5.pack(fill='both', expand=1)
pw_1 = PanedWindow(pwf5, height=135, orient='vertical', sashrelief='sunken')
pw_1.pack(fill='both', expand=1)
pw_2 = PanedWindow(pwf5, width=400, orient='horizontal', sashrelief='sunken')
pwf5.add(pw_1), pwf5.add(pw_2)
# 校园资讯
w = Label(pwf5, text='校园资讯', font=('', 10), fg='black', padx='1', pady='1')
w.place(x=190, y=40)
# 个人动态
w2 = Label(pwf5, text='个人动态', font=('', 10), fg='black', padx='1', pady='1')
w2.place(x=190, y=230)
# ------------------------------------------------------------------------

# 菜单项

menuBar = Menu(root_1)

fmenu = Menu(menuBar, tearoff=0)
for each in ['新建', '打开', '保存', '另存为', '视图', '退出']:
    if each == "新建":
        fmenu.add_command(label="新建")
    elif each == "打开":
        fmenu.add_command(label="打开", command='')
    elif each == "保存":
        fmenu.add_command(label="保存")
    elif each == '另存为':
        fmenu.add_command(label="另存为")
    elif each == "视图":
        fmenu.add_command(label="视图")

fmenu.add_separator()
if each == "退出":
    fmenu.add_command(label="退出", command=root_1.quit)
# elif each == "退出":
#     fmenu.add_command(label="退出", command=root_1.quit)
vmenu = Menu(menuBar, tearoff=0)
# 为每个子菜单实例添加菜单项
for each in ['复制', '粘贴', '剪切']:
    vmenu.add_command(label=each)

sMenu = Menu(menuBar, tearoff=0)
for each in ["腾讯", "搜狐", "芒果", "爱奇艺", "优酷"]:
    if each == "腾讯":
        sMenu.add_command(label="腾讯", command=lambda: webbrowser.open('http://v.qq.com/'))
    elif each == '搜狐':
        sMenu.add_command(label='搜狐', command=lambda: webbrowser.open('http://tv.sohu.com/'))
    elif each == '爱奇艺':
        sMenu.add_command(label='爱奇艺', command=lambda: webbrowser.open('http://www.iqiyi.com/'))
    elif each == '芒果':
        sMenu.add_command(label='芒果', command=lambda: webbrowser.open('http://www.mgtv.com/'))
    elif each == '优酷':
        sMenu.add_command(label='优酷', command=lambda: webbrowser.open('http://www.youku.com/'))

emenu = Menu(menuBar, tearoff=0)
for each in ['默认视图', '新式视图']:
    emenu.add_command(label=each)

xMenu = Menu(menuBar, tearoff=0)
for each in ["C/C++", "Python", "JAVA"]:
    xMenu.add_radiobutton(label=each)  # add_radiobutton单选;add_checkbutton复选
xMenu.add_separator()
# 插入分割线
for each in ["HTML", "CSS", "JAVAScript", "IOS", "Android", "UI"]:
    xMenu.add_checkbutton(label=each, selectcolor='red')  # selectcolor设置选中区的颜色


# 弹出界面式工具
# URL网址二维码生成器
def QR():
    root2 = Tk()
    root2.overrideredirect(True)  # 去除掉界面边框
    root2.geometry('500x100+400+200')
    # 输入URL的文本框，绑定单击事件
    url1 = StringVar(root2, value='请输入URL')
    entryQR = Entry(root2, textvariable=url1)
    entryQR.place(x=10, y=10, width=480, height=20)

    # 清空内容
    def QRclear():
        url1.set('')

    # 转换成二维码并保存图片
    def generate():
        fn = file = 'guibg1.png'
        img = qrcode.make(url1.get())
        img.save(fn)
        startfile(fn)

    entryQR.bind('<Button-1>', QRclear)
    # 两个按钮
    buttonGenerate = Button(root2, text='生成二维码', command=generate)
    buttonGenerate.place(x=200, y=40, width=80, height=20)
    buttonGenerate = Button(root2, text='完成', command=root2.quit)  # bug：会把主界面一同关掉
    buttonGenerate.place(x=300, y=40, width=40, height=20)
    root2.mainloop()


# 技术支持
def Picture():
    root3 = Tk()
    root3.geometry('410x410')
    # photo3 = PhotoImage(file="guibg1.png")
    # imgLabelP = Label(root3, image=photo3)  # 把图片整合到标签类中
    # imgLabelP.place(x=0, y=0)  # 自动对齐
    root3.mainloop()


# 记事本模块
def text():
    Zc3 = Tk()
    Zc3.title('记事本')
    Zc3.geometry('400x300')
    Zc3.resizable(0, 0)
    t = Text(Zc3, width=400, height=300)
    t.place(x=0, y=0)


gMenu = Menu(menuBar, tearoff=0)
for each in ['记事本', '键盘', '二维码生成器', '论文检索']:
    if each == "记事本":
        gMenu.add_command(label='草稿本', command=text)  # bug：不能保存
    elif each == '键盘':
        gMenu.add_command(label='键盘', command='')
    elif each == '二维码生成器':
        gMenu.add_command(label='二维码生成器', command=QR)
    elif each == '论文检索':
        gMenu.add_command(label='论文检索', command='')  # 知网/万方 关键字和数据查询，下载文献

aMenu = Menu(menuBar, tearoff=0)
for each in ['版本信息', '联系我们', '技术支持', '满意度调查']:
    if each == '版本信息':
        aMenu.add_command(label='版本信息', command='')
    elif each == '联系我们':
        aMenu.add_command(label='联系我们', command='')
    elif each == '技术支持':
        aMenu.add_command(label='技术支持', command=Picture)
    elif each == '满意度调查':
        aMenu.add_command(label='满意度调查', command='')
# 顶级菜单项
menuBar.add_cascade(label='文件', menu=fmenu)
menuBar.add_cascade(label='视图', menu=vmenu)
menuBar.add_cascade(label='视频', menu=sMenu)
menuBar.add_cascade(label='选课', menu=xMenu)
menuBar.add_cascade(label='编辑', menu=emenu)
menuBar.add_cascade(label='工具', menu=gMenu)
menuBar.add_cascade(label='关于', menu=aMenu)

root_1['menu'] = menuBar

root_1.mainloop()
