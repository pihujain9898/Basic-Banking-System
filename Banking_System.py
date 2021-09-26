#importing statements
import mysql.connector as mc
import pandas as pd
pd.set_option('display.max_columns',50)         #For too many columns
pd.set_option('expand_frame_repr',False)        #For columns in singel row
import subprocess as s

#Fuctions
#Function 1(Viewing details)
def preview_function():
    s.call('cls',shell=True)
    cursor.execute("select * from customer")
    customer_data = cursor.fetchall()
    customer = pd.DataFrame(customer_data,columns = ['SNo','Name','Mobile_No','Adress','Email','Account_No','PIN','Amount'])
    print("Customer details :-")
    print(customer)
    
#Function 2(Adding new data)
def signin_function():
    s.call('cls',shell=True)
    cursor.execute("select * from customer")
    customer_data = cursor.fetchall()
    list1 = []
    list2 = []
    for i in range(len(customer_data)):
        list1.append(int(customer_data[i][5]))
        list2.append(int(customer_data[i][6]))
    SNo = len(customer_data)+1
    Name = input("Enter customer name: ")
    Mobile_No = input("Enter customer mobile number: ")
    Adress = input("Enter customer adress: ")
    Email = input("Enter customer email: ")
    Account_No = str(int(customer_data[-1][5])+1)
    PIN = input("Choose your PIN: ")
    Amount = int(input("Enter amount for depositing: "))
    string1 = "insert into customer values({},'{}','{}','{}','{}','{}','{}',{})".format(SNo,Name,Mobile_No,Adress,Email,Account_No,PIN,Amount)
    cursor.execute(string1)
    obj.commit()
    
#Function 3(Executing old data)
def login_function():
    s.call('cls',shell=True)
    cursor.execute("select * from customer")
    customer_data = cursor.fetchall()
    list1 = []
    list2 = []
    list3 = []
    for i in range(len(customer_data)):
        list1.append(int(customer_data[i][5]))
        list2.append(int(customer_data[i][6]))
        list3.append(int(customer_data[i][7]))
    Account_No = int(input("Enter Account_No: "))        
    if Account_No in list1:
        var2 = list1.index(Account_No)
        PIN = int(input("Enter PIN: "))         
        if str(list2[var2])==str(PIN):
            s.call('cls',shell=True)
            print("1. Deposit money.\n2. Withdraw money.\n3. Main account balance.\n")
            choice2 = int(input("Enter your choice: "))
            var3 = list3[var2]
            s.call('cls',shell=True)
            if choice2 == 1:
                print('\n')
                var4 = int(input("Enter depositing amount: "))
                cursor.execute("update customer set Amount = {} where Account_No = {}".format(var3+var4,str(Account_No)))
                obj.commit()
                cursor.execute("select * from customer")
                customer_data = cursor.fetchall()
                list3 = []
                for i in range(len(customer_data)):
                    list3.append(int(customer_data[i][7]))
                var3 = list3[var2]
                print("Your account balance is",var3)
            elif choice2 == 2:
                var4 = int(input("Enter withdrawing amount: "))
                cursor.execute("update customer set Amount = {} where Account_No = {}".format(var3-var4,str(Account_No)))
                obj.commit()
                cursor.execute("select * from customer")
                customer_data = cursor.fetchall()
                list3 = []
                for i in range(len(customer_data)):
                    list3.append(int(customer_data[i][7]))
                var3 = list3[var2]
                print("Your account balance is",var3)
            elif choice2 == 3:
                cursor.execute("select * from customer")
                customer_data = cursor.fetchall()
                list3 = []
                for i in range(len(customer_data)):
                    list3.append(int(customer_data[i][7]))
                var3 = list3[var2]
                print("Your account balance is",var3)
            else:
                 print("Check your choice.")
        else:
            print("Incorrect PIN")
    else:
        print("Incorrect Account_No.")

#Compiled function     
def main_function():
    s.call('cls',shell=True)
    print("Welcome to Banking System")
    choice1 = 1
    while choice1 != 0:
        print('\nX-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X')
        print("1. Customer details.\n2. New customer.\n3. Existing Customer.")
        print("0. Quit\n")
        choice1 = int(input("Enter your choice: "))
        if choice1 == 1:
            s.call('cls',shell=True)
            preview_function()
        elif choice1 == 2:
            s.call('cls',shell=True)
            signin_function()
        elif choice1 == 3:
            s.call('cls',shell=True)
            login_function()
        elif choice1 == 0:
            exit()
        else:
            print("Check your choice.")

#python-mysql connection and starting of program
try:            
    mysql_password = input("Enter password of your mysql: ")
    try:
        obj = mc.connect(host = "localhost",
                      user = "root",
                      passwd = mysql_password,
                      database = "banking")
        cursor = obj.cursor()
        main_function()
    except:
        obj = mc.connect(host = "localhost",
                            user = "root",
                            passwd = mysql_password,
                            database = "mysql")
        cursor = obj.cursor()
        cursor.execute("create database banking;")
        cursor.execute("use banking;")
        cursor.execute("create table customer (SNo int, Name varchar(40), Mobile_No varchar(15), Adress varchar(60), Email varchar(40), Account_No varchar(20), PIN varchar(20), Amount int(10));")
        cursor.execute("insert into customer values(1,'Rahul','8441918277','F-201,Kanakpura Nagar','rahul2002@gmail.com;','30201200001','0912',10000)")
        cursor.execute("insert into customer values(2,'Aman','9929507402','C-212,Shyam Nagar Sodala','aman1998@gmail.com;','30201200002','1234',5000)")
        obj.commit()
        main_function()
except:
    s.call('cls',shell=True)
    print("Something went wrong!")


