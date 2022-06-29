
import cv2
import tkinter
import pygame
import pygame as py
from playsound import playsound
from tkinter import *



def saveimg():
    pass

#第1个窗体：登录窗体
def form1():
    def photo():
        img_path = "python detect.py --source " + en1.get()
        os.system(img_path)


    def video():
        os.system("python detect.py --source 0")


    def photoinput():
        pass


    def data():
        form2()



    #第一个窗口：图像识别系统
    root1 = Tk()
    root1.title('欢迎来到第七组的图像识别系统')
    root1.geometry('360x550+800+300')

    #窗口不可调节
    root1.resizable(0, 0)

    #填充背景
    login_frame1 = Frame(
        root1,
        width = 600,
        height = 550,
        background='#6495ED'
    )

    login_frame1.place(x=0, y=0)

    #添加装饰图片
    photo1 = PhotoImage(file="E:\python\pyProject\pika.gif"),
    label1 = Label(root1, image=photo1)
    label1.pack()

    #提示标签
    la0 = Label(
        root1,
        font=("微软雅黑",15,"bold"),
        foreground='#FFFFFF',
        background='#6495ED',
        text='您好，请输入照片路径'
    )

    la0.pack()

    #接收用户输入的图片路径
    en1 = Entry(
        root1,
        foreground = '#6495ED',
        background='#FFFFFF',
        #可以将Entry中的文本复制到剪贴板
        exportselection = True,
        #输入光标的颜色
        insertbackground = '#6495ED',
        #文本被选中的背景颜色
        selectbackground = '#6495ED',
        #文本被选中时的颜色
        selectforeground = '#FFFFFF',
        #Entry边框宽度
        bd = 2,
    )

    en1.pack()

    #按钮组件
    butphoto = Button(
        root1,
        font=("微软雅黑",15,"bold"),
        foreground='#6495ED',
        background='#FFFFFF',
        # 鼠标放上去时字体的颜色
        activeforeground='#CD5C5C',
        #鼠标放上去时按钮的背景颜色
        activebackground = '#FFFFFF',
        text="照片识别 ",
        command=photo
    )

    butphoto.pack(pady=5)

    butvideo = Button(
        root1,
        font=("微软雅黑",15,"bold"),
        foreground='#6495ED',
        background='#FFFFFF',
        # 鼠标放上去时字体的颜色
        activeforeground='#CD5C5C',
        # 鼠标放上去时按钮的背景颜色
        activebackground='#FFFFFF',
        text="视频识别",
        command=video
    )

    butvideo.pack(pady=5)

    butinput = Button(
        root1,
        font=("微软雅黑",15,"bold"),
        foreground='#6495ED',
        background='#FFFFFF',
        # 鼠标放上去时字体的颜色
        activeforeground='#CD5C5C',
        # 鼠标放上去时按钮的背景颜色
        activebackground='#FFFFFF',
        text="录入数据",
        command=data
    )

    butinput.pack(pady=5)

    #关闭登录窗体
    butquit = Button(
        root1,
        font=("微软雅黑",15,"bold"),
        foreground='#6495ED',
        background='#FFFFFF',
        #鼠标放上去时字体的颜色
        activeforeground = '#CD5C5C',
        #鼠标放上去时按钮的背景颜色
        activebackground='#FFFFFF',
        text=" 退 出 ",
        command=root1.destroy
    )

    butquit.pack(pady=5)

    # 第一个窗口bgm功能实现

    #播放音乐
    def play():
        # 初始化
        py.mixer.init()
        # 文件加载
        py.mixer.music.load(r'E:\python\pyProject\开源作业\月鹿同学 _ 茶夜 - 「口风琴」いつも何度でも／亲爱的旅人啊.mp3')
        # 播放  第一个是播放值 -1代表循环播放， 第二个参数代表开始播放的时间
        py.mixer.music.play(-1, 10)

    #打开窗口自动播放
    play()


    # 暂停
    def pause():
        pygame.mixer.music.pause()


    #调节音量条
    def printScale(text):
        t = int(text)
        pygame.mixer.music.set_volume(t / 100)


    # 暂停、播放按钮
    Button(
        root1,
        text="⏸",
        command=pause,
        width=5,
        foreground='#6495ED',
        bg='#FFFFFF'
    ).place(x=315, y=10)

    Button(
        root1,
        text="▶",
        #command=play,
        width=5,
        command=play,
        foreground='#6495ED',
        bg='#FFFFFF'
    ).place(x=255, y=10)


    # 音量调节条
    w1 = Scale(
        root1,
        from_=0,
        to=100,
        orient="horizontal",
        length=97,
        #variable=v,
        command=printScale,
        foreground='#6495ED',
        background='#FFFFFF',
        label="BGM音量"
    )

    w1.place(x=255, y=43)

    #一直在等待接受窗体1事件,不会进入第2个窗体
    root1.mainloop()


#第3个窗体：识别窗口
def form2():

    def videoinput():

        while (True):
            screen = np.array(ImageGrab.grab(bbox=(560, 240, 1360, 879)))
            cap = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            face_cascade = cv2.CascadeClassifier('F:/haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(cap, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(cap, (x, y), (x + w, y + h), (255, 0, 0), 2)
                print((x + w / 2) / 800, (y + h / 2) / 600, w / 800, h / 600)

            cv2.imshow('window', cap)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

    def camerainput():

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  # 人脸

        #3打开摄像头
        capture = cv2.VideoCapture(0)

        while True:

            #读取该帧的画面
            ret, img = capture.read()
            # 6灰度处理
            gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

            #7检查人脸
            faces = face_cascade.detectMultiScale(gray, 1.1, 3, 0, (120, 120))

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 3)
                print((x + w / 2) / 800, (y + h / 2) / 600, w / 800, h / 600)
                face_area = img[y:y + h, x:x + w]

                #用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表

            #9显示图片
            cv2.imshow("My_按q退出", img)


            #10暂停窗口
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

        #11释放资源
        capture.release()

        #12销毁窗口
        cv2.destoryAllWindows()

    def photoinput():
        pass

    #第2个窗体：主窗口
    root2 = Tk()
    root2.title('主窗口')
    root2.geometry('300x350+800+300')
    root2.maxsize(600, 700)

    #背景填充
    login_frame2 = Frame(root2, width=300, height=350, background='#6495ED')
    login_frame2.place(x=0, y=0)

    #按钮组件
    butphoto = Button(
        root2,
        font=("微软雅黑",10,"bold"),
        foreground='#6495ED',
        # 鼠标放上去时字体的颜色
        activeforeground='#CD5C5C',
        pady = 20,
        text="照片录入 ",
        command=photoinput
    )

    butphoto.pack(pady=20)

    butvideo = Button(
        root2,
        font=("微软雅黑",10,"bold"),
        foreground='#6495ED',
        # 鼠标放上去时字体的颜色
        activeforeground='#CD5C5C',
        pady = 20,
        text="视频录入",
        command=videoinput
    )

    butvideo.pack(pady=20)

    butcapture = Button(
        root2,
        font=("微软雅黑",10,"bold"),
        foreground='#6495ED',
        # 鼠标放上去时字体的颜色
        activeforeground='#CD5C5C',
        pady = 20,
        text="摄像录入",
        command=camerainput
    )

    butcapture.pack(pady=20)

    root2.mainloop()

#先进入第一个窗口：登录窗口
form1()
