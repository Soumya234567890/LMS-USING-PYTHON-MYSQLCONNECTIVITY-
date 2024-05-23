from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1440x820+0+0")  ##used this geometry to give height and  width to the window.



        ##################Variables####################
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.post_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()
        ##label_title
        lbl_title=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbl_title.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1440,height=400)

        ####################################Leftframe##########################################################
        DataFrameLeft=LabelFrame(frame,text="Library Members Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=800,height=360)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        ##combobox##########
        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.member_var,width=25,state="readonly")
        comMember["values"]=("Admin Staff","Lecturer","Student")
        comMember.grid(row=0,column=1)

        ###PRNNO#######
        lblprn=Label(DataFrameLeft,bg="powder blue",text="PRN No.:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblprn.grid(row=1, column=0, sticky=W)
        ###Entrybox#############
        txtPRN_NO=Entry(DataFrameLeft, font=("times new roman",15,"bold"),textvariable=self.prn_var,width=25)
        txtPRN_NO.grid(row=1,column=1)

        ##title##
        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Id No:",padx=2,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        ###Entrybox#############
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=28)
        txtTitle.grid(row=2,column=1)

        ###FirstName###
        lblFName=Label(DataFrameLeft,font=("arial",12,"bold"),text="First Name:",padx=2,pady=6,bg="powder blue")
        lblFName.grid(row=3,column=0,sticky=W)
        ###Entrybox#############
        txtFName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=28)
        txtFName.grid(row=3,column=1)

        ##LastName###
        lblLName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Last Name:", padx=2, pady=6, bg="powder blue")
        lblLName.grid(row=4, column=0, sticky=W)
        ###Entrybox#############
        txtLName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.lastname_var,width=28)
        txtLName.grid(row=4, column=1)
        ##ADD1
        lblADD1 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address 1:", padx=2, pady=6, bg="powder blue")
        lblADD1.grid(row=5, column=0, sticky=W)
        ###Entrybox#############
        txtADD1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address1_var,width=28)
        txtADD1.grid(row=5, column=1)

        ##ADD2##
        lblADD2 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address 2:", padx=2, pady=6, bg="powder blue")
        lblADD2.grid(row=6, column=0, sticky=W)
        txtADD2 = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.address2_var, width=28)
        txtADD2.grid(row=6, column=1)

        ##Postcode###
        lblPostC = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Post Code:", padx=2, pady=6, bg="powder blue")
        lblPostC.grid(row=7, column=0, sticky=W)
        txtPostC = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.post_var, width=28)
        txtPostC.grid(row=7, column=1)

        ###MobileNO###
        lblMNO = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile No:", padx=2, pady=6, bg="powder blue")
        lblMNO.grid(row=8, column=0, sticky=W)
        txtMNO = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.mobile_var, width=28)
        txtMNO.grid(row=8, column=1)

        ##BID###
        lblBookId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Id:", padx=2, pady=6, bg="powder blue")
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.bookid_var, width=24)
        txtBookId.grid(row=0, column=3)

        ##BTitle##
        lblBookTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Title:", padx=2, pady=6, bg="powder blue")
        lblBookTitle.grid(row=1, column=2, sticky=W)
        ###Entrybox#############
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.booktitle_var, width=24)
        txtBookTitle.grid(row=1, column=3)

        ##Author##
        lblAuthor = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Author:", padx=2, pady=6, bg="powder blue")
        lblAuthor.grid(row=2, column=2, sticky=W)
        ###Entrybox#############
        txtAuthor = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.author_var ,width=24)
        txtAuthor.grid(row=2, column=3)

        ##DateBorrow##
        lblDateBorrowed  = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Borrowed:", padx=2, pady=6, bg="powder blue")
        lblDateBorrowed .grid(row=3, column=2, sticky=W)
        ###Entrybox#############
        txtDateBorrowed  = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.dateborrowed_var, width=24)
        txtDateBorrowed .grid(row=3, column=3)

        ##DateDue##
        lblDateDue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Due:", padx=2, pady=6, bg="powder blue")
        lblDateDue.grid(row=2, column=2, sticky=W)
        ###Entrybox#############
        txtDateDue = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.datedue_var, width=24)
        txtDateDue.grid(row=2, column=3)

        ##Days on book##
        lblDaysOnBook = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Days On Book:", padx=2, pady=6, bg="powder blue")
        lblDaysOnBook.grid(row=3, column=2, sticky=W)
        ###Entrybox#############
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.daysonbook_var, width=24)
        txtDaysOnBook.grid(row=3, column=3)

        ##Late Return Fine##
        lblLateFine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Late Return Fine:", padx=2, pady=6, bg="powder blue")
        lblLateFine.grid(row=4, column=2, sticky=W)
        ###Entrybox#############
        txtLateFine = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.latereturnfine_var, width=24)
        txtLateFine.grid(row=4, column=3)

        ##Date over Due##
        lbldue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Over Due:", padx=2, pady=6, bg="powder blue")
        lbldue.grid(row=5, column=2, sticky=W)
        ###Entrybox#############
        txtdue = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.dateoverdue_var,width=24)
        txtdue.grid(row=5, column=3)

        ##Actual price##
        lblActualPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Actual Price:", padx=2, pady=6, bg="powder blue")
        lblActualPrice.grid(row=6, column=2, sticky=W)
        ###Entrybox#############
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.finalprice_var, width=24)
        txtActualPrice.grid(row=6, column=3)
        ###################################rightframe##############################################
        DataFrameRight = LabelFrame(frame, text="Books Details", bg="powder blue", fg="green", bd=12,relief=RIDGE, font=("times new roman", 15, "bold"))
        DataFrameRight.place(x=810, y=5, width=540, height=360)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        listverticalScrollBar=Scrollbar(DataFrameRight)
        listhorizontalScrollBar=Scrollbar(DataFrameRight)

        listverticalScrollBar.grid(row=0,column=1,sticky="ns")
        listhorizontalScrollBar.grid(row=0, column=1,sticky="ns")
        ListBooks=["The C Programming Language", "The Mythical Man-Month", "The Code Book","Python","Clean Code","Introduction to Algorithms","The Pragmatic Programmer","Code Complete","Effective Java","Meditations","Being and Time","The Republic","Refactoring","Python Crash Course"]

        def SelectBook(event=""):
            value=str(Listbox.get(Listbox.curselection))
            x=value
            if(x=="The C Programming Language"):
                self.bookid_var.set("ISBN-13")
                self.booktitle_var.set("C Programming ")
                self.author_var.set("Dennis Ritchie")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=18)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(18)
                self.latereturnfine_var.set("Rs 2")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("RS.800")

        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listverticalScrollBar.config(command=listBox.yview)
        listhorizontalScrollBar.config(command=listBox.xview)
        for item in ListBooks:
            listBox.insert(END,item)
        ###########################################BUTTONS FRAME###########################
        FrameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameButton.place(x=0, y=530, width=1440, height=90)
        ##ADD####
        AddDataBtn=Button(FrameButton,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        AddDataBtn.grid(row=0,column=0)
        ###SHOW###
        ShowDataBtn = Button(FrameButton, text="Show Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        ShowDataBtn.grid(row=0, column=1)
        ##UPDATE###
        UpdateDataBtn = Button(FrameButton, text="Update Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        UpdateDataBtn.grid(row=0, column=2)
        ###DELETE###
        DeleteDataBtn = Button(FrameButton, text=" Delete Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        DeleteDataBtn.grid(row=0, column=3)
        ###RESET###
        ResetDataBtn = Button(FrameButton, text="Reset Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        ResetDataBtn.grid(row=0, column=4)
        ##EXIT###
        ExitDataBtn = Button(FrameButton, text="Exit Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        ExitDataBtn.grid(row=0, column=5)
        ########################################Information Frame##############################
        FrameInformation = Frame(self.root, bd=12, relief=RIDGE, padx=22, bg="powder blue")
        FrameInformation.place(x=0, y=600, width=1440, height=200)
        Table_frame= Frame(FrameInformation,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1330,height=170)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,col=("member type","prnno","title","firstname","lastname","address1",
                                                         "address2","postid","mobileno","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("member type",text="Member Type:")
        self.library_table.heading("prnno", text="Prn No:")
        self.library_table.heading("title", text="Title:")
        self.library_table.heading("firstname", text="First Name:")
        self.library_table.heading("lastname", text="Last Name:")
        self.library_table.heading("address1", text="Address 1:")
        self.library_table.heading("address2", text="Address 2:")
        self.library_table.heading("postid", text="Post Id:")
        self.library_table.heading("mobileno", text="Mobile No:")
        self.library_table.heading("bookid", text="Book Id:")
        self.library_table.heading("booktitle", text="Book Title:")
        self.library_table.heading("author", text="Author:")
        self.library_table.heading("dateborrowed",text="Date Borrowed:")
        self.library_table.heading("datedue", text="Date Due:")
        self.library_table.heading("days", text="Days:")
        self.library_table.heading("latereturnfine", text="Late Return Fine:")
        self.library_table.heading("dateoverdue", text="Date Over Due:")
        self.library_table.heading("finalprice", text="Final Price:")
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        ##setting up width####
        self.library_table.column("member type",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobileno",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        self.library_table.column("dateborrowed",width=100)
##########ADD DATA FUNCTION#############

def adda_data(self):
    connection=mysql.connector.connect(host="localhost",username="root",password="Soumya@123",database="librarymanagementsystem")
    my_cursor=connection.cursor()
    my_cursor.execute("insert into lib values(%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S)",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.post_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get(),
    connection.commit(),
        connection.close(),


    messagebox.showinfo("Success", "Memberr has been inserted successfully")
    ))
if __name__ == '__main__':
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()     ##used to demonstrate the window

