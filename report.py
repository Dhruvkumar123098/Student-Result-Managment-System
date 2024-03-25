from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class reportClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #title
        title=Label(self.root,text="View student result",font=("goudy old style",20,"bold"),bg="#262626",fg="white").place(x=10,y=15,width=1180,height=40)
        #search
        self.var_search=StringVar()
        lbl_search=Label(self.root,text="Search by roll no",font=("goudy old style",15,"bold"),bg="white").place(x=300,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="white").place(x=500,y=100,width=200)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.search)
        btn_search.place(x=750,y=100,width=120,height=25)
        btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.clear)
        btn_clear.place(x=900,y=100,width=120,height=25)

        #labels that include roll, name,course,marks,full marks,percentage that are to be displayed in the form of a table

        lbl_roll=Label(self.root,text="Roll No",font=("goudy old style",15,"bold"),bg="white").place(x=50,y=160)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=200,y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=350,y=160)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white").place(x=500,y=160)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",15,"bold"),bg="white").place(x=650,y=160)
        lbl_percentage=Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bg="white").place(x=800,y=160)
        #table
        self.roll=Label(self.root,font=("goudy old style",15,"bold"),bg="white")
        self.roll.place(x=50,y=200)
        self.name=Label(self.root,font=("goudy old style",15,"bold"),bg="white")
        self.name.place(x=200,y=200)
        self.course=Label(self.root,font=("goudy old style",15,"bold"),bg="white")
        self.course.place(x=350,y=200)
        self.marks=Label(self.root,font=("goudy old style",15,"bold"),bg="white")
        self.marks.place(x=500,y=200)
        self.full_marks=Label(self.root,font=("goudy old style",15,"bold"),bg="white")
        self.full_marks.place(x=650,y=200)
        self.percentage=Label(self.root,font=("goudy old style",15,"bold"),bg="white")
        self.percentage.place(x=800,y=200)

        #delete button at the bottom of the page
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2")
        btn_delete.place(x=500,y=400,width=120,height=30)


        #search function
    def search(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll no should be required",parent=self.root)
            else:
                cur.execute("select * from result where roll=?",(self.var_search.get(),))
                rows=cur.fetchone()
                if rows!=None:
                    self.roll.config(text=rows[1])
                    self.name.config(text=rows[2])
                    self.course.config(text=rows[3])
                    self.marks.config(text=rows[4])
                    self.full_marks.config(text=rows[5])
                    self.percentage.config(text=rows[6])
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to {str(ex)}")

    def clear(self):
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full_marks.config(text="")
        self.percentage.config(text="")

    def delete(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","student name should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","select roll from list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Success","student deleted successfully",parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to {str(ex)}")
        



              























if __name__ == '__main__':
    root = Tk()
    obj = reportClass(root)
    root.mainloop()