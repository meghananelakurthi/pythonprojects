import mysql.connector as sqct
import random
def createdb():
    global mydb
    global mycursor
    
    mydb=sqct.connect(host="localhost",user="root",password="pythoninternship@123",database="train")
    if mydb.is_connected():
        print("\t\t\t WELCOME TO TRAINTICKETBOOKING .")
    mycursor=mydb.cursor()
    cmd1 = "create table if not exists Traintb (sno int(100)  primary key,Name varchar(100),from1 varchar(100),TO1 varchar(100),TRAIN_NO varchar(200),TRAIN_NAME varchar(200),train_time varchar(100), SEATS_AVALIABLE varchar(200),cost int(100))"
    mycursor.execute(cmd1)
createdb()
def display_ACSeats():
    
    print("====================================================================================================================")
    print("| DESTINATION PLACE  ARRIVAL PLACE  TRAIN NO   TRAIN NAME           TRAIN TIMINGS       TICKET PRICE  SEATS AVALIABLE|")
    print("====================================================================================================================")

    print("     VISHAKAPATNAM    NELLORE        12347    VishakaExpress         10:55am-3:15am          300rs           300       ")
    print("     ANANTAPUR        HYDERABAD      34567   BhuvaneswarExpress      3:15am-7:30pm           450rs           200       ")
    print("      TIRUPATI       CHENNAI         16054    ChennaiExpress         4:10am-5:40pm           500rs           100       ")
    print("      BANGLORE       CHENNAICENTRAL  45678   VenkatadriExpress       6:20am-8:54pm           390rs           150       ")
    print("     KURNOOL         KAVALI          20895    seshadriExpress        9:40pm-12:55am          450rs           250       ")
    print("==================================================================================================================")

def AC_passengers():
    
    cmd2 = "select * from Traintb"
    mycursor.execute(cmd2)
    r2 = mycursor.fetchall()
    
    print("============================================================================================================================")
    print("|SNO     NAME    DESTINATION PLACE       ARRIVAL PLACE      TRAIN NO      TRAIN NAME        TRAIN TIMINGS     SEATS    COST|")
    print("============================================================================================================================")

    for i in range(len(r2)): 
        print("| ",end="")
        print(str(r2[i][0]).ljust(18," "),end=" ") 
        print(r2[i][1].ljust(20," "),end=" ") 
        print(r2[i][2].ljust(22," "),end=" ")                  
        print(r2[i][3].ljust(14," "),end=" ")               
        print(str(r2[i][4]).ljust(25," "),end=" ")
        print(r2[i][5].ljust(20," "),end=" ")
        print(r2[i][6].ljust(18," "),end=" ")
        print(str(r2[i][7]).ljust(6," "),end="|")
        print(str(r2[i][8]).ljust(7," "),end="|") 
        print()

    print("=============================================================================================================================")

price1,price2,price3,price4,price5 = 300,450,500,390,450

def Booking_ACSeats():
    global seats
    global cost
    global name
    sno = int(input("Enter the sno: "))
    name = input("Enter the name of the passenger: ")
    DestinationPlace=input("Enter the Destination Place: ")               
    ArrivalPlace=input("Enter the Arrival Place: ")                       
    TrainNumber=int(input("Enter the Train Number: "))
    print("VishakaExpress,BhuvaneswarExpress,ChennaiExpress,VenkatadriExpress,seshadriExpress")
    TrainName=input("Enter the Train Name: ")
    if TrainName == "VishakaExpress":
        cost = price1
        print(cost," Rs per ticket")
    elif TrainName == "BhuvaneswarExpress":
        cost = price2
        print(cost," Rs per ticket")
        
    elif TrainName == "ChennaiExpress":
        cost = price3
        print(cost," Rs per ticket")
        
    elif TrainName == "VenkatadriExpress":
        cost = price4
        print(cost," Rs per ticket")
        
    elif TrainName == "seshadriExpress":
        cost = price5
        print(cost," Rs per ticket")
        
    else:
        print("please select the train in given list.")
    Timings=str(input("Enter the Train Timings: "))                    
    seats=int(input("Enter the no.of seats: "))
    cmd3 = "insert into Traintb values ('"+str(sno)+"','"+name+"','"+DestinationPlace+"','"+ArrivalPlace+"','"+str(TrainNumber)+"','"+TrainName+"','"+str(Timings)+"','"+str(seats)+"','"+str(cost)+"')"
    mycursor.execute(cmd3)
    print("Record has been added successfully")

def AC_Bill():
  cmd4 = "select * from Traintb"
  mycursor.execute(cmd4)
  r3 = mycursor.fetchall() 
  print("Your bill")
  name_1 = input("Enter the name of the passenger: ") 
  for i in range(len(r3)): 
      a = r3[i][1] 
      if name_1 == a: 
          seat = int(r3[i][7])
          price = int(r3[i][8]) 
          print("Total number of seats you booked: ",r3[i][7])
          print("your seat numbers are: ")
          
          for i in range(seat):  
              print(random.randrange(1,500),end = ",")
          print(" ")
          total_amount = cost * seat
          print("Total Amount = ",total_amount)

def display_GeneralSeats():
    
    print("====================================================================================================================")
    print("| DESTINATION PLACE  ARRIVAL PLACE  TRAIN NO   TRAIN NAME           TRAIN TIMINGS       TICKET PRICE  SEATS AVALIABLE|")
    print("====================================================================================================================")

    print("     VISHAKAPATNAM    NELLORE        12347    VishakaExpress         10:55am-3:15am          150rs           400       ")
    print("     ANANTAPUR        HYDERABAD      34567   BhuvaneswarExpress      3:15am-7:30pm           245rs           300       ")
    print("      TIRUPATI       CHENNAI         16054    ChennaiExpress         4:10am-5:40pm           250rs           200       ")
    print("      BANGLORE       CHENNAICENTRAL  45678   VenkatadriExpress       6:20am-8:54pm           195rs           250       ")
    print("     KURNOOL         KAVALI          20895    seshadriExpress        9:40pm-12:55am          225rs           350       ")
    print("     PUNE            AGRA            52422    MysoreExpress          12:40am-1:55pm          650rs           400       ")
    print("     MUMBAI          ONGOLE          51750   KasiExpress             1:40am-12:55pm          250rs           357       ")
    print("=======================================================================================================================")

def General_passengers():
    
    cmd2 = "select * from Traintb"
    mycursor.execute(cmd2)
    r2 = mycursor.fetchall()
    
    print("===================================================================================================================================")
    print("|SNO     NAME     DESTINATION PLACE  ARRIVAL PLACE      TRAIN NO       TRAIN NAME   TRAIN TIMINGS   SEATS    COST|")
    print("===================================================================================================================================")

    for i in range(len(r2)): 
        print("| ",end="")
        print(str(r2[i][0]).ljust(6," "),end=" ") 
        print(r2[i][1].ljust(12," "),end=" ") 
        print(r2[i][2].ljust(15," "),end=" ")                  
        print(r2[i][3].ljust(15," "),end=" ")               
        print(str(r2[i][4]).ljust(15," "),end=" ")
        print(r2[i][5].ljust(12," "),end=" ")
        print(r2[i][6].ljust(11," "),end=" ")
        print(str(r2[i][7]).ljust(10," "),end="|")
        print(str(r2[i][8]).ljust(10," "),end="|") 
        print()

    print("=============================================================================================================================")

pric1,pric2,pric3,pric4,pric5,pric6,pric7 = 150,245,250,195,225,650,250

def Booking_GeneralSeats():
    global seats
    global cost
    global name
    sno = int(input("Enter the sno: "))
    name = input("Enter the name of the passenger: ")
    DestinationPlace=input("Enter the Destination Place: ")               
    ArrivalPlace=input("Enter the Arrival Place: ")                       
    TrainNumber=int(input("Enter the Train Number: "))
    print("VishakaExpress,BhuvaneswarExpress,ChennaiExpress,VenkatadriExpress,seshadriExpress,MysoreExpress,KasiExpress")
    TrainName=input("Enter the Train Name: ")
    if TrainName == "VishakaExpress":
        cost = pric1
        print(cost," Rs per ticket")
    elif TrainName == "BhuvaneswarExpress":
        cost = pric2
        print(cost," Rs per ticket")
        
    elif TrainName == "ChennaiExpress":
        cost = pric3
        print(cost," Rs per ticket")
        
    elif TrainName == "VenkatadriExpress":
        cost = pric4
        print(cost," Rs per ticket")
        
    elif TrainName == "seshadriExpress":
        cost = pric5
        print(cost," Rs per ticket")
    elif TrainName == "MysoreExpress":
        cost = pric6
        print(cost," Rs per ticket")
    elif TrainName == "KasiExpress":
        cost = pric7
        print(cost," Rs per ticket")
        
    else:
        print("please select the train in given list.")
    Timings=str(input("Enter the Train Timings: "))                    
    seats=int(input("Enter the no.of seats: "))
    cmd3 = "insert into Traintb values ('"+str(sno)+"','"+name+"','"+DestinationPlace+"','"+ArrivalPlace+"','"+str(TrainNumber)+"','"+TrainName+"','"+str(Timings)+"','"+str(seats)+"','"+str(cost)+"')"
    mycursor.execute(cmd3)
    print("Record has been added successfully")

def General_Bill():
  cmd4 = "select * from Traintb"
  mycursor.execute(cmd4)
  r3 = mycursor.fetchall() 
  print("Your bill")
  name_1 = input("Enter the name of the passenger: ") 
  for i in range(len(r3)): 
      a = r3[i][1] 
      if name_1 == a: 
          seat = int(r3[i][7])
          price = int(r3[i][8]) 
          print("Total number of seats you booked: ",r3[i][7])
          print("your seat numbers are: ")
          
          for i in range(seat):  
              print(random.randrange(1,500),end = ",")
          print(" ")
          total_amount = cost * seat
          print("Total Amount = ",total_amount)

while True:
    print("\n\n-------------DETAILS--------------------")
    print("(1)ACSeats (2)GENERALSeats  (3)Exit")
    choice=int(input("Please enter your choice:")) 
    if(choice==1):
        while True:
            print("(1)display_ACSeats (2)Booking_ACSeats (3)AC_passengers (4)AC_Bill  (5)Exit")
            choice1=int(input("Please enter your choice:")) 
            if(choice1==1):
                display_ACSeats()

            elif(choice1==2):
                Booking_ACSeats()
            elif(choice1==4):
                AC_Bill()
            elif(choice1==3):
                AC_passengers()
            elif(choice1==5):
                break
    if(choice==2):
        while True:
            print("(1)display_GeneralSeats (2)Booking_GeneralSeats (3)General_passengers (4)General_Bill  (5)Exit")
            choice2=int(input("Please enter your choice:")) 
            if(choice2==1):
                display_GeneralSeats()

            elif(choice2==2):
                Booking_GeneralSeats()
            elif(choice2==4):
                General_Bill()
            elif(choice2==3):
               General_passengers()
            elif(choice2==5):
                break
    if(choice==3):
        break
