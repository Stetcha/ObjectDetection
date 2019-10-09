#!/usr/bin/python

from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import cv2

from tkinter import IntVar
import page


class mainframe():

    def __init__(self):
        self.filename = ""
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    def files(self):
        self.Entry2.delete(0, 'end')
        self.filename = filedialog.askopenfilename()

        self.Entry2.insert(0,self.filename)

    def face(self):
        try:

            self.picture = cv2.imread(self.Entry2.get())
     

            self.picture = cv2.resize(self.picture, (600, 450))

            self.gray = cv2.cvtColor(self.picture, cv2.COLOR_BGR2GRAY)
            self.faces = self.face_cascade.detectMultiScale(self.gray, 1.9, 2)

            for (x, y, w, h) in self.faces:
                cv2.rectangle(self.picture, (x, y), (x + w, y + h), (0, 0, 255), 2)


            cv2.imshow('Face only', self.picture)
            cv2.waitKey(0)

            cv2.destroyAllWindows()
        except:
            messagebox.showerror("Can't open file", "Selected file is not an image, or it is corrupted")

    def eyes_only(self):
        try:

            self.picture = cv2.imread(self.Entry2.get())
            
            self.picture = cv2.resize(self.picture, (600, 450))

            self.gray = cv2.cvtColor(self.picture, cv2.COLOR_BGR2GRAY)
            self.faces = self.face_cascade.detectMultiScale(self.gray, 1.9, 2)

            for (x, y, w, h) in self.faces:

                self.roi_gray = self.gray[y:y + h, x:x + w]
                self.roi_color = self.picture[y:y + h, x:x + w]
                self.eyes = self.eye_cascade.detectMultiScale(self.roi_gray, 1.1, 4)
                for (ex, ey, ew, eh) in self.eyes:
                    cv2.rectangle(self.roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            cv2.imshow('Eyes Only', self.picture)
            cv2.waitKey(0)

            cv2.destroyAllWindows()
        except Exception as ex:
            messagebox.showerror("Can't open file", "Selected file is not an image, or it is corrupted")
    def eyes_face(self):
        try:
            self.picture = cv2.imread(self.Entry2.get())
    
            self.picture = cv2.resize(self.picture, (600, 450))

            self.gray = cv2.cvtColor(self.picture, cv2.COLOR_BGR2GRAY)
            self.faces = self.face_cascade.detectMultiScale(self.gray, 1.9,2)

            for (x, y, w, h) in self.faces:
                cv2.rectangle(self.picture, (x, y), (x + w, y + h), (0, 0, 255), 2)
                self.roi_gray = self.gray[y:y + h, x:x + w]
                self.roi_color = self.picture[y:y + h, x:x + w]
                self.eyes = self.eye_cascade.detectMultiScale(self.roi_gray,1.1,4)
                for (ex, ey, ew, eh) in self.eyes:
                    cv2.rectangle(self.roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            cv2.imshow('Eyes and Face', self.picture)
            cv2.waitKey(0)


            cv2.destroyAllWindows()
        except Exception as ex:

            messagebox.showerror("Can't open file", "Selected file is not an image, or it is corrupted")

    def mainwindow(self):

        font11 = "-family {DejaVu Sans} -size 18 -weight normal -slant" \
         " roman -underline 0 -overstrike 0"
        font13 = "-family {DejaVu Sans} -size 20 -weight normal -slant" \
         " roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans} -size 14 -weight normal -slant " \
        "roman -underline 0 -overstrike 0"
        font8 = "-family {DejaVu Sans Mono} -size 10 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        window = tk.Tk()
        window.geometry("776x602+264+47")
        window.resizable(False,False)
        window.title("Facial & Eye Detection")

        self.Frame1 = tk.Frame(window)
        self.Frame1.place(relx=0.013, rely=0.0, relheight=0.689, relwidth=0.973)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="4")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d8d8d8")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=-0.013, rely=0.0, height=411, width=779)
        self.Label1.configure(borderwidth="4")
        self.photo_location = ("images/brain.png")

        self.img = tk.PhotoImage(file=self.photo_location)
        self.Label1.configure(image=self.img)

        self.Labelframe1 = tk.LabelFrame(window)
        self.Labelframe1.place(relx=0.013, rely=0.698, relheight=0.291, relwidth=0.554)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(borderwidth="4")
        self.Labelframe1.configure(font=font13)
        self.Labelframe1.configure(foreground="#ff0f27")
        self.Labelframe1.configure(text='''Image''')
        self.Labelframe1.configure(highlightbackground="#d81818")

        self.Button3 = tk.Button(self.Labelframe1)
        self.Button3.place(relx=0.698, rely=0.743, height=31, width=121, bordermode='ignore')
        self.Button3.configure(background="#3a7069")
        self.Button3.configure(font=font11)
        self.Button3.configure(text="View")

        self.Entry2 = tk.Entry(self.Labelframe1)
        self.Entry2.place(relx=0.023, rely=0.229, height=35, relwidth=0.712, bordermode='ignore')
        self.Entry2.configure(background="#cac2ff")
        self.Entry2.configure(font=font8)
        self.Entry2.configure(highlightthickness="2")

        self.Button4 = tk.Button(self.Labelframe1)
        self.Button4.place(relx=0.744, rely=0.229, height=33, width=96, bordermode='ignore')
        self.Button4.configure(background="#3a7069")
        self.Button4.configure(font=font9)
        self.Button4.configure(text='''Browse''')
        self.Button4.configure(command=self.files)

        self.var1 = IntVar()
        self.var2 = IntVar()

        self.RadioButton1 = tk.Radiobutton(self.Labelframe1, variable=self.var1, value=1)
        self.RadioButton1.place(relx=0.023, rely=0.429, relheight=0.166, relwidth=0.288, bordermode='ignore')
        self.RadioButton1.configure(font=font9)
        self.RadioButton1.configure(justify='left')
        self.RadioButton1.configure(text='''Face only''',command=self.view)


        self.RadioButton2 = tk.Radiobutton(self.Labelframe1, variable=self.var1, value=2)
        self.RadioButton2.place(relx=0.023, rely=0.6, relheight=0.166, relwidth=0.291, bordermode='ignore')
        self.RadioButton2.configure(font=font9)
        self.RadioButton2.configure(justify='left')
        self.RadioButton2.configure(text='''Eyes only''',command=self.view)


        self.RadioButton3 = tk.Radiobutton(self.Labelframe1,value=3,variable=self.var1)
        self.RadioButton3.place(relx=0.023, rely=0.771, relheight=0.166, relwidth=0.498, bordermode='ignore')
        self.RadioButton3.configure(font=font9)
        self.RadioButton3.configure(justify='left')
        self.RadioButton3.configure(text='''Both eyes and face''',command=self.view)


        self.Labelframe2 = tk.LabelFrame(window)
        self.Labelframe2.place(relx=0.58, rely=0.698, relheight=0.291, relwidth=0.412)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(borderwidth="4")
        self.Labelframe2.configure(font=font13)
        self.Labelframe2.configure(foreground="#ff1726")
        self.Labelframe2.configure(text='''Live Image''')

        self.Button1 = tk.Button(self.Labelframe2)
        self.Button1.place(relx=0.188, rely=0.686, height=36, width=141, bordermode='ignore')
        self.Button1.configure(background="#3a7069")
        self.Button1.configure(font=font9)
        self.Button1.configure(text="Stream",)



        self.RadioButton4 = tk.Radiobutton(self.Labelframe2,value=4,variable=self.var2)
        self.RadioButton4.place(relx=0.063, rely=0.171, relheight=0.166, relwidth=0.388, bordermode='ignore')
        self.RadioButton4.configure(font=font9)
        self.RadioButton4.configure(text="Face only",command=self.stream)


        self.RadioButton5 = tk.Radiobutton(self.Labelframe2,text="Eyes only",value=5,variable=self.var2)
        self.RadioButton5.place(relx=0.063, rely=0.343, relheight=0.166, relwidth=0.391, bordermode='ignore')
        self.RadioButton5.configure(font=font9)
        self.RadioButton5.configure(justify='left',command=self.stream)



        self.RadioButton6 = tk.Radiobutton(self.Labelframe2,text="Both eyes and face",value=6,variable=self.var2)
        self.RadioButton6.place(relx=0.063, rely=0.514, relheight=0.166, relwidth=0.669, bordermode='ignore')
        self.RadioButton6.configure(font=font9)
        self.RadioButton6.configure(justify='left',command=self.stream)
        window.mainloop()

    def stream(self):

        if (self.var2.get()) ==6:
            self.Button1.configure(command=page.live_image().face_eyes)
        if (self.var2.get()) ==5:
            self.Button1.configure(command=page.live_image().video_eyes)
        if (self.var2.get()) ==4:
            self.Button1.configure(command=page.live_image().video_face)
    def view(self):
        if self.var1.get() ==1:
            self.Button3.configure(command=self.face)
        if self.var1.get() ==2:
            self.Button3.configure(command=self.eyes_only)
        if self.var1.get() ==3:
            self.Button3.configure(command=self.eyes_face)
mainframe().mainwindow()
