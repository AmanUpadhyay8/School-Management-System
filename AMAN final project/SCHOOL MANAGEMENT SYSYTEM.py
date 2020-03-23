"""*****************************************************************************
                            MODULES USED IN PROJECT
*****************************************************************************"""
import pickle
import os
"""*****************************************************************************
                           studata CLASS USED IN PROJECT
*****************************************************************************"""

class studata(object):
    def __init__(s):
        s.admno=0
        s.roll=0
        s.name=""
        s.fname=""
        s.mname=""
        s.dob=""
        s.sclass=0
        s.sec=""

    def create_studata(s):  #function to get data from user
        s.admno=int(input("\nEnter admission number number: "))
        name=input("\n\nEnter the name of the student: ")
        s.name=name.upper()
        mname=input("\nName of Mother: ")
        s.mname=mname.upper()
        fname=input("\nName of Father: ")
        s.fname=fname.upper()
        s.dob=input("\nEnter date of birth: ")
        
    def show_studata(s):    #function to show data on screen
        print( "\nAdmission No.: ", s.admno)
        print( "\nStudent name: ", s.name)
        print( "\nMother's Name: ", s.mname)
        print( "\nFather's Name: ", s.fname)
        print( "\nDate of Birth: ", s.dob)

    def modify(s):           #function to get new data from user
        print( "\nAdmission No.: ", s.admno)
        name=input("\n\nEnter the name of the student: ")
        s.name=name.upper()
        mname=input("\nName of Mother: ")
        s.mname=mname.upper()
        fname=input("\nName of Father: ")
        s.fname=fname.upper()
        dob=input("\nEnter date of birth: ")


    def report(s):           #function to show data in tabular format
        print( "%-15s"%s.admno,"%-20s"%s.name.strip(),"%-20s"%s.mname,"%-20s"%s.fname,"%-20s"%s.dob)

    def retadmno(s):          #function to return account number
        return s.admno

    def retfname(s):      #function to return balance amount 
        return s.fname

    def retmname(s):         #function to return type of account
        return s.mname
    
"""*****************************************************************************
                           feedata CLASS USED IN PROJECT
*****************************************************************************"""
class  feedata(object):
    def  __init__(s):
        s.trno=0
        s.admno=0
        s.name=""
        s.fmonth=""
        s.famt=0
        s.date=""

            
    def getFeeData(s): 
        flag=0
        try:
            inFile=open("student.dat","rb")
            n=int(input("Enter the Admission number: "))
            while True:
                stu=pickle.load(inFile)
                if stu.retadmno()==n:
                    s.trno=int(input("\nEnter Transaction number: "))
                    s.admno=n
                    s.name=stu.name
                    fm=input("\nEnter the fee quarter: ")
                    s.fmonth=fm.upper()
                    s.famt=int(input("\nEnter the fee of the student: "))
                    s.date=input("\nEnter the fee date: ")
                    flag=1
        except EOFError:
            inFile.close()
            if flag==0:
                print( "\n Admission number not exist ")
            return flag
        except IOError:
            print( " studata.dat : File could not be open !! Press any Key...")
        return flag
    
    def show_feedata(s):
        print("\nTransaction number: ",s.trno)
        print("\nAdmission No.: ", s.admno)
        print("\nStudent name: ", s.name)
        print("\nFee Quarter: ",s.fmonth)
        print("\nFee Amount: ",s.famt)
        print("\nFee Date: ",s.date)

    def modify(s):
        print("\nTransaction number: ",s.trno)
        s.admno=int(input("\nEnter admission  number: "))
        name=input("\nEnter the name of the student: ")
        s.name=name.upper() 
        fm=input("\nEnter the fee quarter: ")
        s.fmonth=fm.upper()
        s.famt=int(input("\nEnter the fee of the student: "))
        s.date=input("\nEnter the fee date: ")

    def report(s):          #function to show data in tabular format
        print( "%-10s"%s.trno,"%-20s"%s.name,"%-10s"%s.fmonth,"%-6s"%s.famt)
        
    def rettrno(s):
        return s.trno

    def retadmno(s):
        return s.admno

    def retname(s):
        return s.name

    def retfmonth(s):
        return s.fmonth

    def retfamt(s):
        return s.famt

    def retdate(s):
        return s.date
    
#*****************************************************************************
#          FUNCTION TO WRITE RECORD IN BINARY FILE
#*****************************************************************************
def write_studata():
    try:
        st=studata()
        outFile=open("student.dat","ab") 
        st.create_studata()
        pickle.dump(st,outFile)
        outFile.close()
        print( "\n\n Student details added Successfully")
        print( "\n\n YOUR ADMISSION NUMBER IS: ",st.retadmno())
    except:
        pass

def write_feedata():
    try:
        fe=feedata()
        outFile=open("feedata.dat","ab") 
        flag=fe.getFeeData()
        if flag==1:
            pickle.dump(fe,outFile)
            print( "\n\n FEEDATA CREATED SUCCESSFULLY")
            print( "\n\n YOUR TRANSACTION NUMBER IS: ",fe.rettrno())
        outFile.close()
        
    except:
        pass

"""*****************************************************************************
                FUNCTION TO DISPLAY STUDENT DETAILS GIVEN BY USER
*****************************************************************************"""

def display_studata(n):
    flag=0
    try:
        inFile=open("student.dat","rb")
        print( "\nSTUDENT DETAILS\n")
        while True:
            st=pickle.load(inFile)
            if st.retadmno()==n:
                st.show_studata()
                flag=1
    except EOFError:
        inFile.close()
        if flag==0:
            print( "\n\n student data not exist ")
    except IOError:
        print( "File could not be open !! Press any Key...")

"""*****************************************************************************
                FUNCTION TO DISPLAY FEE DETAILS GIVEN BY USER
*****************************************************************************"""
def display_feedata(n):
    flag=0
    try:
        inFile=open("feedata.dat","rb")
        print( "\nFEE DETAILS\n")
        while True:
            fe=pickle.load(inFile)
            if fe.rettrno()==n:
                fe.show_feedata()
                flag=1
    except EOFError:
        inFile.close
        if flag==0:
            print( "\n\nTHIS TRANSACTION NUMBER DOES NOT EXIST")
    except IOError:
        print( "File could not be open !! Press any Key...")
"""*****************************************************************************
                        FUNCTION TO MODIFY STUDENT RECORD OF FILE
*****************************************************************************"""

def modify_studata(n):
    found=0
    try:
        inFile=open("student.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            st=pickle.load(inFile)
            if st.retadmno()==n:
                print( 30*"-")
                st.show_studata()
                print( 30*"-")
                print( "\n\nEnter The New Details of Account")
                st.modify()
                pickle.dump(st,outFile)
                print( "\n\n\tRecord Updated")
                found=1
            else:
                pickle.dump(st,outFile)
             
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print( "\n\nRecord Not Found ")

    except IOError:
        print( "File could not be open !! Press any Key...")

    os.remove("student.dat")
    os.rename("temp.dat","student.dat")

"""*****************************************************************************
                        FUNCTION TO MODIFY FEE RECORD OF FILE
*****************************************************************************"""

def modify_feedata(n):
    found=0
    try:
        inFile=open("feedata.dat","rb")
        outFile=open("temp.dat","ab")
        while True:
            fe=pickle.load(inFile)
            if fe.rettrno()==n:
                print( 30*"-")
                fe.show_feedata()
                print( 30*"-")
                print( "\n\nENTER THE NEW DETAILS OF THE STUDENT")
                fe.modify()
                pickle.dump(fe,outFile)
                print( "\n\n\tRECORD UPDATED")
                found=1
            else:
                pickle.dump(fe,outFile)
             
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print( "\n\nRECORD NOT FOUND ")

    except IOError:
        print( "File could not be open !! Press any Key...")

    os.remove("feedata.dat")
    os.rename("temp.dat","feedata.dat")
    
"""*****************************************************************************
                    FUNCTION TO DELETE STUDENT RECORD OF FILE
*****************************************************************************"""

def delete_studata(n):
    found=0

    try:
        inFile=open("student.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            st=pickle.load(inFile)
            if st.retadmno()==n:
                found=1
                print( "\n\n\tRecord Deleted ..")
            else:
                pickle.dump(st,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print( "\n\nRecord Not Found")

    except IOError:
        print( "File could not be open !! Press any Key...")

    os.remove("student.dat")
    os.rename("temp.dat","student.dat")

"""*****************************************************************************
                    FUNCTION TO DELETE FEE RECORD OF FILE
*****************************************************************************"""

def delete_feedata(n):
    found=0

    try:
        inFile=open("feedata.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            fe=pickle.load(inFile)
            if fe.rettrno()==n:
                found=1
                print( "\n\n\tRECORD DELETED ..")
            else:
                pickle.dump(fe,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print( "\n\nRECORD NOT FOUND")

    except IOError:
        print( "File could not be open !! Press any Key...")

    os.remove("feedata.dat")
    os.rename("temp.dat","feedata.dat")


"""*****************************************************************************
                    FUNCTION TO DISPLAY ALL ACCOUNT DETAILS
*****************************************************************************"""

def display_allStudent():
    print( "\n\nSTUDENT DATA LIST\n\n")
    print( 60*"=")
    print( "%-10s"%"Adm No.","%-20s"%"Name","%-20s"%"Mother's name","%-20s"%"Father's name" ,"%-20s"%"Date of birth")
    print( 60*"=","\n")
    try:
        inFile=open("student.dat","rb")
        while True:
            st=pickle.load(inFile)
            st.report()
            
    except EOFError:
        inFile.close()
        
    except IOError:
        print( "File could not be open !! Press any Key...")

"""*****************************************************************************
                    FUNCTION TO DISPLAY ALL FEE DETAILS
*****************************************************************************"""

def display_allFee():
    print( "\n\n\tSTUDENT FEEDATA LIST\n\n")
    print( 60*"=")
    print( "%-10s"%"TR.NO.","%-20s"%"NAME","%-10s"%"MONTH","%-6s"%"AMOUNT")
    print( 60*"=","\n")
    try:
        inFile=open("feedata.dat","rb")
        while True:
            fe=pickle.load(inFile)
            fe.report()
            
    except EOFError:
        inFile.close()
        
    except IOError:
        print( "File could not be open !! Press any Key...")



"""*****************************************************************************
                        INTRODUCTORY FUNCTION
*****************************************************************************"""

def intro():
    print( "\n\n\t\t       SCHOOL    MANAGEMENT   SYSTEM")
    print( "\n \t\tJUSCO   SCHOOL   SOUTH   PARK,   BISTUPUR")
    print( "\n\n\nMADE BY:  AMAN UPHADYAY")
    print( "\nSCHOOL : JUSCO SCHOOL SOUTH PARK")


"""*****************************************************************************
                        THE FEE MENU FUNCTION OF PROGRAM
*****************************************************************************"""
def FeeMenu():
    while True:
        print( 3*"\n",70*"=")
        print( "FEE MENU:")
        print( 3*"\n",70*"=")
        print( "1. ADD NEW FEE DETAILS")
        print( "2. SHOW FEE DETAILS")
        print( "3. SHOW FEE DETAILS OF ALL STUDENT")
        print( "4. DELETE FEE DETAILS")
        print( "5. MODIFY FEE DETAILS")
        print( "6. EXIT")

        try:
            ch=int(input("ENTER YOUR CHOICE(1~8): "))
            if ch==1:
                write_feedata()
            
            elif ch==2:
                num=int(input("\n\nENTER TRANSACTION NUMBER: "))
                display_feedata(num)

            elif ch==3:
                display_allFee()

            elif ch==4:
                num=int(input("\n\nENTER TRANSACTION NUMBER: "))
                delete_feedata(num)
            
            elif ch==5:
                num=int(input("\n\nENTER TRANSACTION NUMBER: "))
                modify_feedata(num)

            elif ch==6:
                break

            else:
                print( "INPUT CORRECT CHOICE...(1~6)")

        except NameError:
            print( "INPUT CORRECT CHOICE...(1~6)")
        

"""*****************************************************************************
                        THE STUDENT MENU FUNCTION OF PROGRAM
*****************************************************************************"""

def StudentMenu():
    while True:
        print( 3*"\n",70*"=")
        print( "STUDENT MENU:")
        
        print( "1. New Admission")
        print( "2. Modify Student ")
        print( "3. Delete Student")
        print( "4. Student Enquiry")
        print( "5. All Student List")
        print( "6. Return to Main Menu")

        try:
            ch=int(input("Enter Your Choice(1~6): "))
            if ch==1:
                write_studata()
            
            elif ch==2:
                num=int(input("\n\nEnter Admission Number : "))
                modify_studata(num)

            elif ch==3:
                num=int(input("\n\nEnter Admission Number : "))
                delete_studata(num)

            elif ch==4:
                num=int(input("\n\nEnter Admission Number : "))
                display_studata(num)

            elif ch==5:
                display_allStudent()

            elif ch==6:
                break

            else:
                print( "Input correcr choice...(1-6)")

        except NameError:
                print( "Input correct choice...(1-6)")
        
"""*****************************************************************************
                        THE STUDENT MENU FUNCTION OF PROGRAM
*****************************************************************************"""
intro()

while True:
        print( 3*"\n",70*"=")
        print( "MAIN MENU:")
        
        print( "1. STUDENT MENU")
        print( "2. FEE MENU ")
        print( "3. Exit")

        try:
            ch=int(input("Enter Your Choice(1~3): "))
            if ch==1:
                StudentMenu()
            
            elif ch==2:
                FeeMenu()

            elif ch==3:
                break

            else:
                print( "Input correcr choice...(1-3)")

        except NameError:
            print( "Input correct choice...(1-3)")

input("\n\n\n\n\nTHANK YOU\n\nPress any key to exit...")

"""*****************************************************************************
				END OF PROJECT
*****************************************************************************"""
