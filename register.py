from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

root2 = Tk()  # 实例化
root2.title('雨教务')  # 软件名字
root2.geometry('400x500')  # 界面大小
root2.resizable(0, 0)  # 界面大小不可变


# 图片背景
frame1 = Frame(root2, width=400, height=500, cursor='cross')
frame1.place(x=0, y=0)


def get_image(filename, width, height):
    im = Image.open(filename).resize((width, height))
    return ImageTk.PhotoImage(im)


im_root = get_image('bgr.jpeg', 400, 500)
canvas_root = Canvas(frame1, width=400, height=500)
canvas_root.place(x=0, y=0)
canvas_root.create_image(0, 0, anchor=NW, image=im_root)  # 坐标x/y；画图的起始点NW西北方(N/S/W/E)；image装入

# 注册项标签：昵称，账号，密码，确认密码，身份证号，学号
# 试图化简： placez={1:'x=25,y=20';}
labelz0 = Label(root2, text=' 昵称：').place(x=25, y=20)
labelz1 = Label(root2, text='* 账号：').place(x=25, y=60)
labelz2 = Label(root2, text='* 密码：').place(x=25, y=100)
labelz3 = Label(root2, text='确认密码：').place(x=20, y=140)
labelz4 = Label(root2, text='身份证号：').place(x=20, y=180)
labelz5 = Label(root2, text=' 姓名：').place(x=25, y=220)
labelz6 = Label(root2, text=' 性别：').place(x=25, y=260)
labelz7 = Label(root2, text=' 籍贯：').place(x=25, y=300)

# 输入框
entryz0 = Entry(root2).place(x=90, y=20)
entryz1 = Entry(root2).place(x=90, y=60)
entryz2 = Entry(root2).place(x=90, y=100)
entryz3 = Entry(root2).place(x=90, y=140)
entryz4 = Entry(root2).place(x=90, y=180)
entryz5 = Entry(root2).place(x=90, y=220)
com1 = Combobox(root2).place(x=90, y=260)  # 设置下拉数据
com2 = Combobox(root2).place(x=90, y=300)
'''com1['value'] = ('男','女')
com2['value'] = ('河北省', '山西省', '内蒙古自治区', '广西壮族自治区', '西藏自治区',
                 '宁夏回族自治区', '新疆维吾尔自治区', '北京市',
                 '天津市', '上海市', '重庆市', '香港特别行政区',
                 '澳门特别行政区', '辽宁省', '吉林省', '黑龙江省', '江苏省',
                 '浙江省', '安徽省', '福建省', '江西省', '山东省',
                 '河南省', '湖北省', '湖南省', '广东省', '海南省', '四川省',
                 '贵州省', '云南省', '陕西省', '甘肃省', '青海省', '台湾省')
com2.current(0)'''

# 按钮（调用响应事件）
btnz1 = Button(root2, text='立即注册', command='')  # command表示被点击时调用的方法
btnz1.place(x=120, y=340)
# 窗口事件循环
root2.mainloop()
