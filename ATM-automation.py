username='suhi'
password='python123'

c_name=input("enter user name")
c_pass=str(input("enter your password"))
if c_name==username and c_pass==password:
    print("success")
    print('''
    1.Deposite
    2.withdraw
    3.ministatement
    4.exit
    ''' )
    amount=50000
    option=int(input("select your option:"))
    #print("please enter valid option")

    if option==1:
        dep=int(input("enter the amount"))
        amount=amount+dep
        print("total amount:",amount)
    elif option==2:
        withdrawal=int(input("enter the amount:"))
        amount=amount-withdrawal
        print("total amount:",amount)
    elif option==3:
        print("======ATM======")
        print("username:",username)
        print("total amount:",amount)
        print("======thanks for visiting======")
    elif option==4:
        exit()
    else:
        print("please enter correct login")