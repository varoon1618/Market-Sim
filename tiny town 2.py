import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import mysql.connector


# INITIAL CONNECTION TO DATABASE
mycon = mysql.connector.connect(host = 'localhost',user = ' root ',password = 'varun0702',database = 'town')
mycursor = mycon.cursor()
window = tk.Tk()

# FUNTIONS TO MOVE AROUND DIFFERENT FRAMES ============================================================================
def show_frame():
    frame2.pack_forget()
    frame1.pack(expand="yes",fill="both")
    window.geometry("500x500")
    
def f1tof2():
    frame1.pack_forget()
    frame2.pack(expand="yes",fill="both")
    window.geometry("400x300")
    flbl1.destroy()

def f4tof2():
    frame4.pack_forget()
    frame2.pack(expand="yes",fill="both")
    window.geometry("400x300")
    
    
def f2tof3():
    frame2.pack_forget()
    frame3.pack(expand="yes",fill="both")
    window.geometry("400x300")

def f3tof2():
    frame3.pack_forget()
    frame2.pack(expand="yes",fill="both")
    window.geometry("400x300")

def login_popup():
    frame3.pack_forget()
    frame4.pack(expand="yes",fill="both")
    window.geometry("500x500")

def f4tof5():
    frame4.pack_forget()
    frame5.pack(expand="yes",fill="both")
    window.geometry("500x500")

def f5tof4():
    frame5.pack_forget()
    frame4.pack(expand="yes",fill="both")
    window.geometry("500x500")
    
def f4tof6():
    frame4.pack_forget()
    frame6.pack(expand="yes",fill="both")
    window.geometry("500x500")

def f6tof4():
    frame6.pack_forget()
    frame4.pack(expand="yes",fill="both")
    window.geometry("500x500")
    
def f4tof7():
    frame4.pack_forget()
    frame7.pack(expand="yes",fill="both")
    window.geometry("500x500")

def f7tof4():
    frame7.pack_forget()
    frame4.pack(expand="yes",fill="both")
    window.geometry("500x500")
    
def f8tof9():
    frame8.pack_forget()
    frame9.pack(expand="yes",fill="both")
    window.geometry("400x300")

def f9tof8():
    frame9.pack_forget()
    frame8.pack(expand="yes",fill="both")
    window.geometry("400x300")

def f8tof2():
    frame8.pack_forget()
    frame2.pack(expand="yes",fill="both")
    window.geometry("400x300")

def f2tof8():
    frame2.pack_forget()
    frame8.pack(expand="yes",fill="both")
    window.geometry("400x300")

def f9tof10():
    frame9.pack_forget()
    frame10.pack(expand="yes",fill="both")
    window.geometry("400x300")

def f10tof9():
    frame10.pack_forget()
    frame9.pack(expand="yes",fill="both")
    window.geometry("400x300")

def f9tof11():
    frame9.pack_forget()
    frame11.pack(expand="yes",fill="both")
    window.geometry("400x300")

def f11tof9():
    frame11.pack_forget()
    frame9.pack(expand="yes",fill="both")
    window.geometry("400x300")
    
def f9tof2():
    frame9.pack_forget()
    frame2.pack(expand="yes",fill="both")
    window.geometry("400x300")


# FUNCTIONS FOR REGISTERING AND LOGIN======================================================================================================= 

def login():
    #FETCHES ALL INFORMATION ENTERED FROM LOGIN_DETAILS AND CHECKS IF PASSWORD AND USERNAME MATCH
    global username1
    username1 = entry_5.get()
    password1 = entry_6.get()
    sql = "select name, password from people where name=%s and password=%s"
    val = (username1,password1)
    mycursor.execute(sql,val)
    result1=mycursor.fetchone()
    var=tk.StringVar()
    var.set(username1)
    if result1:
        login_popup()
        label7 = tk.Label(frame4,textvariable=var,font=("Bodoni MT", 15))
        label7.place(x=210,y=50)
        label8 = tk.Label(frame4,text="Welcome",font=("Bodoni MT", 15))
        label8.place(x=210,y=10)
        entry_5.delete(0,'end')
        entry_6.delete(0,'end')
    else:
        entry_5.delete(0,'end')
        entry_6.delete(0,'end')
        loginfail=tk.Label(frame3,text="You've entered wrong credentials,please try again")
        loginfail.place(x=80,y=250)

def register():
    #TAKES INPUT FROM VARIOUS TKINTER WIDGETS AND ADDS IT TO A TABLE login_details
    name = entry_1.get()
    password = entry_2.get()
    number = entry_3.get()
    #emailid = entry_4.get()
   
    mycursor.execute("select count(*) from people")
    result = mycursor.fetchone()
    old_count = result[0]
    sql = "INSERT INTO people (name,password,number) VALUES (%s,%s,%s)"
    val = (name,password,number)
    mycursor.execute(sql,val)
    mycon.commit()
    entry_1.delete(0,'end')
    entry_2.delete(0,'end')
    entry_3.delete(0,'end')
    #entry_4.delete(0,'end')
    mycursor.execute("select count(*) from people")
    result = mycursor.fetchone()
    new_count = result[0]
    if(old_count + 1 == new_count):
        global flbl1
        flbl1 =tk.Label(frame1,text ="Your account has been reigstered successfully , please head over to home page",width=65)
        flbl1.place(x=60,y=390)
    else:
        flbl2=tk.Label(frame1,text="Your account could not be registered,please retry",width=65)
        flbl2.place(x=60,y=390)

#INITIALISING FRAMES=========================================================================================================================
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
frame1 = tk.Frame(window)
frame2 = tk.Frame(window,bg="#003366")
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)
frame5 = tk.Frame(window)
frame6 = tk.Frame(window)
frame7 = tk.Frame(window)
frame8 = tk.Frame(window)
frame9 = tk.Frame(window)
frame10= tk.Frame(window)
frame11= tk.Frame(window)
frame2.pack(expand="yes",fill="both")






#FRAME 7 ANALYSIS FRAME (CLIENT)=====================================================================

def analysis():
    #SORTS ROWS FROM SELL_DETAILS WITH USERNAME AND PRINTS THE SELLING HISTORY ALONG WITH OTHER DETAILS
    mywin3 = tk.Tk()
    mycursor.execute("select * from sell_details")
    sdata = mycursor.fetchall()
    list5=[]
    list6=[]
    for i in sdata:#FORMS A LIST WITH ALL RECORDS
        list5.append(i)
    for j in list5:#SORTS THE ALREADY ACQUIRED LIST
        if j[0]==username1:
            list6.append(j)
    total_rows = len(list6)
    total_columns = len(list6[0])
    e=tk.Label(mywin3,width=10,text='uname',borderwidth=2, relief='ridge',anchor='w',bg='yellow')#ADDING HEADERS TO TABLE
    e.grid(row=0,column=0)
    e=tk.Label(mywin3,width=10,text='stock',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=tk.Label(mywin3,width=10,text='cp',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=tk.Label(mywin3,width=10,text='sp',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=tk.Label(mywin3,width=10,text='num',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=tk.Label(mywin3,width=10,text='tot_cp',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
    e=tk.Label(mywin3,width=10,text='tot_sp',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=6)
    e=tk.Label(mywin3,width=10,text='brokerage',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=7)
    e=tk.Label(mywin3,width=10,text='tax',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=8)
    e=tk.Label(mywin3,width=10,text='profit',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=9)
    mywin3.title('your analysis')
    for i in range(total_rows):#PRINTING TABLE WITH WIDGETS
        for j in range(total_columns):
            e=tk.Entry(mywin3, width=10, fg='blue')
            e.grid(row=i+1, column=j)
            e.insert(tk.END, list6[i][j])


    
#FRAME 6 SELLING FRAME =====================================================================
def sell_stock():
    #SELLS STOCKS PRESENT IN PORTFOLIO
    username2 = username1
    stock = choice1
    amount1 = int(entry8.get())
 
    if stock=="apple":#ASSIGNS THE SELLING PRICE OF EACH STOCK
        price1=120
        price=100
    elif stock=="gold":
        price1=1000
        price=5000
    elif stock=="cloth":
        price1=600
        price=500
    elif stock=="bicycle":
        price1=50
        price=1000
    elif stock=="banana":
        price1=10
        price=50
    elif stock=="spice":
        price1=800
        price=700
    elif stock=="mobile":
        price1=150
        price=200
    elif stock=="shoes":
        price1=900
        price=1000
    elif stock=="medicine":
        price1=150
        price=100
    elif stock=="watch":
        price1=370
        price=350

    #CREATES A TABLE SELL_DETAILS  
    mycursor.execute('''CREATE TABLE IF NOT EXISTS sell_details(uname VARCHAR(50),
            stock VARCHAR(50),
            cp VARCHAR(50),
            sp VARCHAR(50),
            num VARCHAR(50),
            tot_cp VARCHAR(50),
            tot_sp VARCHAR(50),
            brokerage VARCHAR(50),
            tax VARCHAR(50),
            profit VARCHAR(50));''')
    
    #CALCULATES DETAILS
    selling_price=amount1*price1
    total_price =amount1*price
    brokerage = 0.02*price1
    profit = selling_price-total_price
    if(profit>0):
        taxes= 0.2*(profit-brokerage)
    else:
        taxes=0
    net_profit=0.8*(profit-brokerage)

    #ADDING DETAILS TO TABLE SELL_DETAILS
    sql = "INSERT INTO sell_details (uname,stock,cp,sp,num,tot_cp,tot_sp,brokerage,tax,profit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (username2,stock,price,price1,amount1,total_price,selling_price,brokerage,taxes,net_profit)
    mycursor.execute(sql,val)
    mycon.commit()
    mycursor.execute("select * from holding_details")#SELECTS DETAILS FROM HOLDING_DETAILS
    data = mycursor.fetchall()
    list4=[]
    for i in data:#ADDS THE ROWS FROM HOLDING DETAILS TO A LIST
        list4.append(i)
    for j in list4:#SORTS THE LIST ON BASIS OF USERNAME AND STOCK TO BE SOLD
        if j[0]==username2 and j[1]==choice1:
            list4.remove(j)#REMOVES STOCK FROM THE LIST 
    print(list4)
    mycursor.execute("delete from holding_details")#DELETES ALL ROWS IN TABLE HOLDING DETAILS
    rows = list4
    values = ', '.join(map(str, rows))#ADDS THE UPDATED VALUES BACK TO TABLE HOLDING DETAILS
    sql ="INSERT INTO holding_details VALUES {}".format(values)
    mycursor.execute(sql)
    mycon.commit()  
    list4.clear()
def get_selling_price():#DISPLAYS SELLING PRICE USING WIDGETS DEPENDING ON STOCK SELECTED
    global entry8
    
    global choice1
    choice1=droplist1.get()
    if choice1==("apple"):
        label12 = tk.Label(frame6,text="price of one item")
        label12.place(x=70,y=110)
        label14 = tk.Label(frame6,text="120 per item")
        label14.place(x=300,y=110)
        label10 = tk.Label(frame6,text="choose how many items to sell")
        label10.place(x=70,y=160)
        entry8 = tk.Entry(frame6)
        entry8.place(x=300,y=160)
        
    elif choice1=="gold":
     
        label12 = tk.Label(frame6,text="price of one item")
        label12.place(x=70,y=110)
        label14 = tk.Label(frame6,text="1000 per item")
        label14.place(x=300,y=110)
        entry8 = tk.Entry(frame6)
        entry8.place(x=300,y=160)
        label10 = tk.Label(frame6,text="choose how many items to sell")
        label10.place(x=70,y=160)
        
    elif choice1==("cloth"):
      
        label12 = tk.Label(frame6,text="price of one item")
        label12.place(x=70,y=110)
        label14 = tk.Label(frame6,text="600 per item")
        label14.place(x=300,y=110)
        entry8 = tk.Entry(frame6)
        entry8.place(x=300,y=160)
        label10 = tk.Label(frame6,text="choose how many items to sell")
        label10.place(x=70,y=160)
        
    elif choice1==("bicycle"):
  
        label12 = tk.Label(frame6,text="price of one item")
        label12.place(x=70,y=110)
        label14 = tk.Label(frame6,text="50 per item")
        label14.place(x=300,y=110)
        entry8 = tk.Entry(frame6)
        entry8.place(x=300,y=160)
        label10 = tk.Label(frame6,text="choose how many items to sell")
        label10.place(x=70,y=160)
       
    elif choice1=="banana":
        label12 = tk.Label(frame6,text="price of one item")
        label12.place(x=70,y=110)
        label13 = tk.Label(frame6,text="10 per item")
        label13.place(x=300,y=110)
        entry8 = tk.Entry(frame6)
        entry8.place(x=300,y=160)
        label10 = tk.Label(frame6,text="choose how many items to sell")
        label10.place(x=70,y=160)
        
    elif choice1=="spice":
       
        label12 = tk.Label(frame6,text="price of one item")
        label12.place(x=70,y=110)
        label14 = tk.Label(frame6,text="800 per item")
        label14.place(x=300,y=110)
        entry8 = tk.Entry(frame6)
        entry8.place(x=300,y=160)
        label10 = tk.Label(frame6,text="choose how many items to sell")
        label10.place(x=70,y=160)
        
    elif choice1=="mobile":
        
        label12 = tk.Label(frame6,text="price of one item")
        label12.place(x=70,y=110)
        label14 = tk.Label(frame6,text="150 per share")
        label14.place(x=300,y=110)
        entry8 = tk.Entry(frame6)
        entry8.place(x=300,y=160)
        label10 = tk.Label(frame6,text="choose how many items to sell")
        label10.place(x=70,y=160)
        
    
        
    elif choice1=="shoes":
        
        label12 = tk.Label(frame6,text="price of one item")
        label12.place(x=70,y=110)
        label13 = tk.Label(frame6,text="900 per item")
        label13.place(x=300,y=110)
        entry8 = tk.Entry(frame6)
        entry8.place(x=300,y=160)
        label10 = tk.Label(frame6,text="choose how many items to sell")
        label10.place(x=70,y=160)
        
    
        
    elif choice1== "medicine":
        
        label12 = tk.Label(frame6,text="price of one item")
        label12.place(x=70,y=110)
        label14 = tk.Label(frame6,text="150 per item")
        label14.place(x=300,y=110)
        entry8 = tk.Entry(frame6)
        entry8.place(x=300,y=160)
        label10 = tk.Label(frame6,text="choose how many items to sell")
        label10.place(x=70,y=160)
        
    
        
    elif choice1== "watch":
      
        label12 = tk.Label(frame6,text="price of one item")
        label12.place(x=70,y=110)
        label14 = tk.Label(frame6,text="370 per item")
        label14.place(x=300,y=110)
        entry8 = tk.Entry(frame6)
        entry8.place(x=300,y=160)
        label10 = tk.Label(frame6,text="choose how many items to sell")
        label10.place(x=70,y=160)
        
    
    
        
        

l2 = ["apple" , "gold" , "cloth" , "bicycle" , "banana" , "spice" ,"mobile" , "shoes", "medicine", "watch"]
droplist1 = ttk.Combobox(frame6,values=l2)
label11 = tk.Label(frame6,text="choose which items to sell")
label11.place(x=70,y=60)
droplist1.place(x=300, y=60)
button111 = tk.Button(frame6,width=15,text="See Selling price",command=lambda:get_selling_price())
button111.place(x=50,y=230)
button12 = tk.Button(frame6,width=15,text="Show owned items",command=lambda:show_items())
button12.place(x=180,y=230)
button13 =tk.Button(frame6,width=15,text="Sell",command=lambda:sell_stock())
button13.place(x=310,y=230)
button14=tk.Button(frame6,width=23,text="return to home page",command=lambda:f6tof4())
button14.place(x=180,y=280)
    
# VIEW PORTFOLIO WINDOW======================================================================
def show_items():#FROM TABLE HOLDING DETAILS IT SORTS OUT REQUIRED PORTFOLIO
    mycursor.execute("select * from holding_details")
    hdata = mycursor.fetchall()
    list2=[]
    list3=[]
    for i in hdata:
        list2.append(i)
    for j in list2:
        if j[0]==username1:
            list3.append(j)
    
    mywin2 = tk.Tk()
    total_rows = len(list3)
    total_columns = len(list3[0])
    e=tk.Label(mywin2,width=30,text='Username',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=tk.Label(mywin2,width=30,text='item',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=tk.Label(mywin2,width=30,text='Price per item',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=tk.Label(mywin2,width=30,text='number of items',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=tk.Label(mywin2,width=30,text='total',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    mywin2.title('your items')
    for i in range(total_rows):
        for j in range(total_columns):
            e=tk.Entry(mywin2, width=30, fg='blue')
            e.grid(row=i+1, column=j)
            e.insert(tk.END, list3[i][j])

            
#FRAME 5 BUYING WINDOW ===================================================
def getstock():#DISPLAYS BUYING PRICE OF STOCK DEPENDING ON STOCK CHOSEN
    global choice
    global label13
    choice = droplist.get()
    print(choice)
    if choice==("apple"):
        global entry7
        label12 = tk.Label(frame5,text="price of one item")
        label12.place(x=70,y=110)
        label13 = tk.Label(frame5,text="100 per item")
        label13.place(x=300,y=110)
        label10 = tk.Label(frame5,text="choose how many items to buy")
        label10.place(x=70,y=160)
        entry7 = tk.Entry(frame5)
        entry7.place(x=300,y=160)
    elif choice=="gold":
     
        label12 = tk.Label(frame5,text="price of one item")
        label12.place(x=70,y=110)
        label13 = tk.Label(frame5,text="5000 per item")
        label13.place(x=300,y=110)
        label10 = tk.Label(frame5,text="choose how many items to buy")
        label10.place(x=70,y=160)
        entry7 = tk.Entry(frame5)
        entry7.place(x=300,y=160)
    elif choice==("cloth"):
      
        label12 = tk.Label(frame5,text="price of one item")
        label12.place(x=70,y=110)
        label13 = tk.Label(frame5,text="500 per item")
        label13.place(x=300,y=110)
        label10 = tk.Label(frame5,text="choose how many items to buy")
        label10.place(x=70,y=160)
        entry7 = tk.Entry(frame5)
        entry7.place(x=300,y=160)
    elif choice==("bicycle"):
  
        label12 = tk.Label(frame5,text="price of one item")
        label12.place(x=70,y=110)
        label13 = tk.Label(frame5,text="1000 per item")
        label13.place(x=300,y=110)
        label10 = tk.Label(frame5,text="choose how many items to buy")
        label10.place(x=70,y=160)
        entry7 = tk.Entry(frame5)
        entry7.place(x=300,y=160)
       
    elif choice =="banana":
        label12 = tk.Label(frame5,text="price of one item")
        label12.place(x=70,y=110)
        label13 = tk.Label(frame5,text="50 per share")
        label13.place(x=300,y=110)
        label10 = tk.Label(frame6,text="choose how many items to buy")
        label10.place(x=70,y=160)
        entry7 = tk.Entry(frame5)
        entry7.place(x=300,y=160)
    elif choice =="spice":
       
        label12 = tk.Label(frame5,text="price of one item")
        label12.place(x=70,y=110)
        label13 = tk.Label(frame5,text="200 per item")
        label13.place(x=300,y=110)
        label10 = tk.Label(frame6,text="choose how many items to buy")
        label10.place(x=70,y=160)
        entry7 = tk.Entry(frame5)
        entry7.place(x=300,y=160)
    elif choice =="mobile":
        
        label12 = tk.Label(frame5,text="price of one item")
        label12.place(x=70,y=110)
        label13 = tk.Label(frame5,text="200 per item")
        label13.place(x=300,y=110)
        label10 = tk.Label(frame5,text="choose how many items to buy")
        label10.place(x=70,y=160)
        entry7 = tk.Entry(frame5)
        entry7.place(x=300,y=160)
    elif choice =="shoes":
        
        label12 = tk.Label(frame5,text="price of one item")
        label12.place(x=70,y=110)
        label13 = tk.Label(frame5,text="1000 per item")
        label13.place(x=300,y=110)
        label10 = tk.Label(frame5,text="choose how many items to buy")
        label10.place(x=70,y=160)
        entry7 = tk.Entry(frame5)
        entry7.place(x=300,y=160)
    elif choice == "medicine":
        
        label12 = tk.Label(frame5,text="price of one item")
        label12.place(x=70,y=110)
        label13 = tk.Label(frame5,text="100 per item")
        label13.place(x=300,y=110)
        label10 = tk.Label(frame5,text="choose how many items to buy")
        label10.place(x=70,y=160)
        entry7 = tk.Entry(frame5)
        entry7.place(x=300,y=160)
    elif choice == "watch":
      
        label12 = tk.Label(frame5,text="price of one item")
        label12.place(x=70,y=110)
        label13 = tk.Label(frame5,text="350 per item")
        label13.place(x=300,y=110)
        label10 = tk.Label(frame5,text="choose how many items to buy")
        label10.place(x=70,y=160)
        entry7 = tk.Entry(frame5)
        entry7.place(x=300,y=160)

        
def bill():#EXTRACTS ROWS FROM BILLING DETAILS AS A LIST AND PRINTS IT OUT
    global my_w
    global mywin
    r_set=mycursor.execute("select * from billing_details")
    data = mycursor.fetchall()
    list1=[]
    for i in data:
        list1.append(i)
    
    my_w = tk.Tk()
    total_rows = len(list1)
    total_columns = len(list1[0])
    e=tk.Label(my_w,width=20,text='Username',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=tk.Label(my_w,width=20,text='item',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=tk.Label(my_w,width=20,text='Price per item',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=tk.Label(my_w,width=20,text='number of items',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=tk.Label(my_w,width=20,text='total',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    my_w.title('your bill')
    for i in range(total_rows):
        for j in range(total_columns):
            e=tk.Entry(my_w, width=20, fg='blue')
            e.grid(row=i+1, column=j)
            e.insert(tk.END, list1[i][j])

    mywin = tk.Tk()
    mywin.geometry("500x500")
    label_0 = tk.Label(mywin, text="Payment Window",width=20,font=("bold", 20))
    label_0.place(x=90,y=53)
    label_1 = tk.Label(mywin, text="Username",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)
    entry_1 = tk.Entry(mywin)
    entry_1.place(x=240,y=130)
    label_2 = tk.Label(mywin, text="Credit Card Number",width=20,font=("bold", 10))
    label_2.place(x=68,y=180)
    entry_2 = tk.Entry(mywin)
    entry_2.place(x=240,y=180)
    button1 = tk.Button(mywin,text="Confirm payment",width=20,command=lambda:confirm_payment())
    button1.place(x=180,y=350)
    button2 = tk.Button(mywin,text="Cancel payment",width=20,command=lambda:cancel_payment())
    button2.place(x=180,y=400)

def buystock():
    global total_price
    global amount
    username2 = username1
    stock = choice
    amount = int(entry7.get())
    global price
    if stock=="apple":
        price=100
    elif stock=="gold":
        price=5000
    elif stock=="cloth":
        price=500
    elif stock=="bicycle":
        price=1000
    elif stock=="banana":
        price=50
    elif stock=="spice":
        price=700
    elif stock=="mobile":
        price=200
    elif stock=="shoes":
        price=1000
    elif stock=="medicine":
        price=100
    elif stock=="watch":
        price=350
        
    
 # CREATING HODLING DETAILS TABLE
    mycursor.execute('''CREATE TABLE IF NOT EXISTS holding_details(USERNAME VARCHAR(50),
            NAME_OF_ITEM VARCHAR(50),
            PRICE_PER_ITEM VARCHAR(50),
            NUMBER_OF_ITEMS VARCHAR(50),
            TOTAL_COST VARCHAR(50));''')
    total_price=amount*price
    sql = "INSERT INTO holding_details (username,name_of_item,price_per_item,number_of_items,total_cost) VALUES (%s,%s,%s,%s,%s)"
    val = (username2,stock,price,amount,total_price)
    mycursor.execute(sql,val)#INSERTING VALUES INTO HOLDING DETAILS
    mycon.commit()

# CREATING BILLING DETAILS TABLE
    mycursor.execute('''CREATE TABLE IF NOT EXISTS billing_details(USERNAME VARCHAR(50),
            NAME_OF_ITEM VARCHAR(50),
            PRICE_PER_ITEM VARCHAR(50),
            NUMBER_OF_ITEMS VARCHAR(50),
            TOTAL_COST VARCHAR(50));''')
    sql1 = "INSERT INTO billing_details (username,name_of_item,price_per_item,number_of_items,total_cost) VALUES (%s,%s,%s,%s,%s)"
    val1 = (username2,stock,price,amount,total_price)
    mycursor.execute(sql1,val1)#ADDING RECORDS TO BILLING DETAILS
    mycon.commit()

    label13.destroy()
    entry7.delete(0,5)
    if amount == 0:
        tk.messagebox.showerror("Please enter the number of items you want to buy")
    else:
        tk.messagebox.showinfo("success","items have been added")
    
def confirm_payment():#CONFIRMS PAYMENT AND DELETES ALL ROWS FROM BILLING DETAILS
    tk.messagebox.showinfo("success","you have purchased items")
    mycursor.execute("delete from billing_details;")
    mywin.destroy()
    my_w.destroy()

def cancel_payment():#CANCELS PAYMENT AND DELETES ALL ROWS FROM BILLING DETAILS
    tk.messagebox.showinfo("cancelled","your payment has been cancelled")
    mycursor.execute("delete from billing_details;")
    mywin.destroy()
    my_w.destroy()

#TKINTER WIDGETS FOR BUYING WINDOW    
l1 = ["apple" , "gold" , "cloth" , "bicycle" , "banana" , "spice" ,"mobile" , "shoes", "medicine", "watch"]
droplist = ttk.Combobox(frame5,values=l1)
label11 = tk.Label(frame5,text="choose which items to buy")
label11.place(x=70,y=60)
droplist.place(x=300, y=60)
button111 = tk.Button(frame5,width=15,text="Select item",command=lambda:getstock())
button111.place(x=50,y=230)
button12 = tk.Button(frame5,width=15,text="Add to basket",command=lambda:buystock())
button12.place(x=180,y=230)
button13 =tk.Button(frame5,width=15,text="proceed to pay",command=lambda:bill())
button13.place(x=310,y=230)
button14=tk.Button(frame5,width=23,text="return to home page",command=lambda:f5tof4())
button14.place(x=180,y=280)

# FRAME 4 HOME PAGE CLIENT LOGIN ==========================================

label9 = tk.Label(frame4,text="Home Page",font=("Bodoni MT",15))
label9.place(x=190,y=100)
button6 = tk.Button(frame4,text="View Owned Items",font=("Bold",11),width=20,command=lambda:show_items())
button6.place(x=150,y=170)
button7 = tk.Button(frame4,text="Buy Items",font=("Bold",11),width=20,command=lambda:f4tof5())
button7.place(x=150,y=230)
button8 = tk.Button(frame4,text="Sell Items",font=("Bold",11),width=20,command=lambda:f4tof6())
button8.place(x=150,y=290)
button9 = tk.Button(frame4,text="View Analysis",font=("Bold",11),width=20,command=lambda:analysis())
button9.place(x=150,y=350)
button10 = tk.Button(frame4,text="Logout",font=("Bold",11),width=20,command=lambda:f4tof2())
button10.place(x=150,y=410)
#FRAME 3 LOGIN ====================================================

label_5 = tk.Label(frame3 ,text="Login Window",font=("bold", 18))
label_5.pack()
label_6 = tk.Label(frame3,text="Enter Username")
label_6.place(x=80,y=90)
entry_5=tk.Entry(frame3)
entry_5.place(x=200,y=90)
label_6 =tk.Label(frame3,text="Enter Password")
label_6.place(x=80,y=150)
entry_6=tk.Entry(frame3)
entry_6.place(x=200,y=150)
button4 = tk.Button(frame3,text="Login",width=15,command=lambda:login())
button4.place(x=230,y=220)
button5 = tk.Button(frame3,text="Back",width=15,command=lambda:f3tof2())
button5.place(x=80,y=220)

#FRAME 1 REGISTRATION FORM ============================================================================


label_0 = tk.Label(frame1, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = tk.Label(frame1, text="Username",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = tk.Entry(frame1)
entry_1.place(x=240,y=130)

label_2 = tk.Label(frame1, text="Password",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = tk.Entry(frame1)
entry_2.place(x=240,y=180)

label_3 = tk.Label(frame1, text="Mobile Number",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = tk.IntVar()

entry_3 = tk.Entry(frame1)
entry_3.place(x=240,y=230)

tk.Button(frame1, text='Submit',width=20,bg='green',fg='white',command=lambda:register()).place(x=180,y=350)
button_1 = tk.Button(frame1,text="back to home page",command=lambda:f1tof2())
button_1.place(x=0,y=0)


# FRAME 2 MAIN FRAME =========================================================

lbl=tk.Label(frame2,text="TINY TOWN", fg='#FFFFFF',bg="#003366", font=("Bodoni MT", 16))
lbl.place(x=110,y=0)
lbl1 = tk.Label(frame2, text="Welcome to your personal marketplace",fg='#FFFFFF',bg="#003366",font=("Calibri",13))
lbl1.place(x=30, y=50)
lbl2 = tk.Label(frame2,text = "have an account? ",font=("Calibri",10))
lbl2.place(x=35,y=120)
button1 = tk.Button(frame2,text= "Login",width=15,command=lambda:f2tof3())
button1.place(x=200, y=120)
button2 = tk.Button(frame2,text="Register",width=15,command=lambda:show_frame())
button2.place(x=200,y=160)
lbl3 = tk.Label(frame2,text=" Dont have an account ?")
lbl3.place(x=35,y=160)
#button3 = tk.Button(frame2,text="Employee Login",width=15,command=lambda:f2tof8())
#button3.place(x=200,y=200)
#lbl4 = tk.Label(frame2,text="Are you an employee ?",font=("Calibri",10))
#lbl4.place(x=35,y=200)
window.geometry("400x300")
window.mainloop()


