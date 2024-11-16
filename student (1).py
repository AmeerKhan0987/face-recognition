import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import logging
import cv2



# Create a logger
logger = logging.getLogger(__name__)

class Student(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

        # Create a database connection
        self.conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="password",
            database="face_recognition"
        )
        self.cur = self.conn.cursor()

        # Create variables
        self.var_depar = tk.StringVar()
        self.var_course = tk.StringVar()
        self.var_year = tk.StringVar()
        self.var_semester = tk.StringVar()
        self.var_studeent_id = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_division = tk.StringVar()
        self.var_roll_no = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_dob = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_phone = tk.StringVar()
        self.var_address = tk.StringVar()
        self.var_teacher = tk.StringVar()
        self.var_photosample = tk.StringVar()


        img = Image.open(r"C:\face  img\IntegralUniversity friont image.png")
        img = img.resize((510,150), resample=Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img)

        f_lbl1 = tk.Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=510, height=130)


        title_lbl=tk.Label(self.root, text="FACE RECOGNITION SYSTEM SOFTWARE", font=("times new roman",35,"bold"), bg="white", fg="red")
        title_lbl.place(x=0,y=130,width=1530,height=45)


        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Create main frame
        main_frame = tk.Frame(self.root, bd=2, bg="white")
        main_frame.place(x=0, y=175, width=1530, height=620)

        # Create left frame
        left_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief="ridge", text="Student Detail", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=750, height=560)

        # Create current course frame
        current_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief="ridge", text="Current course", font=("times new roman", 12, "bold"))
        current_frame.place(x=15, y=35, width=740, height=130)

        # Create department label and combo box
        dep_label = tk.Label(current_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        dep_combo = ttk.Combobox(current_frame, textvariable=self.var_depar, font=("times new roman", 12), width=17, state="readonly")
        dep_combo['values'] = ("Select Department", "Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Nursing", "Public Health", "Medicine")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=10, sticky="W")

        # Create course label and combo box
        course_label = tk.Label(current_frame, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10, pady=10, sticky="W")
        course_combo = ttk.Combobox(current_frame, textvariable=self.var_course, font=("times new roman", 12), width=17, state="readonly")
        course_combo['values'] = (" Select Course", "(CSE)", "(ECE)", "(ME)", "(CE)", "(EE)", "(IT)", "(AE)", "(BT)", "(CH)", "(TE)", "(BCA)", "(MCA)", "Software Development", "(CSE)", "(ECE)", "(ME)", "(CE)", "(EE)", "(IT)", "(AE)", "(BT)", "(CH)", "(TE)")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=10, pady=10, sticky="W")

        # Create year label and combo box
        year_label = tk.Label(current_frame, text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        year_combo = ttk.Combobox(current_frame, textvariable=self.var_year, font=("times new roman", 12), width=17, state="readonly")
        year_combo['values'] = ("Select Year", "2020-2021", "2021-2022", "2022-2023", "2023-2024", "2024-2025")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        # Create semester label and combo box
        semester_label = tk.Label(current_frame, text="Semester", font=("times new roman", 12, "bold"))
        semester_label.grid(row=1, column=2, padx=10, pady=10, sticky="W")
        semester_combo = ttk.Combobox(current_frame, textvariable=self.var_semester, font=("times new roman", 12), width=17, state="readonly")
        semester_combo['values'] = ("Select Semester", "S-1", "S-2", "S-3", "S-4", "S-5", "S-6","S-7","S-8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=10, pady=10, sticky="W")

        # Create class student frame
        class_student_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief="ridge", text="Class Student", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=15, y=175, width=740, height=390)

        # Create student ID label and entry
        studeent_id_label = tk.Label(class_student_frame, text="Student ID :", font=("times new roman", 12))
        studeent_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        studeent_id_entry = tk.Entry(class_student_frame, textvariable=self.var_studeent_id, width=20, font=("times new roman", 12))
        studeent_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="W")

        # Create student name label and entry
        student_name_label = tk.Label(class_student_frame, text="Student Name :", font=("times new roman", 12))
        student_name_label.grid(row=0, column=2, padx=10, pady=10, sticky="W")
        student_name_entry = tk.Entry(class_student_frame, textvariable=self.var_name, width=20, font=("times new roman", 12))
        student_name_entry.grid(row=0, column=3, padx=10, pady=10, sticky="W")

        # Create class division label and combo box
        class_division_label = tk.Label(class_student_frame, text="Class division :", font=("times new roman", 12))
        class_division_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        class_division_combo = ttk.Combobox(class_student_frame, textvariable=self.var_division, font=("times new roman", 12), width=17, state="readonly")
        class_division_combo['values'] = ("Select division", "A", "B", "C", "D", "E", "F", "G", "H", "I")
        class_division_combo.current(0)
        class_division_combo.grid(row=1, column=1, padx=10, pady=10, sticky="W")

        # Create roll_no number label and entry
        roll_number_label = tk.Label(class_student_frame, text="Roll Number :", font=("times new roman", 12))
        roll_number_label.grid(row=1, column=2, padx=10, pady=10, sticky="W")
        roll_number_entry = tk.Entry(class_student_frame, textvariable=self.var_roll_no, width=20, font=("times new roman", 12))
        roll_number_entry.grid(row=1, column=3, padx=10, pady=10, sticky="W")

        # Create gender label and combo box
        gender_label = tk.Label(class_student_frame, text="Gender :", font=("times new roman", 12))
        gender_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12), width=17, state="readonly")
        gender_combo['values'] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=10, sticky="W")

        # Create DOB label and entry
        dob_label = tk.Label(class_student_frame, text="DOB :", font=("times new roman", 12))
        dob_label.grid(row=2, column=2, padx=10, pady=10, sticky="W")
        dob_entry = tk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 12))
        dob_entry.grid(row=2, column=3, padx=10, pady=10, sticky="W")

        # Create email label and entry
        email_label = tk.Label(class_student_frame, text="Email :", font=("times new roman", 12))
        email_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")
        email_entry = tk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12))
        email_entry.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        # Create phone number label and entry
        phone_number_label = tk.Label(class_student_frame, text="Phone Number :", font=("times new roman", 12))
        phone_number_label.grid(row=3, column=2, padx=10, pady=10, sticky="W")
        phone_number_entry = tk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12))
        phone_number_entry.grid(row=3, column=3, padx=10, pady=10, sticky="W")

        # Create address label and entry
        address_label = tk.Label(class_student_frame, text="Address :", font=("times new roman", 12))
        address_label.grid(row=4, column=0, padx=10, pady=10, sticky="W")
        address_entry = tk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12))
        address_entry.grid(row=4, column=1, padx=10, pady=10, sticky="W")

        # Create teacher name label and entry
        teacher_name_label = tk.Label(class_student_frame, text="Teacher Name :", font=("times new roman", 12))
        teacher_name_label.grid(row=4, column=2, padx=10, pady=10, sticky="W")
        teacher_name_entry = tk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12))
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=10, sticky="W")

        # Create radio buttons
        self.var_radio1 = tk.StringVar()
        radio_button1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text=" Photo sample", value="yes")
        radio_button1.grid(row=5, column=0, padx=10, pady=10,sticky="W")
        radio_button2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No photo sample", value="no")
        radio_button2.grid(row=5, column=1, padx=10, pady=10,sticky="W")

        # Create button frame
        button_frame = tk.Frame(class_student_frame, bd=2, relief="ridge", bg="white")
        button_frame.place(x=18, y=255, width=710, height=50)

        # Create save button
        save_button = tk.Button(button_frame, text="Save", command=self.add_data, font=("times new roman", 12, "bold"), fg="white", bg="black")
        save_button.place(x=20, y=10, width=130, height=30)

        # Create update button
        update_button = tk.Button(button_frame, text="Update", command=self.update_data, font=("times new roman", 12, "bold"), fg="white", bg="black")
        update_button.place(x=170, y=10, width=130, height=30)

        # Create delete button
        delete_button = tk.Button(button_frame, text="Delete", command=self.delete_data, font=("times new roman", 12, "bold"), fg="white", bg="black")
        delete_button.place(x=320, y =10, width=130, height=30)

        # Create reset button
        reset_button = tk.Button(button_frame, text="Reset", command=self.reset_data, font=("times new roman", 12, "bold"), fg="white", bg="black")
        reset_button.place(x=470, y=10, width=130, height=30)

        # Create frame for student details
        button_frame1 = tk.Frame(class_student_frame, bd=2, relief="ridge", bg="white")
        button_frame1.place(x=18, y=310, width=710, height=50)

        # Create take photo button
        take_photo_button = tk.Button(button_frame1, text="Take photo Sample",command=self.generate_database, font=("times new roman", 12, "bold"), fg="white", bg="black")
        take_photo_button.place(x=20, y=10, width=160, height=30)

        # Create update photo button
        update_photo_button = tk.Button(button_frame1, text="Update photo Sample", font=("times new roman", 12, "bold"), fg="white", bg="black")
        update_photo_button.place(x=320, y=10, width=160, height=30)

        # Create right frame
        right_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief="ridge", text="Student Detail", font=("times new roman", 12, "bold"))
        right_frame.place(x=765, y=10, width=750, height=600)

        # Create search frame
        search_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief="ridge", text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=770, y=35, width=740, height=70)

        # Create search label and combo box
        search_label = tk.Label(search_frame, text="Search by:", font=("times new roman", 12, "bold"))
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12), width=17, state="readonly")
        search_combo['values'] = ("Select", "roll_no No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=10, sticky="W")

        # Create search button
        search_button = tk.Button(search_frame, text="Search ", width=13, font=("times new roman", 12, "bold"), fg="white", bg="black")
        search_button.grid(row=0, column=3, padx=10, pady=10, sticky="W")

        # Create show all button
        show_all_button = tk.Button(search_frame, text="Show all", width=13, font=("times new roman", 12, "bold"), fg="white", bg="black")
        show_all_button.grid(row=0, column=4, padx=10, pady=10, sticky="W")

        # Create table frame
        table_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief="ridge")
        table_frame.place(x=770, y=110, width=740, height=500)

        # Create scroll_no bars
        scroll_x = ttk.Scrollbar(table_frame, orient="horizontal")
        scroll_y = ttk.Scrollbar(table_frame, orient="vertical")

        # Create student table
        self.student_table = ttk.Treeview(table_frame, columns=("depar", "course", "year", "sem", "studeent_id", "name", "division", "roll_no", "gender", "dob", "email", "address", "phone", "teacher", "photosample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Configure student table
        self.student_table.heading("depar", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("studeent_id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("division", text="division")
        self.student_table.heading("roll_no", text="roll_no No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photosample", text="photosample")
        self.student_table["show"] = "headings"

        # Configure student table columns
        self.student_table.column("depar", width=120)
        self.student_table.column("course", width=80)
        self.student_table.column("year", width=80)
        self.student_table.column("sem", width=50)
        self.student_table.column("studeent_id", width=100)
        self.student_table.column("name", width=150)
        self.student_table.column("division", width=80)
        self.student_table.column("roll_no", width=100)
        self.student_table.column("gender", width=50)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("address", width=150)
        self.student_table.column("phone", width=90)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photosample", width=70)

        # Pack student table
        self.student_table.pack(fill="both", expand=1)

        # Bind student table to get data function
        self.student_table.bind("<ButtonRelease>", self.get_data)

        # Fetch data
        self.fetch_data()

    def add_data(self):
     if self.var_depar.get() == "Select Department" or self.var_name.get() == "" or self.var_studeent_id.get() == "":
        messagebox.showerror("Error", "All Fields are required")
     else:
        try:
            print(self.conn.is_connected())
            print("insert into student (Depar, Course, Year, Semester, studeent_id, name, division, roll_no, gender, dob, email, address, phone, teacher, photosample) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                self.var_depar.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_studeent_id.get(),
                self.var_name.get(),
                self.var_division.get(),
                self.var_roll_no.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_address.get(),
                self.var_phone.get(),
                self.var_teacher.get(),
                self.var_photosample.get()
            ))

            # SQL Insert Query
            # Enclose string values retrieved from variables in single quotes
            self.cur.execute("INSERT INTO student (`Depar`, `Course`, `Year`, `Semester`, `studeent_id`, `name`, `division`, `roll_no`, `gender`, `dob`, `email`, `address`, `phone`, `teacher`, `photosample`) " "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                    self.var_depar.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_studeent_id.get(),
                    self.var_name.get(),
                    self.var_division.get(),
                    self.var_roll_no.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_phone.get(),
                    self.var_teacher.get(),
                    self.var_photosample.get()
                ))
            
            # Commit changes
            self.conn.commit()
            messagebox.showinfo("Success", "Data added successfully", parent=self.root)
            self.fetch_data()

        except mysql.connector.Error as err:
            # Show error message
            messagebox.showerror("Error", f"Error: {err}", parent=self.root)
            # Log the error
            logging.error(err)
            print(err)

    def fetch_data(self):
            try:
            
                self.cur.execute("select * from student")
                rows = self.cur.fetchall()
                self.student_table.delete(*self.student_table.get_children())

                for row in rows:
                    self.student_table.insert('', 'end', values=row)

            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)

    def get_data(self, ev):
            row = self.student_table.focus()
            content = self.student_table.item(row)
            row = content["values"]

            # Set values to variables
            self.var_depar.set(row[0])
            self.var_course.set(row[1])
            self.var_semester.set(row[2])
            self.var_year.set(row[3])
            self.var_studeent_id.set(row[4])
            self.var_name.set(row[5])
            self.var_division.set(row[6])
            self.var_roll_no.set(row[7])
            self.var_gender.set(row[8])
            self.var_dob.set(row[9])
            self.var_email.set(row[10])
            self.var_phone.set(row[11])
            self.var_address.set(row[12])
            self.var_teacher.set(row[13])
            self.var_photosample.set(row[14])

    def update_data(self):
        if self.var_depar.get() == "" or self.var_course.get() == "" or self.var_semester.get() == "" or self.var_year.get() == "" or self.var_studeent_id.get() == "" or self.var_name.get() == "" or self.var_division.get() == "" or self.var_roll_no.get() == "" or self.var_gender.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # SQL Update Query
                self.cur.execute("update student set Depar=%s,Course=%s,Semester=%s,year=%s,studeent_id=%s,name=%s,division=%s,roll_no=%s,gender=%s,dob=%s,email=%s,address =%s,phone=%s,teacher=%s,photosample=%s where studeent_id=%s", (
                    self.var_depar.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_studeent_id.get(),
                    self.var_name.get(),
                    self.var_division.get(),
                    self.var_roll_no.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_phone.get(),
                    self.var_teacher.get(),
                    self.var_photosample.get(),
                    self.var_studeent_id.get()
                ))

                # Commit changes
                self.conn.commit()

                # Show success message
                messagebox.showinfo("Success", "Data updated successfully", parent=self.root)

                # Fetch updated data
                self.fetch_data()

            except Exception as es:
                # Show error message
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_studeent_id.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                # SQL Delete Query
                self.cur.execute("delete from student where studeent_id=%s", (self.var_studeent_id.get(),))
                self.conn.commit()
                messagebox.showinfo("Success", "Data deleted successfully", parent=self.root)
                self.fetch_data()

            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)

    def reset_data(self):
        # Reset variables
            self.var_depar.set("Select Department")
            self.var_course.set("Select Course")    
            self.var_year.set("")
            self.var_semester.set("")
            self.var_studeent_id.set("")
            self.var_name.set("")
            self.var_division.set("")
            self.var_roll_no.set("")
            self.var_gender.set("")
            self.var_dob.set("")
            self.var_email.set("")
            self.var_phone.set("")
            self.var_address.set("")
            self.var_teacher.set("")
            self.var_photosample.set("")


    def generate_database(self):
     if self.var_depar.get() == "" or self.var_course.get() == "" or self.var_semester.get() == "" or self.var_year.get() == "" or self.var_studeent_id.get() == "" or self.var_name.get() == "" or self.var_division.get() == "" or self.var_roll_no.get() == "" or self.var_gender.get() == "" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_phone.get()=="" or self.var_teacher.get()=="" :
        messagebox.showerror("Error", "All Fields are required", parent=self.root)
     else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="password", database="face_recognition")
            self.cur = conn.cursor()
            self.cur.execute("SELECT * FROM student")
            myresult = self.cur.fetchall()
            id = 0
            for row in myresult:
                id += 1
            self.cur.execute("INSERT INTO student (Depar, Course, Semester, year, studeent_id, name, division, roll_no, gender, dob, email, address, phone, teacher) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                self.var_depar.get(),
                self.var_course.get(),
                self.var_semester.get(),
                self.var_year.get(),
                self.var_studeent_id.get(),
                self.var_name.get(),
                self.var_division.get(),
                self.var_roll_no.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_address.get(),
                self.var_phone.get(),
                self.var_teacher.get(),
       
            ))
            conn.commit()
            messagebox.showinfo("Success", "Student Added Successfully", parent=self.root)
            self.clear()
            self.fetch_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)
        conn.close()

    def draw_rectangle(self, img):
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            return img[y:y+h, x:x+w]
        return None  # Return None if no face is detected

    def generate_dataset(self):
        cap = cv2.VideoCapture(0)
        img_id = 0
        while True:
            ret, my_frame = cap.read()
            if ret:
                face = self.draw_rectangle(my_frame)
                if face is not None:
                    img_id += 1
                    cv2.imwrite("student/" + str(img_id) + ".jpg", face)
                    face = cv2.resize(face, (450, 450))
                    cv2.putText(my_frame, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("frame", my_frame)
                    cv2.imshow("face", face)
                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Generating data sets completed")



        
if __name__ == "__main__":
    root = tk.Tk()
    obj = Student(root)
    root.mainloop()