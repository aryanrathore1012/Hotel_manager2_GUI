# Hotel_manager2_GUI

---- THIS PROJECT IS FREE AND OPEN SOURCE IF YOU ARE A COLLAGE STUDENT FEEL FREE TO USE MY CODE FOR YOUR ASSINGEMNTS AND ADD MORE TO THIS ---- ---- MADE BY ARYAN RATHORE LINKEDIN- https://www.linkedin.com/in/aryan-rathore-b15459215/ aryanrathore13572002@gmail.com ----

TIME TOOK TO MAKE THIS :- 29-DEC-2022 TO 12-DEC-2022, 2 WEEKS

DISCRIPTION:-

a hotel database management system that uses MySQL for the database (stroring and managing the data) and Python for data processing and output  (using tkinter GUI). this software provides a powerful and flexible tool for managing the data and operations of a hotel.

I HAVE MADE A DEMO VIDEO OF THE PROJECT WHICH IS UPLOADED TO THE REPOSITORY MAKE SURE YOU WATCH IT FIRST

INPUTS AND OUTPUTS:-

![image](https://user-images.githubusercontent.com/91218998/212022169-1eb98453-4f24-4c2b-87b4-18eb89b525b8.png)

![image](https://user-images.githubusercontent.com/91218998/212022273-0fedd3c4-037a-410c-beb1-24100538c155.png)

![image](https://user-images.githubusercontent.com/91218998/212022395-b8b37e19-0535-43f5-b68d-6bbe3a8c106c.png)

![image](https://user-images.githubusercontent.com/91218998/212022481-f9129755-e0fb-4f2b-a70e-cea955140025.png)

![image](https://user-images.githubusercontent.com/91218998/212022618-111bc778-67f1-4dc3-8dac-e88df5588d27.png)

![image](https://user-images.githubusercontent.com/91218998/212022720-bba5b286-ced3-4128-85e2-d159bd3c8c99.png)

an example of error handling (user entering nothing or string when an integer value is asked) :-

![image](https://user-images.githubusercontent.com/91218998/212022947-7e7eb630-b8a6-43be-9e68-ddcaac46babf.png)

THE PROGRAM SHOWS THE CUSTOMER WELCOME AND GOODBEY MSGS WHEN A CUSTOMER CHECKINS OR CHECKOUTS

![image](https://user-images.githubusercontent.com/91218998/212023351-a23417d8-5114-4b3a-93ec-9ee7a0d0ec32.png)

![image](https://user-images.githubusercontent.com/91218998/212023416-a3430d9c-38ff-4f3f-ab28-8673d169ec97.png)

CAN SHOW CUSTOMERS, ROOMS, BOOKINGS DETAILS

![image](https://user-images.githubusercontent.com/91218998/212024470-a2c3cc3b-5ef1-4a3e-b654-b9c306f4acbe.png)

![image](https://user-images.githubusercontent.com/91218998/212024618-eaf750db-b07e-4e5e-b740-8ed2b9b82378.png)

FEATURES :-

1. manages data like customer, room, and booking details by storing/deleting/adding/updating the data in a mysql database.

2. the database now has managers and manager_logins table keep a track of the managers ENCRYPTED PASSWORDS and LOGIN TIMES

3. has text files that keep a track customers bills using PYTHON fileIO

4. WIMP TKINTER GUI simple inputs so anyone can use it as long as they can read

5. has encrypted passwords so no one can access the database other than the managers

WHAT IS A HOTEL_DATABASE:-

A hotel database management system is a software application that is used to store, organize, and manage the data related to a hotel's operations. It typically includes information about guests, rooms, reservations, and staff, as well as financial and accounting data.

THE hotel_database HAS 5 TABLES:-

customer :- this table has the information of the customer like their id and what room they are staying in

room :- this table has the information of the rooms like room_type and who is staying in the room (via customer id)

booking_details :- this table has the information of the booking datials of the customer like their pay amount method and no. of people they are staying with
    
manager_loginss :- this table has the information of manager;s login date and time 
    
managers :- this table has the information of the managers username and passwords 

THE SOFTWARE USES 2 THINGS TO OPERATE:-

    PYTHON:-

The system may also use Python to process the data from the database and present it to the user. Python is a high-level programming language that is known for its readability and simplicity. It can be used to write scripts that can extract data from the database, perform calculations and analysis, and generate reports and other outputs.

    MYSQL:-

The system may use MySQL as the database to store the data. MySQL is a popular open-source relational database management system that is widely used in the hospitality industry. It allows for efficient storage and retrieval of data and offers robust security features to protect sensitive information.

HOW TO SETUP THE hotel_manager2 :-

IMPORTANT
0. WATCH THE DEMO VIDEO THE MANAGERS PASSWORD IS AS FOLLOWS :- USERNAME = 1, PASSWORD = 1

1. IMPORT THE MYSQL DATABASE NAMED hotel_database

2. there is 1 text file and 15 PNGs that keep the track of the following info:-

2A. BILLS.TXT this file keeps track of the when a user is checking in or out with this it also keeps their booking information if the manager needs

2B. PNGs that are images in the windows

MOST_IMPORTANT
3. now that you have imported the database there is only 1 thing you need to do that is TO CHACNGE THE FILE PATH OF BILLS.TXT AND 51 PNGs in your hotel_manager python file i have mentioned in the comments which which functions will require a file path change and what functions use them.

4. after importing the database and changing the file paths you are all set and done.

5. every function has a docstring which disribes how the function works and what it does. 

6. i tried to keep the program simple so anyone who knows the basics of python can solve it 
