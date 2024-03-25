from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class StudentClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #title
        title=Label(self.root,text="Manage student detail",font=("goudy old style",20,"bold"),bg="#262626",fg="white").place(x=10,y=15,width=1180,height=40)
        #variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()

       
        #widgets
        #column 1
        lbl_roll=Label(self.root,text="Roll number",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_email=Label(self.root,text="Course Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        lbl_state=Label(self.root,text="State",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=260)
        lbl_city=Label(self.root,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=220)


        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg="white")
        self.txt_roll.place(x=150,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="white").place(x=150,y=100,width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="white").place(x=150,y=140,width=200)
        txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Male","Female","Other"),font=("goudy old style",15,"bold"),state='readonly',justify=CENTER).place(x=150,y=180,width=200)
        self.txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,"bold"),bg="white")
        txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg="white").place(x=150,y=220,width=200)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg="white").place(x=480,y=220,width=200)

        #column 2
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=100)
        lbl_admission=Label(self.root,text="Admission",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=140)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=180)

        self.txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,"bold"),bg="white")
        self.txt_dob.place(x=480,y=60,width=200)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="white").place(x=480,y=100,width=200)
        txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,"bold"),bg="white").place(x=480,y=140,width=200)
        txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=("Python","CSS","HTML","JAVA","JAVASCRIPT"),font=("goudy old style",15,"bold"),state='readonly',justify=CENTER).place(x=480,y=180,width=200)



        
        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="white")
        self.txt_address.place(x=150,y=260,width=500,height=100)

        #buttons
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #search panel
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Search By Roll number",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="white").place(x=950,y=60,width=200)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.search)
        btn_search.place(x=1150,y=60,width=110,height=27)

        #content
        self.C_Frame =Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=540,height=340)
        scroll_x=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.C_Frame,orient=VERTICAL)
         

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("Roll no","name","Email","Gender","DOB","Contact","Admission","Course","City","State","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.CourseTable.xview)
        scroll_y.config(command=self.CourseTable.yview)
        self.CourseTable.heading("Roll no",text="Roll no")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("Email",text="Email")
        self.CourseTable.heading("Gender",text="Gender")
        self.CourseTable.heading("DOB",text="D.O.B")
        self.CourseTable.heading("Contact",text="Contact")
        self.CourseTable.heading("Admission",text="Admission")
        self.CourseTable.heading("Course",text="Course")
        self.CourseTable.heading("City",text="City")
        self.CourseTable.heading("State",text="State")
        self.CourseTable.heading("Address",text="Address")
        self.CourseTable["show"]="headings"
        self.CourseTable.column("Roll no",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("Email",width=100)
        self.CourseTable.column("Gender",width=100)
        self.CourseTable.column("DOB",width=100)
        self.CourseTable.column("Contact",width=100)
        self.CourseTable.column("Admission",width=100)
        self.CourseTable.column("Course",width=100)
        self.CourseTable.column("City",width=100)
        self.CourseTable.column("State",width=100)
        self.CourseTable.column("Address",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


        

    def search(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()
        try:
            if self.var_search.get()!="":
                cur.execute("select * from student where roll=?",(self.var_search.get(),))
                rows=cur.fetchone()
                if rows!=None:
                    self.CourseTable.delete(*self.CourseTable.get_children())
                    self.CourseTable.insert('',END,values=rows)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to {str(ex)}")                 
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
    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_dob.set("") 
        self.var_contact.set("") 
        self.var_a_date.set("") 
        self.var_course.set("") 
        self.var_city.set("") 
        self.var_state.set("") 
        self.txt_address.delete('1.0', END)
        self.txt_roll.config(state="normal")
        self.var_search.set("")
        self.txt_roll.delete(0,END)
        self.txt_roll.focus()
        self.show()
        
    def get_data(self,ev):
        self.txt_roll.config(state="readonly")
        self.txt_roll.delete(0,END)
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content['values']
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_city.set(row[8]),
        self.var_state.set(row[9]),
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[10])

        

    def add(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()

        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll number already present",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,Email,Gender,DOB,Contact,Admission,Course,City,State,Address) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_city.get(),
                        self.var_state.get(),
                        self.txt_address.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to {str(ex)}")

                    
                

                






    
    
    
    def update(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll no should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","select student from list",parent=self.root)
                else:
                    cur.execute("update student set name=?,Email=?,Gender=?,DOB=?,Contact=?,Admission=?,Course=?,City=?,State=?,Address=? where roll=?",(
                        
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_city.get(),
                        self.var_state.get(),
                        self.txt_address.get('1.0',END),
                        self.var_roll.get()
                    )) 
                    con.commit()
                    messagebox.showinfo("Success","student updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()
        try:
            
            cur.execute("select * from student")
            row=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for i in row:
                self.CourseTable.insert('',END,values=i)
            
        
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to {str(ex)}")


            

          

        






if __name__ == '__main__':
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()
