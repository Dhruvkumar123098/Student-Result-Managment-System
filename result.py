from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class resultClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        title=Label(self.root,text="Add Student Result",font=("goudy old style",20,"bold"),bg="#262626",fg="white").place(x=10,y=15,width=1300,height=50)
        #variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()



        #widget
        lbl_select=Label(self.root,text="Select student",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=80)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=120)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=160)
        lbl_marks=Label(self.root,text="Marks",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=200)
        lbl_full_marks=Label(self.root,text="full narks",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=240)
        #entry field
        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,state="readonly",justify=CENTER,font=("goudy old style",15,"bold"))
        self.txt_student.place(x=150,y=80,width=200)
        self.txt_student.set("Select")
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.search)
        btn_search.place(x=360,y=80,width=120,height=30)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow",state='readonly').place(x=150,y=120,width=200)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow",state='readonly').place(x=150,y=160,width=200)
        txt_marks=Entry(self.root,textvariable=self.var_marks,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=200,width=200)
        txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=240,width=200)

        #buttons
        btn_add=Button(self.root,text="Add",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.add).place(x=150,y=280,width=100,height=30)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.clear).place(x=260,y=280,width=100,height=30)



    
        #funtions
    def fetch_roll(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    self.roll_list.append(row[0])
            else:
                messagebox.showerror("Error", "No students found")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
    def search(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()
        try:
            
            cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
            rows=cur.fetchone()
            if rows!=None:
                self.var_name.set(rows[0])
                self.var_course.set(rows[1])


            else:
                messagebox.showerror("Error","No record found",parent=self.root)
            
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to {str(ex)}")

    def add(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please search first student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already present, try different",parent=self.root)
                else:
                    per=(int(self.var_marks.get())/int(self.var_full_marks.get()))*100
                    cur.execute("insert into result (roll,name,course,marks_ob,full_marks,percentage) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)


                        
                    )) 
                    con.commit()
                    messagebox.showinfo("Success","result added successfully",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to {str(ex)}")
    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")

    





















if __name__ == '__main__':
    root = Tk()
    obj = resultClass(root)
    root.mainloop()
