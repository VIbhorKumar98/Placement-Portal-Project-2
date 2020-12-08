from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import mysql.connector as mysql

class InsertCompanyValue():
    @staticmethod
    def insertvals(Nameentry, Addressentry, Turnoverentry, Businessentry, Profileentry, Salaryentry, Roundsentry, MinPercentageentry, MaxFailedentry,Degreeentry,Timeentry,Dateentry, VenueofExamentry, AptitudeRoundentry,CodingRoundentry, TechnicalInterviewentry,HRInterviewentry):
        name = Nameentry.get()
        address = Addressentry.get()
        turnover = Turnoverentry.get()
        business = Businessentry.get()
        profile = Profileentry.get()
        salary = Salaryentry.get()
        rounds = Roundsentry.get()
        percentage = MinPercentageentry.get()
        FailedSub = MaxFailedentry.get()
        QualificationDegree=Degreeentry.get()
        time = Timeentry.get()
        date=Dateentry.get()
        venue = VenueofExamentry.get()
        AptitudeRound=AptitudeRoundentry.get()
        CodingRound=CodingRoundentry.get()
        TechnicalInterview=TechnicalInterviewentry.get()
        HRInterview=HRInterviewentry.get()

        #if(name == "" or business == "" or salary==""):
        #    messagebox.showinfo("Insert Status", "Fields are required")
        #else:
        con = mysql.connect(host="localhost", user="root", password="Password123#@!", database="Project")
        cursor = con.cursor()
        cursor.execute("insert into Company values('"+name+"','"+address+"','"+turnover+"','"+business+"','"+profile+"','"+salary+"','"+rounds+"','"+percentage+"','"+FailedSub+"','"+QualificationDegree+"','"+time+"','"+date+"','"+venue+"','"+AptitudeRound+"','"+CodingRound+"','"+TechnicalInterview+"', '"+HRInterview+"')")
        cursor.execute("commit")

        messagebox.showinfo("Company Record Insert status","Inserted Successfully")
        con.close()

class studentInsertVal():
    @staticmethod
    def StudentInsert(StudentIDentry, StudentNameentry, Marksentry, MaxFailedentry):
        SID = StudentIDentry.get()
        StudentName = StudentNameentry.get()
        Percentage = Marksentry.get()
        FailedSub = MaxFailedentry.get()

        con = mysql.connect(host="localhost", user="root", password="Password123#@!", database="Project")
        cursor = con.cursor()

        cursor.execute("insert into Student values('"+SID+"','"+StudentName+"','"+Percentage+"','"+FailedSub+"')")
        cursor.execute("commit")

        messagebox.showinfo("Student Record Insert status","Inserted Successfully")
        con.close()

class MtechInsertVal():
    @staticmethod
    def TheseInsert(StudentIDentry, StudentNameentry, ThesisWorkentry):
        SID = StudentIDentry.get()
        StudentName = StudentNameentry.get()
        TheseWork = ThesisWorkentry.get()

        con = mysql.connect(host="localhost", user="root", password="Password123#@!", database="Project")
        cursor = con.cursor()

        cursor.execute("insert into ThesisWork values('"+SID+"','"+StudentName+"','"+TheseWork+"')")
        cursor.execute("commit")

        messagebox.showinfo("Student Record Insert status","Inserted Successfully")
        con.close()


class ShowOffer():
    @staticmethod
    def ShowOfferTable(SIDentry):
        StudentID = SIDentry.get();

        ofwin=Tk()
        ofwin.geometry("650x500")
        ofwin.title("Congratulationts, YOU HAVE SELECTED FOR THESE COMPANIES!!!")

        fr = Frame(ofwin)
        fr.pack(side=tk.LEFT, padx=20)
        oftv = ttk.Treeview(ofwin, columns=(1,2),show = "headings")

        oftv.heading("1", text ="Company Name")
        oftv.heading("2", text ="Job Location")
        con = mysql.connect(host="localhost", user="root", password="Password123#@!", database="Project")
        cursor = con.cursor()

        sql ="""Select CompanyName, JobLocation from Selected where (SID=%s)"""
        cursor.execute(sql, (StudentID,))
        nrows= cursor.fetchall()

        for i in nrows:
            oftv.insert("","end", values=i)
        oftv.pack()
        ofwin.mainloop()

class ShowCompany():
    @staticmethod
    def ShowCompanyTable(Percentageentry, FailedSubentry):
        Score = Percentageentry.get()
        MaxFailed=FailedSubentry.get()

        cwin=Tk()
        cwin.geometry("650x500")
        cwin.title("List of Companies")

        fr = Frame(cwin)
        fr.pack(side=tk.LEFT, padx=20)
        ctv = ttk.Treeview(cwin, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14),show = "headings")

        ctv.heading("1", text ="Name")
        ctv.heading("2", text ="Address")
        ctv.heading("3", text ="TurnOver")
        ctv.heading("4", text ="Business Area")
        ctv.heading("5", text ="Profile")
        ctv.heading("6", text ="Salary")
        ctv.heading("7", text ="No of Rounds")
        ctv.heading("8", text ="Time")
        ctv.heading("9", text ="Date")
        ctv.heading("10", text ="Venue")
        ctv.heading("11", text ="Aptitude Rounds")
        ctv.heading("12", text ="Coding Rounds")
        ctv.heading("13", text ="Technical Interviews")
        ctv.heading("14", text ="HR Rounds")

        con = mysql.connect(host="localhost", user="root", password="Password123#@!", database="Project")
        cursor = con.cursor()

        sql ="""Select name,address,turnover,business,profile,salary,Rounds,time,date,venue,AptitudeRound,CodingRound,TechnicalInterview,HRInterview from Company where (Percentage<=%s) AND (FailedSub>=%s)"""
        cursor.execute(sql, (Score, MaxFailed))
        nrows= cursor.fetchall()

        for i in nrows:
            ctv.insert("","end", values=i)

        ctv.pack()
        cwin.mainloop()




class Existing():
    @staticmethod
    def ExistingStudent():
        st=Tk()
        st.geometry("330x333")
        st.title("Check the companies you're eligible for!")
        SID = Label(st,text="Your Student ID:", font=("Times",12),fg='blue')
        Percentage = Label(st,text="Enter Your Percentage:", font=("Times",12),fg='blue')
        FailedSub = Label(st,text="Enter Failed Subjects:", font=("Times",12),fg='blue')

        SID.grid(row=19, column=10)
        Percentage.grid(row=20,column=10)
        FailedSub.grid(row=21,column=10)

        SID=StringVar()
        Percentage=StringVar()
        FailedSub=StringVar()

        SIDentry=Entry(st,textvariable=SID)
        Percentageentry=Entry(st,textvariable=Percentage)
        FailedSubentry=Entry(st, textvariable=FailedSub)

        SIDentry.grid(row=19, column=11)
        Percentageentry.grid(row=20,column=11)
        FailedSubentry.grid(row=21, column=11)

        Button(st, text="Submit", command=lambda: ShowCompany.ShowCompanyTable(Percentageentry, FailedSubentry)).grid(row=22, column=10)
        Button(st, text="Click Here to see your offers!!", command=lambda: ShowOffer.ShowOfferTable(SIDentry)).grid(row=23, column=10)

class NewRegistrationStudent():
    @staticmethod
    def NewRegistration():
        st = Tk()
        st.geometry("655x333")
        st.maxsize(1200, 1000)
        st.minsize(250, 250)
        st.title("Welcome to the Student portal!!")
        Label(st, text="Please Enter your information", font = ('Times', 15), fg = 'blue').grid(row=0, column=1)

        StudentID = Label(st, text="Student ID", font=('bold',10))
        StudentName = Label(st, text="Student Name", font=('bold',10))
        Marks = Label(st, text="Marks", font=('bold',10))
        MaxFailed = Label(st, text="Max Failed Subjects", font=('bold',10))

        StudentID.grid(row=1, column=0)
        StudentName.grid(row=2, column=0)
        Marks.grid(row=3, column=0)
        MaxFailed.grid(row=4, column=0)

        StudentID = StringVar()
        StudentName = StringVar()
        Marks = StringVar()
        MaxFailed = StringVar()

        StudentIDentry = Entry(st, textvariable = StudentID)
        StudentNameentry = Entry(st, textvariable = StudentName)
        Marksentry = Entry(st, textvariable = Marks)
        MaxFailedentry = Entry(st, textvariable = MaxFailed)

        StudentIDentry.grid(row=1, column=1)
        StudentNameentry.grid(row=2, column=1)
        Marksentry.grid(row=3, column=1)
        MaxFailedentry.grid(row=4, column=1)

        Button(st,text="Submit!!", command=lambda: studentInsertVal.StudentInsert(StudentIDentry, StudentNameentry, Marksentry, MaxFailedentry)).grid(row=5, column=1)

#For Mtech students these work
class ForMtech:
    @staticmethod
    def NewRegistration():
        stForMtech = Tk()
        stForMtech.geometry("655x333")
        stForMtech.maxsize(1200, 1000)
        stForMtech.minsize(250, 250)
        stForMtech.title("Enter Information about your these work!!")
        Label(stForMtech, text="Please Enter your information", font = ('Times', 15), fg = 'blue').grid(row=0, column=1)

        StudentID = Label(stForMtech, text="Student ID", font=('bold',10))
        StudentName = Label(stForMtech, text="Student Name", font=('bold',10))
        ThesisWork = Label(stForMtech, text="Thesis Area", font=('bold',10))

        StudentID.grid(row=1, column=0)
        StudentName.grid(row=2, column=0)
        ThesisWork.grid(row=3, column=0)

        StudentID = StringVar()
        StudentName = StringVar()
        ThesisWork = StringVar()

        StudentIDentry = Entry(stForMtech, textvariable = StudentID)
        StudentNameentry = Entry(stForMtech, textvariable = StudentName)
        ThesisWorkentry = Entry(stForMtech, textvariable = ThesisWork)

        StudentIDentry.grid(row=1, column=1)
        StudentNameentry.grid(row=2, column=1)
        ThesisWorkentry.grid(row=3, column=1)

        Button(stForMtech,text="Submit!!", command=lambda: MtechInsertVal.TheseInsert(StudentIDentry, StudentNameentry, ThesisWorkentry)).grid(row=5, column=1)

class Student:

    def __init__(self, str):
        self.initstr = str

    def Stud(self):
        print("welcome to the IIIT Delhi!!")

class StudentBTech(Student):
    def __init(self, str1):
        self.initstr = str1
        super().__init__(str1)


    def Stud(self):
        st=Tk()
        st.geometry("300x333")
        st.title(self.initstr)
        Label(st, text="Click one of the following", font=('Times', 17), fg='blue').grid(row=8, column=10)
        Button(st, text="Already registered? Click here",command=Existing.ExistingStudent).grid(row=50, column=10)
        Button(st, text="New Registration",command=NewRegistrationStudent.NewRegistration).grid(row=100, column=10)

class StudentMTech(Student):
    def __init(self, str1):
        self.initstr = str1
        super().__init__(str1)

    def Stud(self):
        st=Tk()
        st.geometry("300x333")
        st.title(self.initstr)
        Label(st, text="Click one of the following", font=('Times', 17), fg='blue').grid(row=8, column=10)
        Button(st, text="Already registered? Click here",command=Existing.ExistingStudent).grid(row=50, column=10)
        Button(st, text="New Registration",command=NewRegistrationStudent.NewRegistration).grid(row=100, column=10)
        Button(st, text="Choose your these work",command=ForMtech.NewRegistration).grid(row=150, column=10)




class InsertShortlisted():
    @staticmethod
    def SelectInsert(StudentIDentry, StudentNameentry, CompanyNameentry, JobLocationentry):
        SID = StudentIDentry.get()
        StudentName = StudentNameentry.get()
        CompanyName = CompanyNameentry.get()
        JobLocation = JobLocationentry.get()

        con = mysql.connect(host="localhost", user="root", password="Password123#@!", database="Project")
        cursor = con.cursor()

        cursor.execute("insert into Selected values('"+SID+"','"+StudentName+"','"+CompanyName+"','"+JobLocation+"')")
        cursor.execute("commit")

        messagebox.showinfo("Thank you for visiting the campus", "Thank you")
        con.close()

class ShortlistStudent():
    @staticmethod
    def Select():
        sf = Tk()
        sf.geometry("655x333")
        sf.maxsize(1200, 1000)
        sf.minsize(250, 250)
        sf.title("Thank you for visiting the campus!")
        Label(sf, text="Please Enter The Selected Candidates!", font = ('Times', 15), fg = 'blue').grid(row=0, column=1)

        StudentID = Label(sf, text="Student ID", font=('bold',10))
        StudentName = Label(sf, text="Student Name", font=('bold',10))
        CompanyName = Label(sf, text="Company Name", font=('bold',10))
        JobLocation = Label(sf, text="Job Location", font=('bold',10))

        StudentID.grid(row=1, column=0)
        StudentName.grid(row=2, column=0)
        CompanyName.grid(row=3, column=0)
        JobLocation.grid(row=4, column=0)

        StudentIDentry = Entry(sf, textvariable = StudentID)
        StudentNameentry = Entry(sf, textvariable = StudentName)
        CompanyNameentry = Entry(sf, textvariable = CompanyName)
        JobLocationentry = Entry(sf, textvariable = JobLocation)

        StudentIDentry.grid(row=1, column=1)
        StudentNameentry.grid(row=2, column=1)
        CompanyNameentry.grid(row=3, column=1)
        JobLocationentry.grid(row=4, column=1)

        Button(sf,text="Submit!!", command=lambda: InsertShortlisted.SelectInsert(StudentIDentry, StudentNameentry, CompanyNameentry, JobLocationentry)).grid(row=5, column=1)



class ShowStudent():
    @staticmethod
    def ShowStudentTable(Percentageentry, FailedSubjectentry):
        Score = Percentageentry.get()
        MaxFailed=FailedSubjectentry.get()

        stwin=Tk()
        stwin.geometry("650x500")
        stwin.title("List of Students")

        fr = Frame(stwin)
        fr.pack(side=tk.LEFT, padx=20)

        sttv = ttk.Treeview(stwin, columns=(1,2,3,4,5),show = "headings")

        sttv.heading("1", text ="Student ID")
        sttv.heading("2", text ="Name")
        sttv.heading("3", text ="Percentage")
        sttv.heading("4", text ="FailedSub")

        con = mysql.connect(host="localhost", user="root", password="Password123#@!", database="Project")
        cursor = con.cursor()

        sql ="""Select * from Student where (Percentage>=%s) AND (FailedSub<=%s)"""
        cursor.execute(sql, (Score, MaxFailed))
        nrows= cursor.fetchall()

        for i in nrows:
            sttv.insert("","end", values=i)
        sttv.pack()
        stwin.mainloop()


class CompanyEligibilityCheck():
    @staticmethod
    def EligibilityCheck():
        check=Tk()
        check.geometry("300x333")
        check.title("Welcome!")
        Label(check, text="Check Eligibile Candidates", font=('Times', 17), fg='blue').grid(row=8, column=1)
        Percentage = Label(check, text="Percentage", font=('bold',10))
        FailedSubject = Label(check, text="Failed Subjects", font=('bold',10))

        Percentage.grid(row=15, column=0)
        FailedSubject.grid(row=16, column=0)

        Percentage = StringVar()
        FailedSubject = StringVar()

        Percentageentry = Entry(check, textvariable = Percentage)
        FailedSubjectentry = Entry(check, textvariable = FailedSubject)


        Percentageentry.grid(row=15, column=1)
        FailedSubjectentry.grid(row=16, column=1)

        Button(check, text="Click here to check!!",command=lambda: ShowStudent.ShowStudentTable(Percentageentry, FailedSubjectentry)).grid(row=17, column=1)
        Button(check, text="Select Final Selected Students", command=ShortlistStudent.Select).grid(row=18, column=1)

class Company:
    def __init__(self, str):
        self.str = str

    def Comp(self):
        print("Welcome to the IIIT Delhi World!!")


#For Domestic Offers
class CompanyForDomestic(Company):
    def __init__(self, str1):
        self.str = str1
        super().__init__(str1)

    def Comp(self):
        root = Tk()
        root.geometry("655x333")
        root.maxsize(1200, 1000)
        root.minsize(250, 250)
        root.title(self.str)
        Label(root, text="Please Enter The Information about the company", font = ('Times', 15), fg = 'blue').grid(row=0, column=1)

        companyName = Label(root, text="Company Name", font=('bold',10))
        CompanyAddress = Label(root, text="Address:", font=('bold',10))
        CompanyTurnover = Label(root, text="Turnover", font=('bold',10))
        BusinessArea = Label(root, text="Business Area", font=('bold',10))
        ProfileName = Label(root, text="Profile Name", font=('bold',10))
        SalaryInRupee  = Label(root, text="Salary Offered In Rupee", font=('bold',10))
        Rounds = Label(root, text="No of Rounds to Conduct", font=('bold',10))
        MinPercentage = Label(root, text="Minimum Percentage Needed", font=('bold',10))
        MaxFailed = Label(root, text="Maximum Failed Subjects Allowed", font=('bold',10))
        Degree = Label(root, text="Qualification/Eligible Degree", font=('bold',10))
        TimeOfExam = Label(root, text="Time of Conducting Exam", font=('bold', 10))
        DateOfExam = Label(root, text="Date of Conducting Exam", font=('bold', 10))
        VenueOfExam = Label(root, text="Venue of Conducting Exam", font=('bold', 10))
        AptitudeRound = Label(root, text="No of Aptitude Rounds", font=('bold', 10))
        CodingRound = Label(root, text="No of Coding Rounds", font=('bold', 10))
        TechnicalInterview = Label(root, text="No of Technical Interviews", font=('bold', 10))
        HRInterview = Label(root, text="No of HR Rounds", font=('bold', 10))

        companyName.grid(row=1, column=0)
        CompanyAddress.grid(row=2, column=0)
        CompanyTurnover.grid(row=3, column=0)
        BusinessArea.grid(row=4, column=0)
        ProfileName.grid(row=5, column=0)
        SalaryInRupee.grid(row=6, column=0)
        Rounds.grid(row=7, column=0)
        MinPercentage.grid(row=8, column=0)
        MaxFailed.grid(row=9, column=0)
        Degree.grid(row=10, column=0)
        TimeOfExam.grid(row=11, column=0)
        DateOfExam.grid(row=12,column=0)
        VenueOfExam.grid(row=13, column=0)
        AptitudeRound.grid(row=14, column=0)
        CodingRound.grid(row=15, column=0)
        TechnicalInterview.grid(row=16, column=0)
        HRInterview.grid(row=17, column=0)
        # Variable classes in tkinter
        # BooleanVar, DoubleVar, IntVar, StringVar

        companyName = StringVar()
        CompanyAddress = StringVar()
        CompanyTurnover = StringVar()
        BusinessArea = StringVar()
        ProfileName= StringVar()
        SalaryInRupee= StringVar()
        Rounds= StringVar()
        MinPercentage= StringVar()
        MaxFailed= StringVar()
        Degree=StringVar()
        TimeOfExam=StringVar()
        DateOfExam=StringVar()
        VenueOfExam=StringVar()
        AptitudeRound=StringVar()
        CodingRound=StringVar()
        TechnicalInterview=StringVar()
        HRInterview=StringVar()

        Nameentry = Entry(root, textvariable = companyName)
        Addressentry = Entry(root, textvariable = CompanyAddress)
        Turnoverentry = Entry(root, textvariable = CompanyTurnover)
        Businessentry = Entry(root, textvariable = BusinessArea)
        Profileentry = Entry(root, textvariable = ProfileName)
        SalaryInRupeeentry = Entry(root, textvariable = SalaryInRupee)
        Roundsentry = Entry(root, textvariable = Rounds)
        MinPercentageentry = Entry(root, textvariable = MinPercentage)
        MaxFailedentry = Entry(root, textvariable = MaxFailed)
        Degreeentry = Entry(root, textvariable = Degree)
        Timeentry=Entry(root,textvariable = TimeOfExam)
        Dateentry=Entry(root,textvariable = DateOfExam)
        VenueofExamentry=Entry(root,textvariable = VenueOfExam)
        AptitudeRoundentry=Entry(root,textvariable = AptitudeRound)
        CodingRoundentry=Entry(root,textvariable = CodingRound)
        TechnicalInterviewentry=Entry(root,textvariable = TechnicalInterview)
        HRInterviewentry=Entry(root,textvariable = HRInterview)

        Nameentry.grid(row=1, column=1)
        Addressentry.grid(row=2, column=1)
        Turnoverentry.grid(row=3, column=1)
        Businessentry.grid(row=4, column=1)
        Profileentry.grid(row=5, column=1)
        SalaryInRupeeentry.grid(row=6, column=1)
        Roundsentry.grid(row=7, column=1)
        MinPercentageentry.grid(row=8, column=1)
        MaxFailedentry.grid(row=9, column=1)
        Degreeentry.grid(row=10, column=1)
        Timeentry.grid(row=11,column=1)
        Dateentry.grid(row=12,column=1)
        VenueofExamentry.grid(row=13,column=1)
        AptitudeRoundentry.grid(row=14,column=1)
        CodingRoundentry.grid(row=15,column=1)
        TechnicalInterviewentry.grid(row=16,column=1)
        HRInterviewentry.grid(row=17,column=1)

        Button(root,text="Submit!!", command=lambda: InsertCompanyValue.insertvals(Nameentry, Addressentry, Turnoverentry, Businessentry, Profileentry, SalaryInRupeeentry, Roundsentry, MinPercentageentry, MaxFailedentry,Degreeentry,Timeentry,Dateentry, VenueofExamentry, AptitudeRoundentry,CodingRoundentry, TechnicalInterviewentry,HRInterviewentry)).grid(row=18, column=1)
        Button(root, text="Check Eligible Candidates!!", command=CompanyEligibilityCheck.EligibilityCheck).grid(row=19, column=1)
        root.mainloop()

#For International Offers
class CompanyForInternational(Company):
    def __init__(self, str1):
        self.str = str1
        super().__init__(str1)

    def Comp(self):
        root = Tk()
        root.geometry("655x333")
        root.maxsize(1200, 1000)
        root.minsize(250, 250)
        root.title(self.str)
        Label(root, text="Please Enter The Information about the company", font = ('Times', 15), fg = 'blue').grid(row=0, column=1)

        companyName = Label(root, text="Company Name", font=('bold',10))
        CompanyAddress = Label(root, text="Address:", font=('bold',10))
        CompanyTurnover = Label(root, text="Turnover", font=('bold',10))
        BusinessArea = Label(root, text="Business Area", font=('bold',10))
        ProfileName = Label(root, text="Profile Name", font=('bold',10))
        SalaryInDollars  = Label(root, text="Salary Offered In Dollars", font=('bold',10))
        Rounds = Label(root, text="No of Rounds to Conduct", font=('bold',10))
        MinPercentage = Label(root, text="Minimum Percentage Needed", font=('bold',10))
        MaxFailed = Label(root, text="Maximum Failed Subjects Allowed", font=('bold',10))
        Degree = Label(root, text="Qualification/Eligible Degree", font=('bold',10))
        TimeOfExam = Label(root, text="Time of Conducting Exam", font=('bold', 10))
        DateOfExam = Label(root, text="Date of Conducting Exam", font=('bold', 10))
        VenueOfExam = Label(root, text="Venue of Conducting Exam", font=('bold', 10))
        AptitudeRound = Label(root, text="No of Aptitude Rounds", font=('bold', 10))
        CodingRound = Label(root, text="No of Coding Rounds", font=('bold', 10))
        TechnicalInterview = Label(root, text="No ofCallMtech Technical Interviews", font=('bold', 10))
        HRInterview = Label(root, text="No of HR Rounds", font=('bold', 10))

        companyName.grid(row=1, column=0)
        CompanyAddress.grid(row=2, column=0)
        CompanyTurnover.grid(row=3, column=0)
        BusinessArea.grid(row=4, column=0)
        ProfileName.grid(row=5, column=0)
        SalaryInDollars.grid(row=6, column=0)
        Rounds.grid(row=7, column=0)
        MinPercentage.grid(row=8, column=0)
        MaxFailed.grid(row=9, column=0)
        Degree.grid(row=10, column=0)
        TimeOfExam.grid(row=11, column=0)
        DateOfExam.grid(row=12,column=0)
        VenueOfExam.grid(row=13, column=0)
        AptitudeRound.grid(row=14, column=0)
        CodingRound.grid(row=15, column=0)
        TechnicalInterview.grid(row=16, column=0)
        HRInterview.grid(row=17, column=0)
        # Variable classes in tkinter
        # BooleanVar, DoubleVar, IntVar, StringVar

        companyName = StringVar()
        CompanyAddress = StringVar()
        CompanyTurnover = StringVar()
        BusinessArea = StringVar()
        ProfileName= StringVar()
        SalaryInDollars= StringVar()
        Rounds= StringVar()
        MinPercentage= StringVar()
        MaxFailed= StringVar()
        Degree=StringVar()
        TimeOfExam=StringVar()
        DateOfExam=StringVar()
        VenueOfExam=StringVar()
        AptitudeRound=StringVar()
        CodingRound=StringVar()
        TechnicalInterview=StringVar()
        HRInterview=StringVar()

        Nameentry = Entry(root, textvariable = companyName)
        Addressentry = Entry(root, textvariable = CompanyAddress)
        Turnoverentry = Entry(root, textvariable = CompanyTurnover)
        Businessentry = Entry(root, textvariable = BusinessArea)
        Profileentry = Entry(root, textvariable = ProfileName)
        SalaryInDollarsentry = Entry(root, textvariable = SalaryInDollars)
        Roundsentry = Entry(root, textvariable = Rounds)
        MinPercentageentry = Entry(root, textvariable = MinPercentage)
        MaxFailedentry = Entry(root, textvariable = MaxFailed)
        Degreeentry = Entry(root, textvariable = Degree)
        Timeentry=Entry(root,textvariable = TimeOfExam)
        Dateentry=Entry(root,textvariable = DateOfExam)
        VenueofExamentry=Entry(root,textvariable = VenueOfExam)
        AptitudeRoundentry=Entry(root,textvariable = AptitudeRound)
        CodingRoundentry=Entry(root,textvariable = CodingRound)
        TechnicalInterviewentry=Entry(root,textvariable = TechnicalInterview)
        HRInterviewentry=Entry(root,textvariable = HRInterview)

        Nameentry.grid(row=1, column=1)
        Addressentry.grid(row=2, column=1)
        Turnoverentry.grid(row=3, column=1)
        Businessentry.grid(row=4, column=1)
        Profileentry.grid(row=5, column=1)
        SalaryInDollarsentry.grid(row=6, column=1)
        Roundsentry.grid(row=7, column=1)
        MinPercentageentry.grid(row=8, column=1)
        MaxFailedentry.grid(row=9, column=1)
        Degreeentry.grid(row=10, column=1)
        Timeentry.grid(row=11,column=1)
        Dateentry.grid(row=12,column=1)
        VenueofExamentry.grid(row=13,column=1)
        AptitudeRoundentry.grid(row=14,column=1)
        CodingRoundentry.grid(row=15,column=1)
        TechnicalInterviewentry.grid(row=16,column=1)
        HRInterviewentry.grid(row=17,column=1)

        Button(root,text="Submit!!", command=lambda: InsertCompanyValue.insertvals(Nameentry, Addressentry, Turnoverentry, Businessentry, Profileentry, SalaryInDollarsentry, Roundsentry, MinPercentageentry, MaxFailedentry,Degreeentry,Timeentry,Dateentry, VenueofExamentry, AptitudeRoundentry,CodingRoundentry, TechnicalInterviewentry,HRInterviewentry)).grid(row=18, column=1)
        Button(root, text="Check Eligible Candidates!!", command=CompanyEligibilityCheck.EligibilityCheck).grid(row=19, column=1)
        root.mainloop()

class ChooseStream:

    def choose(self):
        ch = Tk()
        ch.geometry("655x333")
        ch.maxsize(250, 250)
        ch.minsize(250, 250)
        ch.title("welcome")
        Label(ch,text="Choose your Degree course",bd=1,font='Times 11',fg='blue',padx=20).place(x=-20,y=10)
        Label(ch, text="Enter As: ", font=('Times', 10), fg='magenta').place(x=40,y=50)
        Button(ch, text="MTech", command=self.CallMtech).place(x=40,y=80)

        Button(ch, text="BTech.", command=self.CallBtech).place(x=40,y=120)

    def CallBtech(self):
        stBtech = StudentBTech("Portal for Btech students!!")
        stBtech.Stud()

    def CallMtech(self):
        stMtech = StudentMTech("Portal for Mtech students!!")
        stMtech.Stud()

class ChooseCompanyType:

    def CompanyType(self):
        chCompany = Tk()
        chCompany.geometry("655x333")
        chCompany.maxsize(250, 250)
        chCompany.minsize(250, 250)
        chCompany.title("welcome")
        Label(chCompany,text="International or Domestic?",bd=1,font='Times 11',fg='blue',padx=20).place(x=-20,y=10)
        Label(chCompany, text="Enter As: ", font=('Times', 10), fg='magenta').place(x=40,y=50)
        Button(chCompany, text="For Domestic Offer", command=self.CallCompanyForDomestic).place(x=40,y=80)

        Button(chCompany, text="For International Offer.", command=self.CallCompanyForInternational).place(x=40,y=120)

    def CallCompanyForInternational(self):
        cpInternational = CompanyForInternational("Welcome to the International Company portal!!")
        cpInternational.Comp()

    def CallCompanyForDomestic(self):
        cpDomestic = CompanyForDomestic("Welcome to the Domestic Company portal!!")
        cpDomestic.Comp()


class RecruitmentProcess:

    def __init__(self, win):
        win.geometry("655x333")
        win.maxsize(250, 250)
        win.minsize(250, 250)
        win.title("welcome")
        Label(win,text="Welcome to the College Placement Portal",bd=1,font='Times 11',fg='blue',padx=20).place(x=-20,y=10)
        Label(win, text="Enter As: ", font=('Times', 10), fg='magenta').place(x=40,y=50)
        Button(win, text="Company", command=self.callChooseCompanyType).place(x=40,y=80)

        Button(win, text="Student", command=self.callChooseStream).place(x=40,y=120)

    def callChooseStream(self):
        objChoose = ChooseStream()
        objChoose.choose()

    def callChooseCompanyType(self):
        objChooseCompany = ChooseCompanyType()
        objChooseCompany.CompanyType()

    #def Company(self):
    #    print("company")

    #def Stud(self):
    #    print("stud")


if __name__ == "__main__":
    # execute only if run as a script
    root = Tk()
    recruit = RecruitmentProcess(root)
    root.mainloop()
