########################################################### CREDITS ##############################################################################################

'''
                                                  WELCOME TO THE HOTEL_MANAGER2

                THIS PROGRAM MANAGES A HOTEL'S CUSTOMERS, BILLS AND ROOMS USING A MYSQL DATABASE (HOTEL_DATABASE) WITH GUI

                                                    MADE BY : ARYAN RATHORE 
                                            COMPUTER SCIENCE ENGINEER AT VIT BHOPAL

                                                        CONTACT INFO
                                                aryanrathore13572002@gmail.com
                                               aryan.rathore2021@vitbhopal.ac.in
                                    LINKEDIN - https://www.linkedin.com/in/aryan-rathore-b15459215/
'''

########################################################### IMPORTS ##############################################################################################

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as tmsg
from tkinter import ttk
import mysql.connector as c
import datetime as dt
from tabulate import tabulate

########################################################### FUNCTIONS ############################################################################################


'''                                                             IMPORTANT NOTE                                                              
                     BEFORE YOU RUN THE PROGRAM MAKE SURE YOU READ AND FOLLOW THE LINES BELOW AND CHECK how_to_setup_hotel_manager2.txt 
                                                       OTHERWISE THE PROGRAM WONT RUN                                                      '''

# 1

'''          THERE ARE IN TOTAL OF 15 FUNCTIONS THAT CALL EACH OTHER, "EVERY FUNCTION HAS A DOCSTRING LIKE THIS SPECIFIES WHAT THAT FUNCTION DOES
                                                          AND HOW THE THE FUNCTION WORKS"                                                      '''

# 2

'''   I HAVE TO SPECIFY A FILE PATH TO OPEN THE LOG (BILLS.TXT, MANAGER_LOGINS.TXT and all the images and icons) FILES IF YOU ARE USING OR COPY PASTING MY CODE
            MAKE YOU CHANGE THE FILE PATHS I HAVE SPECIFIED WHICH FUNCTIONS NEED A 'FILE PATH CHANGE' SO MAKE SURE YOU CHANGE THEM FIRST '''

def insights():
    ''' this funtion will show important insights of the hotel i will update this in the future'''

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def check_in_visited(check_in_window):# file path change (title_icon, check_in_image.png) | done

    '''
        this function runs when the visited button is pressed in the check in window takes information of an old customer and assings them a room
        1. destroys the check_in_window | done
        2. makes a window that greets the customer [top frame] | done
        3. shows manager the customer table | done
        4. makes a frame with a form that takes their information if the old customer [form frame] | done
        5. makes a submit button that takes information of old customers [bottom frame] | done
        6. checks the values if the submit button is clicked and adds them to the database | done
        7. opens hotel_menu | done

    '''

    # -------------------------------------------------------------------------------------------------------
    # 1. destroys the hotel_menu_window 

    check_in_window.destroy()

    # -------------------------------------------------------------------------------------------------------
    # 2. makes a window that greets the customer [top frame]

    # -------------------------------------------------------------------------------------------------------
    # main window and frames

    check_inv_window = Tk()
    check_inv_window.geometry("1200x750")
    check_inv_window.wm_iconbitmap("F://aryans_code_notes//mySQL//hotel_manager_gui//title_icon.ico")
    check_inv_window.title("Hotel_manager")
    check_inv_window.config(bg = "#630330")

    # frames
    
    top_frame = Frame(check_inv_window, bg="#630330")
    top_frame.pack(side=TOP,fill=BOTH)

    form_frame = Frame(check_inv_window, bg="#630330")
    form_frame.pack(side=TOP,fill=BOTH)

    bottom_frame = Frame(check_inv_window, bg="#630330")
    bottom_frame.pack(side=BOTTOM,fill=BOTH)

    namaste_image = Image.open("F://aryans_code_notes//mySQL//hotel_manager_gui//check_in_image.png").resize((100,100), Image.ANTIALIAS)
    namaste_image = ImageTk.PhotoImage(namaste_image)

    Label(top_frame, image=namaste_image,borderwidth=10,relief=GROOVE,anchor=CENTER).pack(side=TOP,pady=(25,0))

    Label(top_frame, text="Namaste sir/maam\nWelcome back to our hotel",font=("Cascadia Mono SemiBold", 20, "bold italic"),anchor=CENTER,bg='#E30B5C',fg='white',borderwidth=2,relief=RIDGE).pack(side=TOP,pady=(25,10),fill=X)

    Label(top_frame, text="enter VSISTED customer's information below\ncheck black window to see what room they want AND THIER CUSTOMER_ID.",font=("Cascadia Mono SemiBold", 15, "bold italic"),fg='black',bg="#FDFF00",anchor=CENTER).pack(side=TOP,pady=(10,10),fill=X)
    
    Label(top_frame, text="IMPORTANT NOTE: 1.entries with 0 as initial value can have only integer values none of the values can be empty\n2.DO NOT ENTER A ROOM NUMBER THAT IS NOT EMPTY",font=("Cascadia Mono SemiBold", 15, "bold italic"),fg='black',bg="#FDFF00",anchor=CENTER).pack(side=TOP,pady=(10,25),fill=X)
    
    
    # -------------------------------------------------------------------------------------------------------
    # 3. shows manager the customer table and rooms table

    show_rooms()
    show_customer_info()

    # -------------------------------------------------------------------------------------------------------
    # 4. makes a frame with a form that takes their information if the old customer [form frame] 
    
    cust_id_var = IntVar(name="cust_id_var")
    bill_id_var = IntVar(name="bill_id_var") 
    room_num_var = IntVar(name="room_num_var") 
    pay_amt_var = IntVar(name="pay_amt_var")
    pay_method_var = StringVar(name="pay_method_var")
    no_of_people_var = IntVar(name="no_of_people_var")

    Label(form_frame,text="cust_id (from black window)".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=0,column=0,padx=(100,5),pady=(50,15),sticky=W)
    Entry(form_frame,textvariable=cust_id_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=0,column=1,padx=(100,10),pady=10,sticky=W)

    Label(form_frame,text="new bill_id (must be unique)".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=1,column=0,padx=(100,5),pady=(15,25),sticky=W)
    Entry(form_frame,textvariable=bill_id_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=1,column=1,padx=(100,10),pady=10,sticky=W)

    Label(form_frame,text="room_number (from black window)".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=2,column=0,padx=(100,5),pady=(15,25),sticky=W)
    Entry(form_frame,textvariable=room_num_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=2,column=1,padx=(100,10),pady=10,sticky=W)

    Label(form_frame,text="pay_amt".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=0,column=2,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=pay_amt_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=0,column=3,padx=(100,10),pady=10,sticky=W)

    Label(form_frame,text="pay_method".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=1,column=2,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=pay_method_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=1,column=3,padx=(100,10),pady=10,sticky=W)

    Label(form_frame,text="no_of_people".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=2,column=2,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=no_of_people_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=2,column=3,padx=(100,10),pady=10,sticky=W)

    # -------------------------------------------------------------------------------------------------------
    # 6. checks the values if the submit button is clicked and adds them to the database | done

    def check_visited_values():
        
        # add try accept here
        try:
            check_list = [cust_id_var,bill_id_var,room_num_var,pay_amt_var,pay_method_var,no_of_people_var]
            
            for Variable in check_list:
                if Variable.get() == "":
                    tmsg.showerror(f"Invalid value for {Variable}",f"{Variable} cannot be empty. ")
                    break
            else:
                # Checking if room is empty or not
                cursor1.execute(f"SELECT EMPTY FROM `room` WHERE room_number = {room_num_var.get()}; ")
                empty = cursor1.fetchone()
                
                # checking room number
                if empty == None:
                    tmsg.showerror("invalid value for room_number",f"the room with the room number {room_num_var.get()} does not exsist. ")
                elif empty[0] == "NO":
                    tmsg.showerror("invalid value for room_number",f"the room with the room number {room_num_var.get()} is not empty please choose another one. ")
                else:

                    # getting rest of the info from database and checking customer_id
                    cursor1.execute(f"SELECT * FROM customer WHERE customer_id = '{cust_id_var.get()}'")
                    result = cursor1.fetchone()

                    if result == None:
                        tmsg.showerror("invalid customer_Id",f"there is no customer with {cust_id_var} as their cust_id")
                    else:
                        tmsg.showinfo("check customer info",f"the fetched customer_info is as follows you may cross check it with black window ({result})")

                        customer_id =  cust_id_var.get()
                        bill_id = bill_id_var.get() 
                        room_number = room_num_var.get() 
                        payment_amount = pay_amt_var.get()
                        payment_method = pay_method_var.get()
                        number_of_people = no_of_people_var.get()

                        name = result[1]
                        age = result[3]
                        sex = result[4]
                        book_date = dt.date.today()
                        book_time = dt.datetime.now().time()
                        book_time = book_time.replace(microsecond=0)

                        # updating the room number the user is staying in and their new bill
                        cursor1.execute(f"UPDATE customer SET room_number = '{room_number}', bill_id = {bill_id} WHERE customer_id = {customer_id}; ")

                        # updating the room number the user is staying in and their new bill
                        cursor1.execute(f"UPDATE room SET EMPTY = 'NO', occupant= {customer_id} WHERE room_number = '{room_number}';")

                        # creating their bill and adding data to booking details
                        cursor1.execute(f"INSERT INTO booking_details VALUES ({bill_id},'{room_number}','{book_date}','{book_time}' ,{payment_amount},'{payment_method}',{number_of_people},{customer_id});")

                        # updating and logging in the bil log that the customer has come in:-
                        bill_log_checkin(bill_id, room_number, customer_id, name, age, sex, book_date, book_time, payment_amount, payment_method, number_of_people)

                        if cursor1.rowcount > 0:
                            print("\n------------------------------------------------------------------------------------------\n")
                            print(f"\t -------- SUCCESS WELCOME TO THE HOTEL {name} -------- \n")
                            print(f"1. the user {cust_id_var}, {name} has been ssuccessfully added to the database. ")
                            print(f"2. the book ing_details / bill {bill_id_var} has been successfully added to the database. ")
                            print(f"3. the {room_number} has been successfully updated to the database. ")
                            print("\n-----------------------------------------------------------------------------\n")
                            main_connector.commit()
                            tmsg.showinfo(f"welcome {name}","you have succesfully been added to our database. ")
                            check_inv_window.destroy()
                            hotel_menu()
                        else:
                            print(f"some error occured. ")

        except TclError:
            tmsg.showerror("invalid value","cust_id, bill_id must be integers only and not empty. ")
        

     # -------------------------------------------------------------------------------------------------------
     # 5. makes a submit button that takes information of old customers [bottom frame]

    Button(bottom_frame,text="SUBMIT",borderwidth=10,relief=RAISED,font=("",20,""),bg="#FFD700",command=check_visited_values).pack(anchor=CENTER,padx=250,pady=15)

    check_inv_window.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def check_in(hotel_menu_window): # file path change (title_icon, check_in_image.png) | done 
    '''
        this function runs when the check button is pressed it takes information of a customer and assings them a room
        1. destroys the hotel_menu_window | done
        2. makes a frame with a form that takes their information if the customer is new [form-top frame] | done
        3. makes a visited button that takes information of old customers and submit button to take values of the new customer [bottom frame] | done
        4. checks the values if the submit button is clicked and adds them to the database | done
        5. opens a new window where old customers information is taken | done

    '''

    # -------------------------------------------------------------------------------------------------------
    # 1. destroys the hotel_menu_window 

    hotel_menu_window.destroy()

    # -------------------------------------------------------------------------------------------------------
    # main window and frames

    check_in_window = Tk()
    check_in_window.geometry("1200x750")
    check_in_window.wm_iconbitmap("F://aryans_code_notes//mySQL//hotel_manager_gui//title_icon.ico")
    check_in_window.title("Hotel_manager")
    check_in_window.config(bg = "#630330")

    # frames
    
    top_frame = Frame(check_in_window, bg="#630330")
    top_frame.pack(side=TOP,fill=BOTH)

    form_frame = Frame(check_in_window, bg="#630330")
    form_frame.pack(side=TOP,fill=BOTH)

    bottom_frame = Frame(check_in_window, bg="#630330")
    bottom_frame.pack(side=BOTTOM,fill=BOTH)

    # -------------------------------------------------------------------------------------------------------
    # 2. makes a frame with a form that takes their information if the customer is new [form-top frame] | done

    room_image = Image.open("F://aryans_code_notes//mySQL//hotel_manager_gui//check_in_image.png").resize((80,80), Image.ANTIALIAS)
    room_image = ImageTk.PhotoImage(room_image)

    Label(top_frame, image=room_image,borderwidth=10,relief=GROOVE,anchor=CENTER).pack(side=TOP,pady=(25,0))

    Label(top_frame, text="Namaste sir/maam",font=("Cascadia Mono SemiBold", 20, "bold italic"),anchor=CENTER,bg='#E30B5C',fg='white',borderwidth=2,relief=RIDGE).pack(side=TOP,pady=(25,10),fill=X)

    Label(top_frame, text="enter NEW customer's information below\ncheck black window to see what room they want or CLICK VISITED IF THEY HAVE VISITED BEFORE.",font=("Cascadia Mono SemiBold", 15, "bold italic"),fg='black',bg="#FDFF00",anchor=CENTER).pack(side=TOP,pady=(10,10),fill=X)
    
    Label(top_frame, text="IMPORTANT NOTE: 1.entries with 0 as initial value can have only integer values none of the values can be empty\n2. if the customer has already visited before press the visited button and ignore this window.\n3.make sure the NAME HAS NO SPACE for Eg: (aryan rathore = aryan_rathore)",font=("Cascadia Mono SemiBold", 15, "bold italic"),fg='black',bg="#FDFF00",anchor=CENTER).pack(side=TOP,pady=(10,25),fill=X)

    cust_id_var = IntVar(name="cust_id_var")
    name_var = StringVar(name="name_var") 
    phone_var = IntVar(name="phone_var")
    age_var = IntVar(name="age_var")
    sex_var = StringVar(name="sex_var")  
    address_var = StringVar(name="address_var")  
    adhar_num_var = IntVar(name="adhar_num_var")
    bill_id_var = IntVar(name="bill_id_var")
    pay_amt_var = IntVar(name="pay_amt_var")
    pay_method_var = StringVar(name="pay_method_var")
    no_of_people_var = IntVar(name="no_of_people_var")
    room_number_var = IntVar(name="room_number")

    Label(form_frame,text="cust_id".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=0,column=0,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=cust_id_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=0,column=1,padx=(150,10),pady=10,sticky=W)

    Label(form_frame,text="name".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=1,column=0,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=name_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=1,column=1,padx=(150,10),pady=10,sticky=W)

    Label(form_frame,text="phone".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=2,column=0,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=phone_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=2,column=1,padx=(150,10),pady=10,sticky=W)

    Label(form_frame,text="age".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=3,column=0,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=age_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=3,column=1,padx=(150,10),pady=10,sticky=W)

    Label(form_frame,text="Sex ('M' or 'F')",font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=4,column=0,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=sex_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=4,column=1,padx=(150,10),pady=10,sticky=W)
    
    Label(form_frame,text="address".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=0,column=2,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=address_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=0,column=3,padx=(150,10),pady=10,sticky=W)

    Label(form_frame,text="adhar_num".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=1,column=2,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=adhar_num_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=1,column=3,padx=(150,10),pady=10,sticky=W)
    
    Label(form_frame,text="bill_id".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=2,column=2,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=bill_id_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=2,column=3,padx=(150,10),pady=10,sticky=W)

    Label(form_frame,text="pay_amt".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=3,column=2,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=pay_amt_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=3,column=3,padx=(150,10),pady=10,sticky=W)

    Label(form_frame,text="pay_method".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=4,column=2,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=pay_method_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=4,column=3,padx=(150,10),pady=10,sticky=W)

    Label(form_frame,text="no_of_people".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=5,column=0,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=no_of_people_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=5,column=1,padx=(150,10),pady=10,sticky=W)

    Label(form_frame,text="room_numnber (EMPTY ONLY)".capitalize(),font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#630330").grid(row=5,column=2,padx=(100,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=room_number_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=5,column=3,padx=(150,10),pady=10,sticky=W)


    # -------------------------------------------------------------------------------------------------------
    # 4. checks the values if the submit button is clicked and adds them to the database | done

    def check_form_values():
        try:
            
            variables_list = [room_number_var,cust_id_var,name_var,phone_var,age_var,sex_var,address_var,adhar_num_var,bill_id_var,pay_amt_var,pay_method_var,no_of_people_var]

            for variable in variables_list:
                if variable.get() == "":
                    tmsg.showerror(f"incorrect values for {variable}", f"{variable} must not be empty")
                    break
            else:
                
                # Checking if room is empty or not
                cursor1.execute(f"SELECT EMPTY FROM `room` WHERE room_number = {room_number_var.get()}; ")
                empty = cursor1.fetchone()
                
                if empty == None:
                    tmsg.showerror("invalid value for room_number",f"the room with the room number {room_number_var.get()} does not exsist. ")
                elif empty[0] == "NO":
                    tmsg.showerror("invalid value for room_number",f"the room with the room number {room_number_var.get()} is not empty please choose another one. ")
                else:
                
                    room_number = room_number_var.get()
                    customer_id = cust_id_var.get()
                    name = name_var.get()
                    
                    for letter in name:
                        if letter == " ":
                            name = name.replace(" ","_")
                            break
                    
                    phone = phone_var.get()
                    age = age_var.get()
                    sex = str(sex_var.get()).upper()
                    address =  address_var.get()
                    adhaar_number = adhar_num_var.get()
                    bill_id = bill_id_var.get()

                    # adding them to the customers table
                    # cursor1.execute(f"INSERT INTO customer VALUES ({customer_id}, '{name}',{phone}, {age}, '{sex}', '{address}', {adhar_number}, '{room_number}', {bill_id})")
                    cursor1.execute(f"INSERT INTO `customer` (`customer_id`, `name`, `phone`, `age`, `sex`, `address`, `adhaar_number`, `room_number`, `bill_id`) VALUES ('{customer_id}', '{name}', '{phone}', '{age}', '{sex}', '{address}', '{adhaar_number}', '{room_number}', '{bill_id}');")

                    book_date1 = dt.date.today()
                    book_time1 = dt.datetime.now().time()
                    book_time1 = book_time1.replace(microsecond=0)
                    payment_amount = pay_amt_var.get()
                    payment_method = pay_method_var.get()
                    number_of_people = no_of_people_var.get()
                    
                    # creating their bill and adding data to booking details
                    cursor1.execute(f"INSERT INTO booking_details VALUES ('{bill_id}','{room_number}','{book_date1}','{book_time1}' ,'{payment_amount}','{payment_method}','{number_of_people}','{customer_id}');")

                    # updating the booked rooms status to unavaible:-
                    cursor1.execute(f"UPDATE room SET EMPTY = 'NO', occupant= '{customer_id}' WHERE room_number = '{room_number}';")

                    # updating and logging in the bil log that the customer has come in:-
                    bill_log_checkin(bill_id, room_number, customer_id, name, age, sex, book_date1, book_time1, payment_amount, payment_method, number_of_people)

                    # -------------------------------------------------------------------------------------------------------
                    # 5. opens a new window where old customers information is taken | done
                    
                    if cursor1.rowcount > 0:
                        print("\n------------------------------------------------------------------------------------------\n")
                        print(f"\t -------- SUCCESS WELCOME TO THE HOTEL {name_var} -------- \n")
                        print(f"1. the user {cust_id_var}, {name_var} has been ssuccessfully added to the database. ")
                        print(f"2. the booking_details / bill {bill_id_var} has been successfully added to the database. ")
                        print(f"3. the {room_number_var} has been successfully updated to the database. ")
                        print("\n-----------------------------------------------------------------------------\n")
                        main_connector.commit()
                        tmsg.showinfo(f"welcome {name_var}","you have succesfully been added to our database. ")
                        check_in_window.destroy()
                        hotel_menu()
                    else:
                        print(f"some error occured. ")

        except TclError:
            tmsg.showerror("invalid value","only name, sex, address, pay_method can be alphanumeric others must be integers only and not empty. ")

    # -------------------------------------------------------------------------------------------------------
    # 3. makes a visited button that takes information of old customers and submit button to submit the values of the new customer [bottom frame]

    Button(bottom_frame,text="SUBMIT",borderwidth=10,relief=RAISED,font=("",15,""),bg="#FFD700",command=check_form_values).pack(side=LEFT,padx=250,pady=15)
    Button(bottom_frame,text="VISITED",borderwidth=10,relief=RAISED,font=("",15,""),bg="#1E90FF",command=lambda:check_in_visited(check_in_window)).pack(side=RIGHT,padx=250,pady=15)

    
    check_in_window.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bill_log_checkin(bill_id, room_number, customer_id, name, age, sex, book_date, book_time, payment_amount, payment_method, number_of_people): # file path change (bills.txt) | done
    '''
        makes a bill and saves it into the bill log so the manager can check who checked in at what time 

    '''

    bill = f"check-in, {bill_id}, {room_number}, {customer_id}, {name}, {age}, {sex}, {book_date}, {book_time}, {payment_amount}, {payment_method}, {number_of_people}"    
    
    bill_log_file_path = "F://aryans_code_notes//mySQL//hotel_manager_gui//bills.txt"

    with open(bill_log_file_path, 'a') as t:
        t.write("\n" + bill)

    print("\nThe bill log has successfully been updated. \n") 

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def check_out(hotel_menu_window): # file path change (title_icon, check_out_image.png) | done

    '''
        this function runs when the check button is pressed it takes information of a customer and assings them a room
        1. destroys the hotel_menu_window | done
        2. makes a window that greets the customer [top frame] | done
        3. makes a frame with a form that takes their information if the customer [form frame] | done
        4. makes a submit button to take values of the customer [bottom frame] | done
        5. checks the values if the submit button and checks the customer out | done
        6. opens a new window where old customers information is taken | done

    '''

    # -------------------------------------------------------------------------------------------------------
    # 1. destroys the hotel_menu_window 

    hotel_menu_window.destroy()

    # -------------------------------------------------------------------------------------------------------
    # main window and frames

    check_out_window = Tk()
    check_out_window.geometry("700x600")
    check_out_window.wm_iconbitmap("F://aryans_code_notes//mySQL//hotel_manager_gui//title_icon.ico")
    check_out_window.title("Hotel_manager")
    check_out_window.config(bg = "#6082B6")

    # frames
    
    top_frame = Frame(check_out_window, bg="#6082B6")
    top_frame.pack(side=TOP,fill=BOTH)

    form_frame = Frame(check_out_window, bg="#6082B6")
    form_frame.pack(side=TOP,fill=BOTH)

    bottom_frame = Frame(check_out_window, bg="#6082B6")
    bottom_frame.pack(side=BOTTOM,fill=BOTH)

    # -------------------------------------------------------------------------------------------------------
    # 2. makes a window that greets the customer [top frame] | done

    show_rooms()
    show_bookings()
    show_customer_info()
    room_image = Image.open("F://aryans_code_notes//mySQL//hotel_manager_gui//check_out_image.png").resize((200,200), Image.ANTIALIAS)
    room_image = ImageTk.PhotoImage(room_image)

    Label(top_frame, image=room_image,borderwidth=10,relief=GROOVE,anchor=CENTER).pack(side=TOP,pady=(25,0))

    Label(top_frame, text="check out customer",font=("Cascadia Mono SemiBold", 20, "bold italic"),anchor=CENTER,fg='white',bg="black",borderwidth=2,relief=RIDGE).pack(side=TOP,pady=(25,10),fill=X)

    Label(top_frame, text="enter the customer's information below\ncheck black window to see what room they are staying in.",font=("Cascadia Mono SemiBold", 15, "bold italic"),fg='white',bg="#282c39",anchor=CENTER).pack(side=TOP,pady=(10,10),fill=X)
    
    # -------------------------------------------------------------------------------------------------------
    # 3. makes a frame with a form that takes their information if the customer [form frame] | done

    bill_id_var = IntVar(name="bill_id_var")

    Label(form_frame,text="Bill_id".capitalize(),font=("Cascadia Mono SemiBold",20, "bold italic "),fg='black',bg="#6082B6").grid(row=0,column=0,padx=(100,5),pady=50,sticky=W)
    Entry(form_frame,textvariable=bill_id_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=0,column=1,padx=(150,10),pady=10,sticky=W)


    # -------------------------------------------------------------------------------------------------------
    # 5. checks the values if the submit button and checks the customer out | done

    def check_custid_values():
        try:
            if bill_id_var.get() == "":
                tmsg.showerror("invalid value", "bill_id can only be an integer and not empty. ")

            else:

                # checking if the cutomer id exsists or not 
                cursor1.execute(f"SELECT * FROM `booking_details` where bill_id = '{bill_id_var.get()}';")
                booking_data = cursor1.fetchone()

                if booking_data == None:
                    tmsg.showerror("invalid customer_Id",f"there is no bill with {bill_id_var} as their bill_id")
                else:

                    tmsg.showinfo("check booking info",f"the fetched booking_info is as follows you may cross check it with black window ({booking_data})")

                    # updating tables
                    customer_id = booking_data[-1]

                    # gtting their booking information so we can log it
                    cursor1.execute(f"SELECT * FROM `customer` WHERE customer_id = '{customer_id}';") 
                    customer_data = cursor1.fetchone()

                    tmsg.showinfo("check customer info",f"the fetched customer_info is as follows you may cross check it with black window ({customer_data})")

                    cursor1.execute(f"UPDATE `room` SET EMPTY = 'YES', occupant = NULL WHERE occupant = '{customer_id}';")
                    cursor1.execute(f"UPDATE `customer` SET room_number = '' WHERE customer_id = '{customer_id}';")


                    bill_id = booking_data[0]
                    room_number = booking_data[1]
                    name = customer_data[1]
                    age = customer_data[3]
                    sex = customer_data[4]
                    book_date = dt.datetime.now().date()
                    book_time = dt.datetime.now().time()
                    book_time = book_time.replace(microsecond=0)
                    payment_amount = booking_data[4]
                    payment_method = booking_data[5]
                    number_of_people = booking_data[6]

                    main_connector.commit()

                    # logging customers information
                    bill_log_checkout(bill_id, room_number, customer_id, name, age, sex, book_date, book_time, payment_amount, payment_method, number_of_people)

                    print("\n--------------------------------------------------------------------------------\n")
                    print("\t\t   ------- GOODBYE -------- \n")
                    print("\t --- Hope you had a good stay at our hotel --- ")
                    print("\n--------------------------------------------------------------------------------\n")
                    tmsg.showinfo(" ------- GOODBYE -------- ", "  --- Hope you had a good stay at our hotel ---  ")

                    #  -------------------------------------------------------------------------------------------------------
                    #  6. opens a new window where old customers information is taken | done
                    check_out_window.destroy()
                    hotel_menu()

        except TclError:
            tmsg.showerror("invalid value", "cust_id can oly be an integer and not empty. ")

    # -------------------------------------------------------------------------------------------------------
    # 4. makes a submit button to submit the values of the customer [bottom frame]

    Button(bottom_frame,text="SUBMIT",borderwidth=10,relief=RAISED,font=("",15,""),bg="#FFD700",command=check_custid_values).pack(side=LEFT,padx=300,pady=5)

    check_out_window.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bill_log_checkout(bill_id, room_number, customer_id, name, age, sex, book_date, book_time, payment_amount, payment_method, number_of_people): # done
    '''
        shows the user the all the user and booking info in form of a bill 

    '''

    bill = f"check-out, {bill_id}, {room_number}, {customer_id}, {name}, {age}, {sex}, {book_date}, {book_time}, {payment_amount}, {payment_method}, {number_of_people}"

    bill_log_file_path = "F://aryans_code_notes//mySQL//hotel_manager_gui//bills.txt"

    with open(bill_log_file_path, 'a') as t:
        t.write("\n" + bill)

    print("\nThe bill log has successfully been updated. \n")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def check_manager_logins(hotel_menu_window): # file path change (title_icon, manager_image.png) | done

    '''
        when the check logins buttons is pressed this function runs it shows the user the date and time of when the manager logs in to the database
        1. destroys the hotel_menu_window | done
        2. get data from the server and extract insights | done
        3. makes a window that first shows the icon and insights [top frame] | done
        4. second shows all the tabs in manager_logins.txt [bottom frame]

    '''

    # -------------------------------------------------------------------------------------------------------
    # 1. destroys the hotel_menu_window 

    hotel_menu_window.destroy()

    # -------------------------------------------------------------------------------------------------------
    # 2. get data from the server and extract insights

    cursor1.execute("SELECT COUNT(*), manager_name FROM `manager_logins` GROUP BY manager_name ORDER BY `COUNT(*)` DESC LIMIT 1; ")

    most_used = cursor1.fetchall()
    most_used_times = most_used[0][0]
    most_used_name = most_used[0][1]

    cursor1.execute("SELECT * FROM `manager_logins` ")
    content = cursor1.fetchall()

    last_used = content[-2][0]
    

    # -------------------------------------------------------------------------------------------------------
    # main window and frames

    check_manager_window = Tk()
    check_manager_window.geometry("800x700")
    check_manager_window.wm_iconbitmap("F://aryans_code_notes//mySQL//hotel_manager_gui//title_icon.ico")
    check_manager_window.title("Hotel_manager")
    check_manager_window.config(bg = "#663399")

    # frames
    
    top_frame = Frame(check_manager_window, bg="#663399")
    top_frame.pack(side=TOP,fill=BOTH)

    bottom_frame = Frame(check_manager_window, bg="#663399")
    bottom_frame.pack(side=TOP,fill=BOTH)

    # -------------------------------------------------------------------------------------------------------
    # 3. makes a window that first shows the icon and insights [top frame] | done

    manager_image = Image.open("F://aryans_code_notes//mySQL//hotel_manager_gui//manager_image.png").resize((120,120), Image.ANTIALIAS)
    manager_image = ImageTk.PhotoImage(manager_image)

    photo_label = Label(top_frame,image=manager_image,borderwidth=10,relief=RIDGE,anchor=CENTER)
    photo_label.image = manager_image
    photo_label.pack(side=TOP,pady=(25,0))

    Label(top_frame,text=f"check all manager logins",font=("Cascadia Mono SemiBold", 15, "bold italic "),fg='white',bg="#282c39",anchor=CENTER,borderwidth=5,relief=SOLID).pack(side=TOP,pady=(15,5),fill=X)
    
    Label(top_frame,text=f"most frequent manager : {most_used_name} ({most_used_times}) times\nlast used by : {last_used}",font=("Cascadia Mono SemiBold", 15, "bold italic "),fg='white',bg="#282c39",anchor=CENTER,borderwidth=5,relief=SOLID).pack(side=TOP,pady=(5,5),fill=X)

    # -------------------------------------------------------------------------------------------------------
    # 4. second shows all the tabs in manager_logins.txt [bottom frame]

    style=ttk.Style()
    style.configure("Treeview", rowheight=25)
    style.map("Treeview")

    columns = ("manager name", "login_date", "login_time")

    logins_table=ttk.Treeview(bottom_frame, height=12, columns=columns, show="headings")

    logins_table.column("manager name", anchor=CENTER, width=200)
    logins_table.column("login_date", anchor=CENTER, width=200)
    logins_table.column("login_time", anchor=CENTER, width=200)

    logins_table.heading("manager name", text="manager name", anchor=CENTER)
    logins_table.heading("login_date", text="login_date", anchor=CENTER)
    logins_table.heading("login_time", text="login_time", anchor=CENTER)

    #  reverses the data so the lastest comes first

    for index in range(len(content)-1,-1,-1):
        logins_table.insert('', index="end", values=content[index])

    scrollbary = ttk.Scrollbar(bottom_frame, orient=VERTICAL, command=logins_table.yview)
    logins_table.configure(yscroll=scrollbary.set)

    logins_table.grid(row=0,column=0,padx=(100,0),pady=(25,0))
    scrollbary.grid(row=0,column=1,sticky=NS,pady=(25,0))
    
    # -------------------------------------------------------------------------------------------------------
    # 5. opens hotel menu

    def finish_window():
        check_manager_window.destroy()
        hotel_menu()

    Button(bottom_frame,text="Go Back",relief=RAISED,bg="#90EE90",fg='black',borderwidth=10,font=("Helvetica",10,"bold italic"),command=finish_window).grid(row=2,column=0)

    check_manager_window.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def check_bills(hotel_menu_window): # file path change (title_icon, bills_image.png) | done
    '''
        when the check bills buttons is pressed this function runs it shows the user the bills of the customers when the manager logs in to the database
        1. destroys the hotel_menu_window | done
        2. get data from the server and extract insights | done
        3. makes a window that first shows the icon and insights [top frame] | done
        4. second shows all the tabs in manager_logins.txt [bottom frame] | done

    '''

    # -------------------------------------------------------------------------------------------------------
    # 1. destroys the hotel_menu_window 

    hotel_menu_window.destroy()
    
    # -------------------------------------------------------------------------------------------------------
    # 2. get data from the server and extract insights

    # extracting insights from bills.txt
    with open("F://aryans_code_notes\mySQL//hotel_manager_gui//bills.txt", 'r') as t:
        bills = t.read().split("\n")

    
    # checkin-out, bill_id, room_number, customer_id, name, age, sex, book_date, book_time, payment_amount, payment_method, number_of_people
    #      0        1            2           3         4     5    6     7           8               9              10         11

    # check-out, 123, 11, 1023, rajesh, 50, M, 2022-12-28, 18:28:20, 18000, UPI, 3

    total_profit = 0
    highest = 0
    
    for i in bills:
        i = i.split(", ")

        if int(i[9]) > highest:
            highest = int(i[9])
        
        total_profit = total_profit + int(i[9])


    # -------------------------------------------------------------------------------------------------------
    # main window and frames

    check_bills_window = Tk()
    check_bills_window.geometry("1000x700")
    check_bills_window.wm_iconbitmap("F://aryans_code_notes//mySQL//hotel_manager_gui//title_icon.ico")
    check_bills_window.title("Hotel_manager")
    check_bills_window.config(bg = "#231A14")

    # frames
    
    top_frame = Frame(check_bills_window, bg="#231A14")
    top_frame.pack(side=TOP,fill=BOTH)

    bottom_frame = Frame(check_bills_window, bg="#231A14")
    bottom_frame.pack(side=TOP,fill=BOTH)

    # -------------------------------------------------------------------------------------------------------
    # 3. makes a window that first shows the icon and insights [top frame] | done

    manager_image = Image.open("F://aryans_code_notes//mySQL//hotel_manager_gui//bills_image.jpg").resize((120,120), Image.ANTIALIAS)
    manager_image = ImageTk.PhotoImage(manager_image)

    photo_label = Label(top_frame,image=manager_image,borderwidth=10,relief=RIDGE,anchor=CENTER)
    photo_label.image = manager_image
    photo_label.pack(side=TOP,pady=(25,0))

    Label(top_frame,text=f"check all bills",font=("Cascadia Mono SemiBold", 15, "bold italic "),fg='white',bg="#282c39",anchor=CENTER,borderwidth=5,relief=SOLID).pack(side=TOP,pady=(15,5),fill=X)
    
    Label(top_frame,text=f"total profit from inogration : {total_profit}Rs/-\n highest payment from one customer: {highest}Rs/-",font=("Cascadia Mono SemiBold", 15, "bold italic "),fg='white',bg="#282c39",anchor=CENTER,borderwidth=5,relief=SOLID).pack(side=TOP,pady=(5,5),fill=X)

    # -------------------------------------------------------------------------------------------------------
    # 4. second shows all the tabs in manager_logins.txt [bottom frame]

    style=ttk.Style()
    style.configure("Treeview", rowheight=25)
    style.map("Treeview")

    columns = ( "checkin-out", "bill_id", "room_num", "cust_id", "name", "age", "sex", "book_date", "book_time", "pay_amt", "pay_method", "no of people")

    logins_table=ttk.Treeview(bottom_frame, height=12, columns=columns, show="headings")

    logins_table.column("checkin-out", anchor=CENTER, width=80)
    logins_table.column("bill_id", anchor=CENTER, width=70)
    logins_table.column("room_num", anchor=CENTER, width=70)
    logins_table.column("cust_id", anchor=CENTER, width=70)
    logins_table.column("name", anchor=CENTER, width=50)
    logins_table.column("age", anchor=CENTER, width=50)
    logins_table.column("sex", anchor=CENTER, width=50)
    logins_table.column("book_date", anchor=CENTER, width=70)
    logins_table.column("book_time", anchor=CENTER, width=70)
    logins_table.column("pay_amt", anchor=CENTER, width=70)
    logins_table.column("pay_method", anchor=CENTER, width=80)
    logins_table.column("no of people", anchor=CENTER, width=90)

    logins_table.heading("checkin-out", text="checkin-out", anchor=CENTER)
    logins_table.heading("bill_id", text="bill_id", anchor=CENTER)
    logins_table.heading("room_num", text="room_num", anchor=CENTER)
    logins_table.heading("cust_id", text="cust_id", anchor=CENTER)
    logins_table.heading("name", text="name", anchor=CENTER)
    logins_table.heading("age", text="age", anchor=CENTER)
    logins_table.heading("sex", text="sex", anchor=CENTER)
    logins_table.heading("book_date", text="book_date", anchor=CENTER)
    logins_table.heading("book_time", text="book_time", anchor=CENTER)
    logins_table.heading("pay_amt", text="pay_amt", anchor=CENTER)
    logins_table.heading("pay_method", text="pay_method", anchor=CENTER)
    logins_table.heading("no of people", text="no of people", anchor=CENTER)
    
    for index in range(len(bills)-1,-1,-1):
        logins_table.insert('', index="end", values=bills[index])

    scrollbary = ttk.Scrollbar(bottom_frame, orient=VERTICAL, command=logins_table.yview)
    logins_table.configure(yscroll=scrollbary.set)

    logins_table.grid(row=0,column=0,padx=(100,0),pady=(25,0))
    scrollbary.grid(row=0,column=1,sticky=NS,pady=(25,0))

    # -------------------------------------------------------------------------------------------------------
    # 5. opens hotel menu

    def finish_window():
        check_bills_window.destroy()
        hotel_menu()

    Button(bottom_frame,text="Go Back",relief=RAISED,bg="#90EE90",fg='black',borderwidth=10,font=("Helvetica",10,"bold italic"),command=finish_window).grid(row=2,column=0)

    check_bills_window.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_room(hotel_menu_window): # file path change (title_icon, add_rooms_image) | done

    '''
        when the add room button is pressed this window pops up it adds new rooms to the database
        1. destroys the hotel_menu_window so no errors occure | done
        2. make a window with a form asking for the new rooms information [top frame] | done
        3. takes the information as a form [form frame] | done
        4. make a button to submit these values and checks for errors [bottom] | done
        5. submit these values to the database | done
        6. destroys itself and opens the hotel_menu again so the user can do other tasks | done
    '''

    # -------------------------------------------------------------------------------------------------------
    # 1. destroys the hotel_menu_window so no errors occure
    
    hotel_menu_window.destroy()

    # -------------------------------------------------------------------------------------------------------
    # main window and frames

    add_room_window = Tk()
    add_room_window.geometry("800x700")
    add_room_window.wm_iconbitmap("F://aryans_code_notes//mySQL//hotel_manager_gui//title_icon.ico")
    add_room_window.title("Hotel_manager")
    add_room_window.config(bg = "#008B8B")

    # frames
    
    top_frame = Frame(add_room_window, bg="#008B8B")
    top_frame.pack(side=TOP,fill=BOTH)

    form_frame = Frame(add_room_window, bg="#008B8B")
    form_frame.pack(side=TOP,fill=BOTH)

    bottom_frame = Frame(add_room_window, bg="#008B8B")
    bottom_frame.pack(side=BOTTOM,fill=BOTH)

    # -------------------------------------------------------------------------------------------------------
    # 2. make a window with a form asking for the new rooms information [top frame]

    room_image = Image.open("F://aryans_code_notes//mySQL//hotel_manager_gui//add_rooms_image.png").resize((100,100), Image.ANTIALIAS)
    room_image = ImageTk.PhotoImage(room_image)

    Label(top_frame, image=room_image,borderwidth=10,relief=GROOVE,anchor=CENTER).pack(side=TOP,pady=(25,0))

    Label(top_frame, text="add a new room",font=("Cascadia Mono SemiBold", 27, "bold italic"),anchor=CENTER,bg='black',fg='white',borderwidth=5,relief=RIDGE).pack(side=TOP,pady=(25,10),fill=X)

    Label(top_frame, text="enter the new room's information below",font=("Cascadia Mono SemiBold", 20, "bold italic"),fg='white',bg="#282c39",anchor=CENTER).pack(side=TOP,pady=(10,10),fill=X)
    
    Label(top_frame, text="NOTE: room_number, room_rate\ncan have only integer values",font=("Cascadia Mono SemiBold", 20, "bold italic"),fg='white',bg="#282c39",anchor=CENTER).pack(side=TOP,pady=(10,25),fill=X)

    # -------------------------------------------------------------------------------------------------------
    # 3. takes the information as a form [bottom frame]
    
    room_number_var = IntVar()
    room_type_var = StringVar()
    room_rate_var = IntVar()

    Label(form_frame,text="room_number",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#008B8B").grid(row=0,column=0,padx=(150,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=room_number_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=0,column=1,padx=(150,10),pady=10,sticky=W)

    Label(form_frame,text="room_type",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#008B8B").grid(row=1,column=0,padx=(150,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=room_type_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=1,column=1,padx=(150,10),pady=10,sticky=W)

    Label(form_frame,text="room_rate",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#008B8B").grid(row=2,column=0,padx=(150,5),pady=10,sticky=W)
    Entry(form_frame,textvariable=room_rate_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=2,column=1,padx=(150,10),pady=10,sticky=W)


    # -------------------------------------------------------------------------------------------------------
    # 5. submit these values to the database

    def check_room_values():
        try:

            if room_type_var.get() == "":
                tmsg.showerror("incorrect values for room_type", "room_type must not be empty")

            else:

                cursor1.execute(f"INSERT INTO room  VALUES ({room_number_var.get()},'{room_type_var.get()}',{room_rate_var.get()},NULL,'YES'); ")

                # checking if the value has been inserted sucessfully
                if cursor1.rowcount > 0:
                    tmsg.showinfo("SUCCESS",f"{room_number_var.get()} {room_type_var.get()} {room_rate_var.get()} was added successfuly. ")
                    main_connector.commit()

                    # -------------------------------------------------------------------------------------------------------
                    # 6. destroys itself and opens the hotel_menu again so the user can do other tasks

                    add_room_window.destroy()
                    hotel_menu()

                else:
                    tmsg.showerror("FAILED","couldnt add room to the database. ")

        except TclError:
            tmsg.showerror("invalid value","room_rate, room_number must be integers only and not empty. ")


    # -------------------------------------------------------------------------------------------------------
    # 4. make a button to submit these values and checks for errors [bottom frame]

    Button(text="SUBMIT",borderwidth=10,relief=RAISED,font=("",30,""),bg="#1E90FF",command=check_room_values).pack(anchor=S,pady=15)

    add_room_window.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def delete_room(hotel_menu_window): # file path change (title_icon, remove_room) | done
    '''
        when the remove room button is pressed this window pops up it adds new rooms to the database | done
        1. destroys the hotel_menu_window so no errors occure | done
        2. show the user a list of all rooms so they can select which one to delete | done
        3. make a window with a form asking for the new rooms information [top frame] | done
        4. takes the given infoirmation and handles error [form frame] | done
        5. deletes the room from the database  | done
        6. destroys itself and opens the hotel_menu again so the user can do other tasks | done

    '''

    # -------------------------------------------------------------------------------------------------------
    # 1. destroys the hotel_menu_window so no errors occure

    hotel_menu_window.destroy()

    # -------------------------------------------------------------------------------------------------------
    # 2. show the user a list of all rooms so they can select which one to delete

    show_rooms()

    # -------------------------------------------------------------------------------------------------------
    # main window and frames

    remove_room_window = Tk()
    remove_room_window.geometry("800x700")
    remove_room_window.wm_iconbitmap("F://aryans_code_notes//mySQL//hotel_manager_gui//title_icon.ico")
    remove_room_window.title("Hotel_manager")
    remove_room_window.config(bg = "#FF6347")

    # frames
    
    top_frame1 = Frame(remove_room_window, bg="#FF6347")
    top_frame1.pack(side=TOP,fill=BOTH)

    form_frame1 = Frame(remove_room_window, bg="#FF6347")
    form_frame1.pack(side=TOP,fill=BOTH)

    bottom_frame1 = Frame(remove_room_window, bg="#FF6347")
    bottom_frame1.pack(side=BOTTOM,fill=BOTH)

    # -------------------------------------------------------------------------------------------------------
    # 3. make a window with a form asking for the new rooms information [top frame]

    hotel_image = Image.open("F://aryans_code_notes//mySQL//hotel_manager_gui//remove_room.jpg").resize((150,150),Image.ANTIALIAS)
    hotel_image = ImageTk.PhotoImage(hotel_image)

    photo = Label(top_frame1,image=hotel_image,borderwidth=10,relief=GROOVE,anchor=CENTER)
    photo.image = hotel_image
    photo.pack(side=TOP,pady=(25,0))

    Label(top_frame1, text="remove room from hotel",font=("Cascadia Mono SemiBold", 27, "bold italic"),anchor=CENTER,bg='black',fg='white',borderwidth=5,relief=RIDGE).pack(side=TOP,pady=(25,25),fill=X)

    Label(top_frame1, text="check black window for room's details",font=("Cascadia Mono SemiBold", 20, "bold italic"),fg='white',bg="#282c39",anchor=CENTER).pack(side=TOP,pady=(15,15),fill=X)
    
    Label(top_frame1, text="NOTE: room_number can have only integer values",font=("Cascadia Mono SemiBold", 20, "bold italic"),fg='white',bg="#282c39",anchor=CENTER).pack(side=TOP,pady=(15,25),fill=X)

    # -------------------------------------------------------------------------------------------------------
    # 4. takes the given infoirmation and handles error [form frame]
    room_number_var = IntVar()

    Label(form_frame1,text="room_number",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#FF6347").grid(row=0,column=0,padx=(150,5),pady=25,sticky=W)
    Entry(form_frame1,textvariable=room_number_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=0,column=1,padx=(150,10),pady=25,sticky=W)


    # -------------------------------------------------------------------------------------------------------
    # 5. deletes the room from the database

    def check_room_values2():
        try:

            if room_number_var.get() == "":
                tmsg.showerror("incorrect value for room_number", "room_number must not be empty")

            else:

                cursor1.execute(f"DELETE FROM room WHERE room_number = {room_number_var.get()}")

                # checking if the value has been inserted sucessfully
                if cursor1.rowcount > 0:
                    tmsg.showinfo("SUCCESS",f"{room_number_var.get()} was removed from the hotel successfuly. ")
                    main_connector.commit()

                    # -------------------------------------------------------------------------------------------------------
                    # 6. destroys itself and opens the hotel_menu again so the user can do other tasks

                    remove_room_window.destroy()
                    hotel_menu()

                else:
                    tmsg.showerror("FAILED","couldnt delete room from the database. (it may not exsist check black window)")

        except TclError:
            tmsg.showerror("invalid value","room_number must be integers only and not empty. ")

    # -------------------------------------------------------------------------------------------------------
    # 4. make a button to submit these values and checks for errors [bottom frame]

    Button(text="SUBMIT",borderwidth=10,relief=RAISED,font=("",30,""),bg="#1E90FF",command=check_room_values2).pack(anchor=S,pady=(50,16))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def show_rooms(): # done
    '''
        this function shows the manager the status and info of all rooms if the 'check room status' option is selected
        1. should show the info of all the rooms in a nice clean way | done
        2. if too many rooms the manager should have a search room by room number option | this should be optional

    '''

    # getting the information from the database as a list filled with tuples
    cursor1.execute("SELECT * FROM room")
    all_rooms_data = cursor1.fetchall()
    
    print("\n----------------------------------------------------------------------\n")
    print("The information of the rooms in the hotel are as follows:- \n")
    print("if the occupant row is empty, it means that it is empty. \n")

    # showing the data in a tablular format using the tabulate module
    print(tabulate(all_rooms_data, headers=['room_number', 'room_type', 'room_rate', 'occupant', 'empty'], tablefmt='outline', numalign='center'))
    print("\n----------------------------------------------------------------------\n")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def show_customer_info(): # done
    '''
        shows the manager the information of all users like name and room they stay in

    '''

    # getting the information from the database as a list filled with tuples
    cursor1.execute("SELECT * FROM `customer` ")
    all_customers_data = cursor1.fetchall()

    print("\n----------------------------------------------------------------------\n")
    print("The information of the customers who stayed hotel are as follows:- \n")

    # showing the data in a tablular format using the tabulate module
    print(tabulate(all_customers_data, headers=['customer_id','name','phone', 'age', 'sex','address','adhaar_number','room_number','bill_id'], numalign='centre', tablefmt='outline'))
    print("\n----------------------------------------------------------------------\n")
    print(" ---------------- maxise the window to look at table properly ---------------- ")
    print("\n----------------------------------------------------------------------\n")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def show_bookings(): # done
    '''
        shows the manager the information of all past bookings and and ongoing ones

    '''

    # getting the information from the database as a list filled with tuples
    cursor1.execute("SELECT * FROM `booking_details` ")
    all_customers_data = cursor1.fetchall()

    print("\n----------------------------------------------------------------------\n")
    print("The information of the bookings who stayed hotel are as follows:- \n")

    # showing the data in a tablular format using the tabulate module
    print(tabulate(all_customers_data, headers=['bill_id','room_number', 'book_date', 'book_time', 'payment_amount', 'payment_method', 'number_of_people', 'customer_id'], numalign='centre', tablefmt='outline'))
    print("\n----------------------------------------------------------------------\n")
    print(" ---------------- maxise the window to look at table properly ---------------- ")
    print("\n----------------------------------------------------------------------\n")
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def hotel_menu(): # file path change (title_icon, quit_button) | done

    ''' 
        
        this is the hotel menu this shows all the options a manager can choose and the main window of the program all functions end and come back to this window
        1. show the manager the total number of occupied and free and total rooms in the hotel (occupied percentage) [top frame] | done
        2. shows all the buttons for diffrent choices  [bottom frame] | done
        3. shows the manager the current date and time in status bar [status_bar] | done

    '''

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # main window and frames
    
    hotel_menu_window = Tk()
    hotel_menu_window.geometry("900x770")
    hotel_menu_window.wm_iconbitmap("F://aryans_code_notes//mySQL//hotel_manager_gui//title_icon.ico")
    hotel_menu_window.title("Hotel_manager")
    hotel_menu_window.config(bg = "#191970")


    # all the frames 
    top_frame = Frame(hotel_menu_window,bg="#191970")
    top_frame.pack(side=TOP,fill=BOTH)

    bottom_frame = Frame(hotel_menu_window,bg="#191970")
    bottom_frame.pack(side=TOP,fill=BOTH)

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # 1. show the manager the total number of occupied and free and total rooms in the hotel (occupied percentage) [top frame]

    # sql query to get all the rooms 
    cursor1.execute("SELECT * FROM room")
    rooms_data = cursor1.fetchall()

    # sql query to get all avaible rooms
    cursor1.execute("SELECT COUNT(*) FROM `room` WHERE EMPTY = 'NO';")
    unavaible_rooms = cursor1.fetchone()

    # sql query to get all avaible rooms
    cursor1.execute("SELECT COUNT(*) FROM `room` WHERE EMPTY = 'YES';")
    avaible_rooms = cursor1.fetchone()


    Label(top_frame,text="HOTEL_MENU",font=("Cascadia Mono SemiBold", 27, "bold italic"),anchor=CENTER,bg='black',fg='white',borderwidth=5,relief=SOLID).pack(anchor=NE,pady=10,fill=X)

    Label(top_frame,text=f"total rooms in the hotel: {len(rooms_data)}",font=("Cascadia Mono SemiBold", 15, "bold italic "),fg='white',bg="#282c39",anchor=CENTER,borderwidth=5,relief=SOLID).pack(side=TOP,pady=(15,5),fill=X)
    
    Label(top_frame,text=f"Empty: {unavaible_rooms[0]} | occupied : {avaible_rooms[0]}",font=("Cascadia Mono SemiBold", 15, "bold italic "),fg='white',bg="#282c39",anchor=CENTER,borderwidth=5,relief=SOLID).pack(side=TOP,pady=(5,5),fill=X)
    
    Label(top_frame,text=f"IMPORTANT NOTE: (this is the menu window)\nfrom here you can click the buttons down below to manage your hotel\n(the black window in the back is the command line)\nyou will see all the tables information\nand errors in if the program crashes",font=("Cascadia Mono SemiBold", 15, "bold italic"),fg='white',bg="#282c39",anchor=CENTER,borderwidth=5,relief=SOLID).pack(side=TOP,pady=(5,5),fill=X)

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # 2. shows all the buttons for diffrent choices  [bottom frame]

    qbutton = Image.open("F://aryans_code_notes//mySQL//hotel_manager_gui//quit_button.png").resize((150,50), Image.ANTIALIAS)
    qbutton = ImageTk.PhotoImage(qbutton)

    Button(bottom_frame,text="check-in",relief=RAISED,bg="#90EE90",fg='black',borderwidth=10,font=("Helvetica",20,"bold italic"),command=lambda: check_in(hotel_menu_window)).grid(row=0,column=0,padx=(70,50),pady=20,sticky=W)
    Button(bottom_frame,text="check-out",relief=RAISED,bg="#90EE90",fg='black',borderwidth=10,font=("Helvetica",20,"bold italic"),command=lambda: check_out(hotel_menu_window)).grid(row=0,column=1,padx=(20,50),pady=20,sticky=W)
    Button(bottom_frame,text="show rooms",relief=RAISED,bg="#FFA500",fg='black',borderwidth=10,font=("Helvetica",20,"bold italic"),command=show_rooms).grid(row=0,column=2,padx=20,pady=20,sticky=W)
    Button(bottom_frame,text="check logins",relief=RAISED,bg="#FF69B4",fg='black',borderwidth=10,font=("Helvetica",20,"bold italic"),command=lambda:check_manager_logins(hotel_menu_window)).grid(row=1,column=0,padx=(70,50),pady=20,sticky=W)
    Button(bottom_frame,text="check bills",relief=RAISED,bg="#FF69B4",fg='black',borderwidth=10,font=("Helvetica",20,"bold italic"),command=lambda: check_bills(hotel_menu_window)).grid(row=1,column=1,padx=(20,50),pady=20,sticky=W)
    Button(bottom_frame,text="show customers",relief=RAISED,bg="#FFA500",fg='black',borderwidth=10,font=("Helvetica",20,"bold italic"),command=show_customer_info).grid(row=1,column=2,padx=20,pady=20,sticky=W)
    Button(bottom_frame,text="add room",relief=RAISED,bg="#DC143C",fg='black',borderwidth=10,font=("Helvetica",20,"bold italic"),command=lambda: add_room(hotel_menu_window)).grid(row=2,column=0,padx=(70,50),pady=20,sticky=W)
    Button(bottom_frame,text="remove room",relief=RAISED,bg="#DC143C",fg='black',borderwidth=10,font=("Helvetica",20,"bold italic"),command=lambda: delete_room(hotel_menu_window)).grid(row=2,column=1,padx=(20,50),pady=20,sticky=W)
    Button(bottom_frame,text="show bookings",relief=RAISED,bg="#FFA500",fg='black',borderwidth=10,font=("Helvetica",20,"bold italic"),command=show_bookings).grid(row=2,column=2,padx=20,pady=20,sticky=W)
    Button(bottom_frame,image=qbutton,relief=RAISED,borderwidth=0,command=hotel_menu_window.destroy).grid(row=3,column=1,padx=20,pady=5)

    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print("this is the command line you will all the information of tables (rooms, customers, bookings, managers) for example -----\n")
    print("\n----------------------------------------------------------------------\n")
    show_rooms()

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # 3. shows the manager the current date and time in status bar [status_bar]

    Label(text=f"made by : aryan rathore  |  contactinfo : aryanrathore13572002@gmal.com  |  time: {dt.datetime.now().time()}  |  date: {dt.datetime.now().date()}",font=(" 10 "),borderwidth=5,relief=SUNKEN).pack(side=BOTTOM,fill=X)

    hotel_menu_window.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_manager(root): # file path change title_icon.ico | done

    '''
        when the add manager button is pressed on the manager_login_window this function runs it adds new managers into the database

        0. destroy the prev window | done
        1. opens a new window which takes the username and password of the new manager | done
        2. ask for a exsisting managers password and adds the new login info to the database | done
        3. commits the changes to the database and opens the login window again | done

    '''

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # 0. destroy the prev window | done

    root.destroy()

    # ----------------------------------------------------------------------------------------------------------------------------------------
    # 1. opens a new window which takes the username and password of the new manager | done

    add_manager_window = Tk()
    add_manager_window.geometry("800x600")
    add_manager_window.wm_iconbitmap("F://aryans_code_notes//mySQL//hotel_manager_gui//title_icon.ico")
    add_manager_window.title("Hotel_manager")
    add_manager_window.config(bg = "#460D6C")

    Label(add_manager_window,text="add a new manager",font=("Cascadia Mono SemiBold", 27, "bold italic"),anchor=CENTER,bg='black',fg='white',borderwidth=5,relief=RIDGE).pack(side=TOP,pady=(100,0),fill=X)

    Label(add_manager_window,text="enter new username and passowrd",font=("Cascadia Mono SemiBold", 20, "bold italic "),fg='white',bg="#282c39",anchor=CENTER).pack(side=TOP,pady=(25,25),fill=X)

    new_username_var = StringVar()
    new_password_var = StringVar()
    prev_password = StringVar()

    Label(add_manager_window,text="username",font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#460D6C").pack(anchor=CENTER,padx=(10,25),fill=X)
    Entry(add_manager_window,textvariable=new_username_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).pack(anchor=CENTER,pady=(10,25))

    Label(add_manager_window,text="password",font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#460D6C").pack(anchor=CENTER,padx=(20,20),fill=X)
    Entry(add_manager_window,textvariable=new_password_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).pack(anchor=CENTER)

    Label(add_manager_window,text="old manager password",font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#460D6C").pack(anchor=CENTER,pady=(20,0),fill=X)
    Entry(add_manager_window,textvariable=prev_password,font=("Cascadia Mono SemiBold",15, "bold italic ")).pack(anchor=CENTER)


    # ----------------------------------------------------------------------------------------------------------------------------------------
    # ask for a exsisting managers password and adds the new login info to the database | done

    def check_newinfo():
        
        try:
            if new_username_var.get() == "":
                tmsg.showerror("Invalid login information","Please enter a username. ")
            elif new_password_var.get() == "":
                tmsg.showerror("Invalid login information","Please enter a password. ")
            elif prev_password.get() == "":
                tmsg.showerror("Invalid login information","plaease enter an exsisting manager's password")
            else:
                cursor1.execute(f"SELECT * FROM `managers` WHERE upassword = PASSWORD('{prev_password.get()}');")
                result = cursor1.fetchone()

                if result == None:
                    tmsg.showerror("wrong credentials","exsisting manager's password is invalid correct it. ")
                else:
                    try:

                        # 3. commits the changes to the database and opens the login window again | done
                        
                        cursor1.execute(f"INSERT INTO `managers` VALUES('{new_username_var.get()}', PASSWORD('{new_password_var.get()}'));")
                        main_connector.commit()
                        tmsg.showinfo("success","manager is added to database succesfuly. ")
                        add_manager_window.destroy()
                        manager_login_window()

                    except:
                        tmsg.showerror("database error", "could not add manager details to the database. ")
                    

        except:
            tmsg.showerror("connection error","could not connect to the database. ")

    Button(add_manager_window,text="submit", bg='blue', fg='white', borderwidth=5,relief=RAISED,font=("Cascadia Mono SemiBold",15, "bold italic "),command=check_newinfo).pack(side=BOTTOM,pady=(25,10))

    add_manager_window.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def manager_login_window(): # file path change title_icon.ico, hotel_icon.png | done 

    ''' This function runs first whenever the program runs
        1. shows the title and icon of the hotel manager | done
        2. ask the manager to enter their username and password | done 
        3. checks the username and password of the manager from the database | done 
        4. calls the add manager function if the add manager button is pressed | done
        5. destroys the root window and opens the hotel menu | done
        6. adds the manager login time and date to the database  | done '''

    
    # ----------------------------------------------------------------------------------------------------------------------------------------
    # 1. shows the title and icon of the hotel manager

    root = Tk()
    root.geometry("800x600")
    root.wm_iconbitmap("F://aryans_code_notes//mySQL//hotel_manager_gui//title_icon.ico")
    root.title("Hotel_manager")
    root.config(bg = "#282c39")

    top_frame = Frame(root, bg = "#282c39")
    top_frame.pack(fill=X)    

    hotel_image = Image.open("F://aryans_code_notes//mySQL//hotel_manager_gui//hotel_icon.png").resize((100,100), Image.ANTIALIAS)
    hotel_image = ImageTk.PhotoImage(hotel_image)

    Label(top_frame,image=hotel_image,borderwidth=2,relief=RIDGE,anchor=CENTER).pack(side=TOP,pady=(25,0))

    Label(top_frame,text="welcome to Hotel_manager",font=("Cascadia Mono SemiBold", 27, "bold italic"),anchor=CENTER,bg='black',fg='white',borderwidth=5,relief=RIDGE).pack(side=TOP,pady=(25,0),fill=X)

    Label(top_frame,text="enter username and passowrd",font=("Cascadia Mono SemiBold", 20, "bold italic"),fg='white',bg="#282c39",anchor=CENTER).pack(side=TOP,pady=(10,25),fill=X)

    # --------------------------------------------------------------------------------------------------------
    # 2. ask the manager to enter their username and password

    username_var = StringVar()
    password_var = StringVar()

    Label(top_frame,text="username",font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#282c39").pack(anchor=CENTER,padx=(10,25),fill=X)
    Entry(top_frame,textvariable=username_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).pack(anchor=CENTER,pady=(10,25))

    Label(top_frame,text="password",font=("Cascadia Mono SemiBold",15, "bold italic "),fg='white',bg="#282c39").pack(anchor=CENTER,padx=(20,20),fill=X)
    Entry(top_frame,textvariable=password_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).pack(anchor=CENTER)


    # --------------------------------------------------------------------------------------------------------
    # 3. checks the username and password of the manager from the database

    def check_login_password(root):
        
        # try:
        if username_var.get() == "":
            tmsg.showerror("Invalid login information","Please enter a username. ")
        elif password_var.get() == "":
            tmsg.showerror("Invalid login information","Please enter a password. ")
        else:
            cursor1.execute(f"SELECT * FROM `managers` WHERE username = '{username_var.get()}' AND upassword = PASSWORD('{password_var.get()}');")
            result = cursor1.fetchone()

            if result == None:
                tmsg.showerror("Incorrect username/password","your login credentials are invalid please correct yourself. ")
            else:

                # --------------------------------------------------------------------------------------------------------
                # 6. adds the manager login time and date to the database

                time1 = dt.datetime.now().time()
                time1 = time1.replace(microsecond=0)
                cursor1.execute(f"INSERT INTO manager_logins VALUES ('{username_var.get()}', '{dt.datetime.now().date()}', '{time1}')")

                if cursor1.rowcount > 0:
                    print('success')
                    main_connector.commit()
                else:
                    print('fail')

                # --------------------------------------------------------------------------------------------------------
                # 5. destroys the root window and opens the hotel menu

                root.destroy()
                hotel_menu()
                

        # except:
        #     tmsg.showerror("connection error","could not connect to the database. ")

    Button(text="submit", bg='blue', fg='white', borderwidth=5,relief=RAISED,font=("Cascadia Mono SemiBold",15, "bold italic "),command=lambda : check_login_password(root)).pack(side=BOTTOM,pady=(0,10))
    
    # --------------------------------------------------------------------------------------------------------
    # 4. calls the add manager function if the add manager button is pressed

    Button(text="add new manager", bg='blue', fg='white', borderwidth=5,relief=RAISED,font=("Cascadia Mono SemiBold",15, "bold italic "),command=lambda: add_manager(root)).pack(side=BOTTOM,pady=(0,10))

    root.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    try:

        # connecting to the database:- 
        main_connector = c.connect(host="localhost", user="root", password="", database="hotel_database")
        cursor1 = main_connector.cursor(buffered=True)

        print(" ------------ DO NOT CLOSE THIS WINDOW ------------ ")
        manager_login_window()
            
    except:
        tmsg.showerror("connection error","could not connect to the database. ")
        quit()