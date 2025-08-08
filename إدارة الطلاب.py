from tkinter import *
from tkinter import ttk
import pymysql

class student:
# ==================انشاء نافذة البرنامج===========================
     def hi():
          
          print("hellow")  
     
     
     
     def __init__(self,root):
            self.root=root
            self.root.geometry('1280x690')
            self.root.title('برنامج إدارة المدارس')
            self.root.configure(background="silver")
            self.root.resizable(False,False)
            title= Label(self.root,text="نظام تسجيل الطلاب", bd='2 ',bg='#1AAECB',font=('monospace',14,'bold'))
            title.pack(fill="x" )
# ==================================المتغيرات=====================
            self.id_var=StringVar()
            self.name_var=StringVar()
            self.email_var=StringVar()
            self.phone_var=StringVar()
            self.moahel_var=StringVar()
            self.gender_var=StringVar()
            self.address_var=StringVar()
            self.se_var=StringVar()
          
            self.del_var=StringVar()
            self.se_by=StringVar()
            self.se_var=StringVar()
# ======================إدوات التحكم بالبرنامج========================
            manage_fram=Frame(self.root,bg='white')
            manage_fram.place(x=1037,y=30,width=210,height=400)
            lb1_id=Label(manage_fram,  text="الرقم التسلسلي",bg='white')
            lb1_id.pack( )
            id_entry=Entry(manage_fram,textvariable=self.id_var,bd='2',justify="center")
            id_entry.pack()
            lb1_name=Label(manage_fram,text="اسم الطالب",bg='white')
            lb1_name.pack()
            entry_name=Entry(manage_fram, textvariable=self.name_var,  bd='2',justify='center')
            entry_name.pack()
            lb1_email=Label(manage_fram,text=" إيميل الطالب",bg='white')
            lb1_email.pack()
            entry_email=Entry(manage_fram,textvariable=self.email_var,bd='2',justify='center')
            entry_email.pack()
            lb1_phone=Label(manage_fram,text="رقم الطالب",bg='white')
            lb1_phone.pack()
            entry_phone=Entry(manage_fram, bd='2',justify='center')
            entry_phone.pack()
            lb1_certi=Label(manage_fram,text="مؤهلات الطالب",bg='white')
            lb1_certi.pack()
            entery_certi=Entry(manage_fram,textvariable=self.moahel_var,bd='2',justify='center')
            entery_certi.pack()
            lb1_gender=Label(manage_fram,text="اختر جنس الطالب ",bg="white")
            lb1_gender.pack( )
            combobox_gander=ttk.Combobox(manage_fram)
            combobox_gander['value']=('ذكر','انثى')
            combobox_gander.pack()
            lb1_addres=Label(manage_fram,text="عنوان الطالب",bg="white")
            lb1_addres.pack()
            entry_addres=Entry(manage_fram, textvariable=self.address_var, bd='2',justify='center')
            entry_addres.pack()
            lb1_delete=Label(manage_fram,text="حذف الطالب",bg="white",fg="red")
            lb1_delete.pack()
            entry_delete=Entry(manage_fram, textvariable=self.del_var, bd='2',justify='center')
            entry_delete.pack()
# =======================Buttonsالازرار ============================
            btn_frame=Frame(self.root,bg='white')
            btn_frame.place(x=1037,y=430,width=210,height=230)
            title1=Label(btn_frame,text="لوحة التحكم",bg="#2980B9",font=('Deco',14),fg='white')
            title1.pack(fill='x')
            
            add_btn=Button(btn_frame,text="إضافة طالب",bg='#34495E',fg="white",command=self.add_student)
            add_btn.place(x=33,y=33,width=150,height=30)
            del_btn=Button(btn_frame,text="حذف طالب",bg='#34495E',fg="white")
            del_btn.place(x=33,y=63,width=150,height=30)
            update_btn=Button(btn_frame,text="تعديل بياتات طالب",bg='#34495E',fg="white",command=self.apdate)
            update_btn.place(x=33,y=93,width=150,height=30)
            clear_btn=Button(btn_frame,text="إفراغ الحقول",bg='#34495E',fg="white",command=self.clear)
            clear_btn.place(x=33,y=123,width=150,height=30)
            about_btn=Button(btn_frame,text="من نحن",bg='#34495E',fg="white")
            about_btn.place(x=33,y=153,width=150,height=30)
            exit_btn=Button(btn_frame,text="إغلاق البرنامج",bg='#34495E',fg="white")
            exit_btn.place(x=33,y=183,width=150,height=30)
# =====================================search manage===================================
            search_frame=Frame(self.root,bg='white')
            search_frame.place(x=1,y=30,height=50 ,width=1000)
            Label_searach=Label(search_frame,text="البحث عن طالب",bg='white')
            Label_searach.place(x=900,y=12)
            combo_search=ttk.Combobox(search_frame,justify= 'right')
            combo_search['value']=('id','name','email','phone')
            combo_search.place(x=760,y=12)
            search_entry=Entry(search_frame,textvariable=self.se_var,justify='right',bd='2')
            search_entry.place(x=620,y=12)
            se_btn=Button(search_frame,text="يبحث",bg='#3498DB',fg='white', command=self.SEA)
            se_btn.place(x=510,y=12,width=100,height=25)
# =================================عرض النتائج البيانات ===============================
            Dietals_frame=Frame(self.root,bg="#000606")
            Dietals_frame.place(x=1,y=82,width=1000,height=605)
# ==================scrools=================
            scroll_x=Scrollbar(Dietals_frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Dietals_frame,orient=VERTICAL)
# ==================treeveiw===================

            self.student_table=ttk.Treeview(Dietals_frame,
            columns=('address','gender','certil','phone','email','name','id'),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)  # صحيح

            self.student_table.place(x=8,y=1,width=1000,height=590)
            scroll_x.pack(side=BOTTOM,fill='x')
            scroll_y.pack(side=LEFT,fill='y')
            self.student_table['show']='headings'
            self.student_table.heading('address',text='عنوان الطالب')
            self.student_table.heading('gender',text='جنس الطالب')
            self.student_table.heading('certil',text='مؤهلات الطالب')
            self.student_table.heading('phone',text='رقم الهاتف')
            self.student_table.heading('email',text='البريد الالكتروني')
            self.student_table.heading('name',text='اسم الطالب')
            self.student_table.heading('id',text='الرقم التسلسلي')
            self.student_table.column('address',width=130)
            self.student_table.column('gender',width=30)
            self.student_table.column('certil',width=65)
            self.student_table.column('phone',width=65)
            self.student_table.column('email',width=70)
            self.student_table.column('name',width=100)
            self.student_table.column('id',width=18)
            
            self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_all()
# ======================================con+add=========================================
     def add_student(self):
        # إنشاء الاتصال بقاعدة البيانات
         con = pymysql.connect(
            host='localhost',
            user='root',
           passwd='',
           database='student'
          )
    
    # إنشاء كائن المؤشر
         cur = con.cursor()

    # تنفيذ الأمر SQL لإدخال البيانات
         cur.execute(
             

        "insert into student values (%s, %s, %s, %s, %s, %s, %s)",
        (
          self.id_var.get(),
          self.name_var.get(),
          self.email_var.get(),
          self.phone_var.get(),
          self.moahel_var.get(),
          self.gender_var.get(), 
          self.address_var.get()
            
        )
    )

    # تنفيذ الحفظ
         con.commit()
         self.fetch_all()
         self.clear()
    # إغلاق الاتصال
         con.close()
     def fetch_all(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='student')
        cur = con.cursor()
        cur.execute('SELECT * FROM student')
        rows = cur.fetchall()
        if len(rows) != 0:
          self.student_table.delete(*self.student_table.get_children())
          for row in rows:
            self.student_table.insert("", END, values=row)
            con.commit()
        con.close()
     

     def clear(self):

          self.id_var.set('')
          self.name_var.set('')
          self.email_var.set('')
          self.phone_var.set('')
          self.moahel_var.set('')
          self.gender_var.set('')
          self.address_var.set('') 
     
     def get_cursor(self,ev):
         cursor_row=self.student_table.focus()
         contents=self.student_table.item(cursor_row)
         row=contents['values']
         self.id_var.set(row[6])
         self.name_var.set(row[5])
         self.email_var.set(row[4])
         self.phone_var.set(row[3])
         self.moahel_var.set(row[2])
         self.gender_var.set(row[1])
         self.address_var.set(row[0])

     def apdate(self):
       con = pymysql.connect(
            host='localhost',
            user='root',
           passwd='',
           database='student'
           )
    # إنشاء كائن المؤشر
       cur = con.cursor()
    # تنفيذ الأمر SQL لإدخال البيانات
       cur.execute("update student set address=%s,gender=%s,moahel=%s,email=%s,phone=%s,name=%s, where id=%s",
        (   
          self.address_var.get()  ,
          self.gender_var.get(),
          self.moahel_var.get(),
          self.phone_var.get(),
          self.email_var.get(),
          self.name_var.get(),
          self.id_var.get()
        )
    )

    # تنفيذ الحفظ
       con.commit()
       self.fetch_all()
       self.clear()
    # إغلاق الاتصال
       con.close()        
     def search(self):
         
          con = pymysql.connect(host='localhost', user='root', password='', database='student')
          cur = con.cursor()
          cur.execute("select * from student where " +
          str(self.se_by.get())+" LIKE '%"+str(self.se_var.get())+"%'")
          rows = cur.fetchall() 
          if len(rows) != 0:
             
             self.student_table.delete(*self.student_table.get_children())
             for row in rows:
               self.student_table.insert("", END, values=row)
             con.commit()
          con.close()    

root =Tk()   
ob=student(root)
root=mainloop()  
