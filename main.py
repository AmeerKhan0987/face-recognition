import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from face_recognition_system.student import Student

class Face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # 1 image
        img = Image.open(r"C:\face  img\IntegralUniversity friont image.png")
        img = img.resize((510,150), resample=Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img)

        f_lbl1 = tk.Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=510, height=130)


        title_lbl=tk.Label(self.root, text="FACE RECOGNITION SYSTEM SOFTWARE", font=("times new roman",35,"bold"), bg="white", fg="red")
        title_lbl.place(x=0,y=130,width=1530,height=45)

        # student button
        try:
            img3 = Image.open(r"E:\face  img\student1.jpg")
            img3 = img3.resize((300,250), resample=Image.LANCZOS) 
            self.photo_button_student = ImageTk.PhotoImage(img3)
        except Exception as e:
            print(f"Error opening image: {e}")

        b1_student = tk.Button(self.root, image=self.photo_button_student, cursor="hand2", command=self.student_detail)
        b1_student.place(x=60, y=230, width=300, height=220)

        block1 = tk.Button(self.root, text="", borderwidth=0, relief='flat',bg="white")
        block1.place(x=60, y=445, width=300, height=5 )

        b1_1_student = tk.Button(self.root, text="Student Detail", cursor="hand2",command=self.student_detail, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1_student.place(x=60, y=450, width=300, height=40)

        # Face Detector button
        img4 = Image.open(r"C:\face  img\detector.jpeg")
        img4 = img4.resize((300,250), resample=Image.LANCZOS) 
        self.photoimg_button_detector = ImageTk.PhotoImage(img4)

        b1_detector = tk.Button(self.root, image=self.photoimg_button_detector, cursor="hand2")
        b1_detector.place(x=430, y=230, width=300, height=220)

        block2 = tk.Button(self.root, text="", borderwidth=0, relief='flat',bg="white")
        block2.place(x=430, y=445, width=300, height=5 )

        b1_2_detector = tk.Button(self.root, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_2_detector.place(x=430, y=450, width=300, height=40)

        # Attendence button
        img5 = Image.open(r"C:\face  img\Attendence.png")
        img5 = img5.resize((300,250), resample=Image.LANCZOS) 
        self.photoimg_button_attendence = ImageTk.PhotoImage(img5)

        b1_attendence = tk.Button(self.root, image=self.photoimg_button_attendence, cursor="hand2")
        b1_attendence.place(x=790, y=230, width=300, height=220)

        block3 = tk.Button(self.root, text="", borderwidth=0, relief='flat',bg="white")
        block3.place(x=790, y=445, width=300, height=5 )

        b1_3_attendence = tk.Button(self.root, text="Attendence", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_3_attendence.place(x=790, y=450, width=300, height=40)

        # Help Desk button
        img6 = Image.open(r"C:\face  img\helpdesk.jpg")
        img6 = img6.resize((300,250), resample=Image.LANCZOS) 
        self.photoimg_button_helpdesk = ImageTk.PhotoImage(img6)

        b1_helpdesk = tk.Button(self.root, image=self.photoimg_button_helpdesk, cursor="hand2")
        b1_helpdesk.place(x=1150, y=230, width=300, height=220)

        block4 = tk.Button(self.root, text="", borderwidth=0, relief='flat',bg="white")
        block4.place(x=1150, y=445, width=300, height=5 )

        b1_4_helpdesk = tk.Button(self.root, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_4_helpdesk.place(x=1150, y=450, width=300, height=40)

        # Train Data button
        img7 = Image.open(r"C:\face  img\train data.jpeg")
        img7 = img7.resize((300,250), resample=Image.LANCZOS) 
        self.photoimg_button_traindata = ImageTk.PhotoImage(img7)

        b1_traindata = tk.Button(self.root, image=self.photoimg_button_traindata, cursor="hand2")
        b1_traindata.place(x=60, y=520, width=300, height=220)
        
        block1 = tk.Button(self.root, text="", borderwidth=0, relief='flat',bg="white")
        block1.place(x=60, y=715, width=300, height=5 )

        b1_5_traindata = tk.Button(self.root, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_5_traindata.place(x=60, y=720, width=300, height=40)

        # photosamples Collection button
        img8 = Image.open(r"C:\face  img\photos.jpeg")
        img8 = img8.resize((300,250), resample=Image.LANCZOS) 
        self.photoimg_button_photos = ImageTk.PhotoImage(img8)

        b1_photos = tk.Button(self.root, image=self.photoimg_button_photos, cursor="hand2")
        b1_photos.place(x=430, y=520, width=300, height=220)

        block1 = tk.Button(self.root, text="", borderwidth=0, relief='flat',bg="white")
        block1.place(x=430, y=715, width=300, height=5 )

        b1_6_photos = tk.Button(self.root, text="photos Collection", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_6_photos.place(x=430, y=720, width=300, height=40)

        # Developer button
        img9 = Image.open(r"C:\face  img\Developers.jpg")
        img9 = img9.resize((300,250), resample=Image.LANCZOS) 
        self.photoimg_button_developer = ImageTk.PhotoImage(img9)

        b1_developer = tk.Button(self.root, image=self.photoimg_button_developer, cursor="hand2")
        b1_developer.place(x=790, y=520, width=300, height=220)

        block1 = tk.Button(self.root, text="", borderwidth=0, relief='flat',bg="white")
        block1.place(x=790, y=715, width=300, height=5 )

        b1_7_developer = tk.Button(self.root, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_7_developer.place(x=790, y=720, width=300, height=40)

        # Exit button
        img10 = Image.open(r"C:\face  img\Exit.jpeg")
        img10 = img10.resize((300,250), resample=Image.LANCZOS) 
        self.photo_button_exit = ImageTk.PhotoImage(img10)

        b1_exit = tk.Button(self.root, image=self.photo_button_exit, cursor="hand2")
        b1_exit.place(x=1150, y=520, width=300, height=220)

        block1 = tk.Button(self.root, text="", borderwidth=0, relief='flat',bg="white")
        block1.place(x=1150, y=715, width=300, height=5 )

        b1_8_exit = tk.Button(self.root, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_8_exit.place(x=1150, y=720, width=300, height=40)


    def student_detail(self):
        self.new_window=tk.Toplevel(self.root)
        self.app=Student(self.new_window)

if __name__ == "__main__":
    root = tk.Tk()
    obj = Face_recognition_system(root)
    root.mainloop()