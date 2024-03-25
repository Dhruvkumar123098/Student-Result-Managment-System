from tkinter import *
from PIL import Image, ImageTk
from Course import COurseClass
from student import StudentClass
from result import resultClass
from report import reportClass
class RMS:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #icons
        self.icon_student=ImageTk.PhotoImage(file="images/logo_p.png")
        


        title=Label(self.root,text="Student Management System",padx=10,compound=LEFT,image=self.icon_student,font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
        #menu
        M_Frame =LabelFrame(self.root,text="Menu",font=("goudy old style",15,"bold"),bg="white",fg="black")
        M_Frame.place(x=10,y=70,width=1250,height=80)

        #buttons
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand1",width=10,command=self.add_courses).place(x=10,y=5,width=150,height=40) 
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand1",width=10,command=self.add_students).place(x=170,y=5,width=150,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand1",width=10,command=self.add_result).place(x=332,y=5,width=150,height=40) 
        btn_view_result=Button(M_Frame,text="View Result",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand1",width=10,command=self.add_report).place(x=492,y=5,width=150,height=40) 
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand1",width=10).place(x=657,y=5,width=150,height=40) 
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand1",width=10).place(x=817,y=5,width=150,height=40) 

        #content
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,470),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        #update details

        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20,"bold"),bg="#262626",fg="white").place(x=50,y=180)
        self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20,"bold"),bg="#262626",fg="white").place(x=50,y=280)
        self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("goudy old style",20,"bold"),bg="#262626",fg="white").place(x=50,y=380)
        #make the website more good by adding some designs
        
        

        #footer      
        footer=Label(self.root,text="Developed by Dhruv",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
    def add_courses(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=COurseClass(self.new_win)
    def add_students(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

if __name__ == '__main__':
    root = Tk()
    obj = RMS(root)
    root.mainloop()
