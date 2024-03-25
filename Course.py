from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class COurseClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #title
        title=Label(self.root,text="Manage course detail",font=("goudy old style",20,"bold"),bg="#262626",fg="white").place(x=10,y=15,width=1180,height=40)
        #variables
        self.var_course_name=StringVar()
        self.var_duration=StringVar()
        self.var_fee=StringVar()

       
        #widgets
        lbl_course_name=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_duration=Label(self.root,text="Course Dur",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_fee=Label(self.root,text="Course Fee",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_description=Label(self.root,text="Course Des",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)


        self.txt_course_name=Entry(self.root,textvariable=self.var_course_name,font=("goudy old style",15,"bold"),bg="white")
        self.txt_course_name.place(x=150,y=60,width=200)
        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="white").place(x=150,y=100,width=200)
        txt_fee=Entry(self.root,textvariable=self.var_fee,font=("goudy old style",15,"bold"),bg="white").place(x=150,y=140,width=200)
        self.txt_description=Text(self.root,font=("goudy old style",15,"bold"),bg="white")
        self.txt_description.place(x=150,y=180,width=500,height=100)

        #buttons
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=300,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=300,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=300,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=300,width=110,height=40)

        #search panel
        self.var_search=StringVar()
        lbl_search_course_name=Label(self.root,text="Search By Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        txt_search_course_name=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="white").place(x=950,y=60,width=200)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.search)
        btn_search.place(x=1150,y=60,width=110,height=27)

        #content
        self.C_Frame =Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=540,height=340)
        scroll_x=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.C_Frame,orient=VERTICAL)
         

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","fee","description"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.CourseTable.xview)
        scroll_y.config(command=self.CourseTable.yview)
        self.CourseTable.heading("cid",text="ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("fee",text="Fee")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]="headings"
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("fee",width=100)
        self.CourseTable.column("description",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    def search(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()
        try:
            if self.var_search.get()!="":
                cur.execute("select * from Course where name LIKE '%"+self.var_search.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.CourseTable.delete(*self.CourseTable.get_children())
                    for row in rows:
                        self.CourseTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            else:
                messagebox.showerror("Error","search field should not be empty",parent=self.root)
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to {str(ex)}")    
    def delete(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()
        try:
            if self.var_course_name.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root)
            else:
                cur.execute("select * from Course where name=?",(self.var_course_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","select course from list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.root)
                    if op==True:
                        cur.execute("delete from Course where name=?",(self.var_course_name.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Course deleted successfully",parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to {str(ex)}") 
    def clear(self):
        self.var_course_name.set("")
        self.var_duration.set("")
        self.var_search.set("")
        self.var_fee.set("")
        self.txt_description.delete('1.0',END)
        self.txt_course_name.config(state="normal")
        self.txt_course_name.focus()
        self.show()
    def get_data(self,ev):
        self.txt_course_name.config(state="readonly")
        self.txt_course_name.delete(0,END)
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content['values']
        self.var_course_name.set(row[1])
        self.var_duration.set(row[2])
        self.var_fee.set(row[3])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])

    def add(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()
        try:
            if self.var_course_name.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root)
            else:
                cur.execute("select * from Course where name=?",(self.var_course_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course name already present, try different",parent=self.root)
                else:
                    cur.execute("insert into Course (name,duration,fee,description) values(?,?,?,?)",(
                        self.var_course_name.get(),
                        self.var_duration.get(),
                        self.var_fee.get(),
                        self.txt_description.get('1.0',END)
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
            if self.var_course_name.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root)
            else:
                cur.execute("select * from Course where name=?",(self.var_course_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","select course from list",parent=self.root)
                else:
                    cur.execute("update Course set duration=?,fee=?,description=? where name=?",(
                        self.var_duration.get(),
                        self.var_fee.get(),
                        self.txt_description.get('1.0',END),
                        self.var_course_name.get()
                    )) 
                    con.commit()
                    messagebox.showinfo("Success","Course updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database='images.db')
        cur=con.cursor()
        try:
            
            cur.execute("select * from Course")
            row=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for i in row:
                self.CourseTable.insert('',END,values=i)
            
        
        except Exception as ex:
            messagebox.showerror("ERROR",f"Error due to {str(ex)}")


            

          

        






if __name__ == '__main__':
    root = Tk()
    obj = COurseClass(root)
    root.mainloop()