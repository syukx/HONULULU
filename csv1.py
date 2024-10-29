import pyttsx3
from PIL import Image
import pickle
import random
import mysql.connector as mc
from prettytable import PrettyTable
from mysql.connector import Error
from datetime import date, datetime
import datetime
import time
import matplotlib.pyplot as plt
import csv

cs = 0
h1 = 0
j = 0
h = 0
hh = 0
l78 = 0
c178 = 0
k99 = []
k8 = []
t78 = 0
fgh = 0
nm = ""
ba = ""
re = ""


def meals():
    global t78
    b1 = "y"
    ts = pyttsx3.init()
    i = Image.open("./relish.jpg")
    plt.imshow(i)
    plt.ion()
    plt.show()
    plt.pause(3)
    ts.say("Relish Gourmet experience in flight")
    ts.runAndWait()
    plt.close()
    i = Image.open("./prebook_meals.jpg")
    plt.imshow(i)
    plt.ion()
    plt.show()
    plt.pause(3)
    ts.say("Prebook these meals for your next flight")
    ts.runAndWait()
    plt.close()
    i = Image.open("./sandwiches.jpg")
    plt.imshow(i)
    plt.ion()
    plt.show()
    plt.pause(4)
    ts.say("Sandwiches")
    ts.runAndWait()
    plt.close()
    i = Image.open("./hot_meals.jpg")
    plt.imshow(i)
    plt.ion()
    plt.show()
    plt.pause(4)
    ts.say("hot meals")
    ts.runAndWait()
    plt.close()
    i = Image.open("./beverages.jpg")
    plt.imshow(i)
    plt.ion()
    plt.show()
    plt.pause(4)
    ts.say("beverages")
    ts.runAndWait()
    plt.close()
    a = []
    t78 = 0
    a2 = []
    print("\U0001F371" * 2, "FOOD & BEVERAGES", "\U0001F371" * 2)
    while b1 == "y" or b1 == "Y":
        ts.say("enter the food item number")
        ts.runAndWait()
        b = int(input("ENTER FOOD ITEM NO.:"))
        a.append(b)
        b1 = input("do you want to add more items?(y/n):".upper())
    a.sort()
    f = open(
        "C:\\Users\\ansel\\PycharmProjects\\pythonProject\\comp_proj_XII_2023\\MEALS.csv",
        "r",
    )
    a1 = list(csv.reader(f))
    i1 = []
    for i in range(1, 28):
        i1.append(i)
    for j in a:
        f1 = 0
        if j in i1:
            f1 = 1
            t78 += int(a1[j - 1][2])
            a2.append(a1[j - 1][1])
        else:
            ts.say("please enter valid food number")
            ts.runAndWait()
            print("please enter valid food number".upper())
            meals()
            break
    if f1 == 1:
        print("IN STOCKS")
        time.sleep(2)
        print("PROCESSING....")
    return ["FOOD ITEMS:", a2, "TOTAL COST:", t78]


def captcha():
    ts = pyttsx3.init()
    i = Image.open("./captcha.jpg")
    plt.imshow(i)
    plt.ion()
    plt.show()
    plt.pause(2)
    plt.close()
    ts.say("PLEASE VERIFY THAT YOU ARE NOT A ROBOT!")
    ts.runAndWait()
    print("\U0001F916" * 2, "PLEASE VERIFY THAT YOU ARE NOT A ROBOT!", "\U0001F916" * 2)
    d = random.randint(0, 1)
    if d == 1:
        f = Image.open("./captcha2.png")
        plt.imshow(f)
        plt.ion()
        plt.show()
        plt.pause(5)
        plt.close()
        c = input("ENTER THE CODE IN THE IMAGE:")
        if c == "qGphJD":
            ts.say("VERIFIED!!!")
            ts.runAndWait()
            print("VERIFIED!!!", "\U00002714" * 3)
            return True
        else:
            ts.say("OOPS! ROBOT DETECTION FAILED")
            ts.runAndWait()
            print("\U0000274C" * 2, "OOPS! ROBOT DETECTION FAILED", "\U0000274C" * 2)
            return False
    else:
        f = Image.open("./captcha1.png")
        plt.imshow(f)
        plt.ion()
        plt.show()
        plt.pause(5)
        plt.close()
        ts.say("ENTER THE CODE IN THE IMAGE:")
        ts.runAndWait()
        c = input("ENTER THE CODE IN THE IMAGE:")
        if c == "smwm":
            ts.say("VERIFIED!!!")
            ts.runAndWait()
            print("VERIFIED!!!", "\U00002714" * 2)
            return True
        else:
            ts.say("OOPS! ROBOT DETECTION FAILED")
            ts.runAndWait()
            print("\U0000274C" * 2, "OOPS! ROBOT DETECTION FAILED", "\U0000274C" * 2)
            return False


def luggage(a, c, i, cls):  # argument for ADULT,CHILD,INFANT and class
    ts = pyttsx3.init()
    f = Image.open("./wp")
    plt.imshow(f)
    plt.ion()
    plt.show()
    ts.say("luggage")
    ts.runAndWait()
    plt.pause(5)
    plt.close()
    print("\U0001F9F3" * 2, "LUGGAGE", "\U0001F9F3" * 2)
    t = a + c
    if cls == 1:
        t1 = (t * 25) + (i * 10)
        print("CLASS: ECONOMY")
        print("MAXIMUM WEIGHT PASSENGERS CAN CARRY:", t1)
        return t1
    elif cls == 2:
        t1 = (t * 35) + (i * 10)
        print("CLASS:BUSINESS")
        print("MAXIMUM WEIGHT PASSENGERS CAN CARRY:", t1)
        return t1
    elif cls == 3:
        t1 = (t * 40) + (i * 10)
        print("CLASS:FIRST CLASS")
        print("MAXIMUM WEIGHT PASSENGERS CAN CARRY :", t1)
        return t1


def coupon(p):  # price argument
    ts = pyttsx3.init()
    i = 0
    p1 = str(p)
    new_text = ""
    while i < len(p1):
        new_text += p1[i] + "\u0336"
        i = i + 1
    f = Image.open("./wp")
    plt.imshow(f)
    plt.ion()
    plt.show()
    plt.pause(2)
    ts.say("exclusive deals for you, more discount for your flight")
    ts.runAndWait()
    plt.pause(3)
    plt.close()
    print(
        "\U0001F3F7" * 2,
        "exclusive deals for you! more discount for your flight".upper(),
        "\U0001F3F7" * 2,
    )
    c = input("IS THIS YOUR FIRST FLIGHT BOOKING ON HONULULU?(Y/N)").upper()
    if c == "Y":
        print("\U0001F389" * 2, "'WELCOME' COUPON APPLIED", "\U0001F389" * 2)
        p -= p * (12 / 100)
        print("ORIGINAL PRICE:", new_text)
        print("NEW PRICE AFTER 'WELCOME' COUPON APPLIED:", p)
        return p * (12 / 100)
    else:
        print("\U0001F389" * 2, "'SAVEMORE' COUPON APPLIED", "\U0001F389" * 2)
        p -= p * (10 / 100)
        print("ORIGINAL PRICE:", new_text)
        print("NEW PRICE AFTER 'SAVEMORE' COUPON APPLIED:", p)
        return p * (10 / 100)


def bc():
    if h1 > cs and fgh == 1:
        print("\t" * 7, "FARE SUMMARY")
        print("\tBASE FAIR:", "\u0336" + "\u0336".join(str(h1 * j)))
        print("\tTAXES $ FEES:", (18 / 100) * (h1 * j))
        print("\tLUGGAGE FEE:", l78)
        print("\tCOUPON APPLIED:", c178)
        print("\tMEALS FEE:", 399)
        print("\tGRAND TOTAL:", (18 / 100) * (h1 * j) + (h1 * j) + l78 - c178 + t78)
    elif h1 > cs and fgh == 0:
        print("\t" * 7, "FARE SUMMARY")
        print("\tBASE FAIR:", "\u0336" + "\u0336".join(str(h1 * j)))
        print("\tTAXES $ FEES:", (18 / 100) * (h1 * j))
        print("\tLUGGAGE FEE:", l78)
        print("\tCOUPON APPLIED:", c178)
        print("\tMEALS FEE:", 399)
        print("\tGRAND TOTAL:", (18 / 100) * (h1 * j) + (h1 * j) + l78 - c178 + t78)
    elif cs < h1 and fgh == 1:
        print("\t" * 7, "FARE SUMMARY")
        print("\tBASE FAIR:", "\u0336" + "\u0336".join(str(cs * j)))
        print("\tTAXES $ FEES:", (18 / 100) * (cs * j))
        print("\tLUGGAGE FEE:", l78)
        print("\tCOUPON APPLIED:", c178)
        print("\tMEALS FEE:", 399)
        print("\tGRAND TOTAL:", (18 / 100) * (cs * j) + (cs * j) + l78 - c178 + t78)
    else:
        print("\t" * 7, "FARE SUMMARY")
        print("\tBASE FAIR:", "\u0336" + "\u0336".join(str(cs * j)))
        print("\tTAXES $ FEES:", (18 / 100) * (cs * j))
        print("\tLUGGAGE FEE:", l78)
        print("\tCOUPON APPLIED:", c178)
        print("\tMEALS FEE:", 399)
        print("\tGRAND TOTAL:", (18 / 100) * (cs * j) + (cs * j) + l78 - c178 + t78)


def transaction():
    global l78, c178
    print("PRESS 1 TO ADD MEALS'\n'PRESS 2 TO SKIP")
    jj = int(input("Enter choice:".upper()))
    if jj == 1:
        w = meals()
        print(w)
    elif jj == 2:
        fgh = 1
        pass
    l78 = luggage(a78, c78, i78, cg)
    if ba == "DXB" or ba == "SYD" or ba == "LON" or ba == "MEL" or ba == "MOW":
        c178 = coupon(h1 * j)
    else:
        c178 = coupon(cs * j)
    print("PRESS 1 FOR NET BANKING'\n'PRESS 2 FOR DEBIT/CREDIT CARD")
    cc = int(input("ENTER MODE OF TRANSACTION:"))
    print("Processing transaction...".upper())
    tts("Processing transaction...".upper())
    transid = random.randint(100000000, 900000000)  # transaction ID = transid
    print(" ")
    if cc == 1:
        print(
            "PRESS 1 FOR SBI'\n'PRESS 2 FOR BOI'\n'PRESS 3 FOR PNB'\n'PRESS 4 FOR ICICI BANK'\n'PRESS 5 FOR AXIS BANK'\n'PRESS 6 FOR BANDHAN BANK"
        )
        fg = int(input("SELECT BANK FOR NET BANKING:"))
        if fg == 1 or fg == 2 or fg == 3 or fg == 4 or fg == 5 or fg == 6:
            fk = int(input("ACCOUNT NO:"))
            gk = int(input("RE-ENTER ACCOUNT NO:"))
            if captcha():
                if fk == gk:
                    kk = input(("ENTER IFC CODE:"))
                    while True:
                        time.sleep(3)
                        trans = random.randint(
                            3, 10
                        )  # generate random number for transaction success verification
                        if (
                            trans > 3.5
                        ):  # check random number for transaction success verification
                            print("Transaction successful".upper())
                            tts("Transaction successful")
                            bc()
                            print(" ")

                            break
                        else:
                            print("Transaction not successful.".upper())
                            tts("Transaction not successful.")
                            transaction()
                            break
                else:
                    print("INPUTS DIDN'T MATCHED. TRY AGAIN LATER!!!")
                    wlc()
            else:
                transaction()
    elif cc == 2:
        fk = int(input("CARD NO:"))
        gk = int(input("CVV NUMBER:"))
        print("ENTER DATE OF EXPIRY:-")
        year = int(input("ENTER YEAR OF EXPIRY:"))
        month = int(input("ENTER MONTH OF EXPIRY:"))
        day = int(input("ENTER DAY OF EXPIRY:"))
        d = date(year, month, day)
        if captcha():
            while True:
                time.sleep(3)
                trans = random.randint(
                    3, 10
                )  # generate random number for transaction success verification
                if (
                    trans > 3.5
                ):  # check random number for transaction success verification
                    print("Transaction successful".upper())
                    tts("Transaction successful")
                    bc()
                    print(" ")
                    break
                else:
                    print("Transaction not successful".upper())
                    tts("Transaction not successful")
                    transaction()
        else:
            transaction()
    return transid


def tts(text):
    engine = pyttsx3.init()
    say_var = text
    engine.say(say_var)
    engine.runAndWait()


print("\U00002708" * 2, "WELCOME TO HONULULU.COM", "\U00002708" * 2)
f = Image.open("./bhrfbhr.png")
plt.imshow(f)
plt.ion()
plt.show()
t = pyttsx3.init()
t.say("welcome to HONULULU dot com")
t.runAndWait()
plt.pause(3)
plt.close()
f.close()
try:
    con = mc.connect(
        host="localhost", user="root", password="1234", database="airlines_goibibo"
    )
    if con.is_connected():
        print("CONNECTION SUCCESSFUL....")
    else:
        print("ISSUE IN CONNECTION!!!")
except Error as e:
    pass
l = []


def add_p():
    global k99
    global k8
    c = con.cursor()
    l2 = []
    nm = input("ENTER NAME OF THE REGISTRANT:")
    while True:
        mo = input("ENTER MOBILE NUMBER:+91 ")
        if len(mo) == 10:
            break
        else:
            print("ENTER VALID MOBILE NUMBER!!!")
    print("RESERVATION DATE:", d23)
    l2.extend([nm, mo])
    print(l2)
    # s="insert into passenger values(%s,%s)"
    # c.execute(s,(l2))
    # con.commit()
    global a78, c78, i78
    print("----TRAVELLERS----")
    a78 = int(input("ADULTS (12+ YRS):"))
    c78 = int(input("CHILD (2-12 YRS):"))
    i78 = int(input("INFANTS (BELOW 2 YRS):"))
    global t
    t = a78 + c78 + i78
    for i in range(a78):
        print("PLEASE CHOOSE YOUR TITLE:-")
        print("PRESS 1 FOR MR.")
        print("PRESS 2 FOR MRS.")
        print("PRESS 3 FOR MS.")
        ch = int(input("enter choice:".upper()))
        nm1 = input("ENTER FIRST & MIDDLE NAME:")
        nm2 = input("ENTER LAST NAME:")
        if ch == 1:
            nm1 = "MR. " + nm1
            n = nm1 + " " + nm2
            k99.append(n)
        elif ch == 2:
            nm1 = "MRS. " + nm1
            n = nm1 + " " + nm2
            k99.append(n)
        elif ch == 3:
            nm1 = "MS. " + nm1
            n = nm1 + " " + nm2
            k99.append(n)
        else:
            print("PLEASE ENTER VALID ID!")
            a78 += 1
        print(
            "FOR ID VERIFICATION:-'\n'PRESS 1 FOR AADHAR CARD'\n'PRESS 2 FOR VOTER ID CARD'\n'PRESS 3 FOR DRIVING LICENSE'\n'PRESS 4 FOR PAN CARD"
        )
        ch1 = int(input("ENTER YOUR CHOICE:"))
        if ch1 == 1:
            k = int(input("ENTER AADHAR CARD NO.:"))
        elif ch1 == 2:
            k = int(input("ENTER VOTER ID CARD CARD NO.:"))
        elif ch1 == 3:
            k = int(input("ENTER DRIVING LICENSE NO.:"))
        elif ch1 == 4:
            k = int(input("ENTER PAN CARD NO.:"))
        else:
            print("WRONG CHOICE!!!")
            add_p()
    for j in range(c78):
        print("PLEASE CHOOSE YOUR CHILD'S TITLE:-")
        print("PRESS 1 FOR MS.")
        print("PRESS 2 FOR MASTER")
        ch = int(input("enter choice:".upper()))
        nm3 = input("ENTER FIRST & MIDDLE NAME:")
        nm4 = input("ENTER LAST NAME:")
        if ch == 1:
            nm3 = "MS. " + nm3
            n = nm1 + " " + nm2
            k8.append(n)
        elif ch == 2:
            nm3 = "MASTER " + nm3
            n = nm1 + " " + nm2
            k8.append(n)
        else:
            print("PLEASE ENTER VALID ID!")
            a78 += 1
    f1 = open(
        "C:\\Users\\ansel\\PycharmProjects\\pythonProject\\comp_proj_XII_2023\\tc.txt",
        "r",
    )
    st = f1.read()
    print("\t\t\t\t\t\t\t\tTERMS $ CONDITIONS")
    print(st)
    f1.close()
    return t


def log(a):
    f = open("C:\\Users\\ansel\\PycharmProjects\\pythonProject1\\login.dat", "wb+")
    pickle.dump(a, f)
    f.close()


def chk(l):
    f = open("C:\\Users\\ansel\\PycharmProjects\\pythonProject1\\login.dat", "rb+")
    while True:
        try:
            a = pickle.load(f)
            if l[0] == a[0]:
                if l[1] == a[1]:
                    return True
                else:
                    for i in range(3, 0, -1):
                        b = input(f"Re-enter password(attempts left:{i})):".upper())
                        if b == a[1]:
                            f.close()
                            return True
                        else:
                            pass
                    else:
                        f1 = Image.open("./wp")
                        plt.imshow(f1)
                        plt.ion()
                        plt.show()
                        plt.pause(3)
                        plt.close()
                        f.close()
                        wlc()
                        return False
        except EOFError:
            break
    f.close()


def wlc():
    print("PRESS 1:- SIGN IN")
    print("PRESS 2:- SIGN UP")
    a = input("ENTER CHOICE:")
    if a == "1":
        em = input("ENTER EMAIL ADDRESS:")
        pw = input("ENTER PASSWORD:")
        l = [em, pw]
        a1 = chk(l)
        if a1:
            print("WELCOME TO AIRLINES RESERVATION!!!")
        else:
            f = Image.open("./wp")
            plt.imshow(f)
            plt.ion()
            plt.show()
            plt.pause(3)
            plt.close()
            wlc()
    elif a == "2":
        em = input("ENTER EMAIL ADDRESS:")
        pw = input("ENTER PASSWORD:")
        l = [em, pw]
        log(l)
        wlc()
    else:
        print("WRONG CHOICE!!!")
        t.say("wrong choice")
        t.runAndWait()
        wlc()


wlc()


def baa():
    h = random.randint(4500, 9000)
    print("COST:", h, "/SEAT")
    # return h


def v(nm, ba):
    x1 = []
    global cs
    global j
    global h
    global hh
    h = random.randint(2, 4)
    hh = random.randint(0, 60)
    cr = con.cursor()
    cr.execute(
        "select flights.fcode,flights.flights from flights,routes where routes.fcode=flights.fcode and routes.depart_airport=%s and routes.arrive_airport=%s",
        (nm, ba),
    )
    x = cr.fetchall()
    if len(x) != 0:
        print(x)
        m = PrettyTable(["FCODE", "Name_of_flights"])
        for i in x:
            if i not in x1:
                x1.append(i)
        for u in x1:
            m.add_row([u[0], u[1]])
        print(m)
        y = int(input("Enter FCODE to select the choice of Flight:".upper()))
        for u in x:
            if u[0] == y:
                print(u[0])
                print("Selected airline is:".upper(), u[1])
                break

        cs = random.randint(4500, 9000)
        print("COST:", cs, "/SEAT")
        tr = random.randint(0, 120)
        print("Seats available:".upper(), tr)
        if tr == 0:
            v(nm, ba)
        j = add_p()
        if tr >= j:
            print()
            print()
            print("DURATION OF JOURNEY:--", h, "HOURS", hh, "MINUTES.")
        else:
            print(
                "total no of passengers not matching with total infants+children+adults"
            )
            v(nm, ba)
        return cs

    else:
        print(
            "No airlines are assigned for the given route. Sorry for the inconvenience caused.".upper()
        )
        fl()

    con.commit()


def ind(nm, ba):
    global h1
    global j
    global h
    global hh
    h = random.randint(12, 16)
    hh = random.randint(0, 60)
    cr = con.cursor()
    cr.execute(
        "select flights.fcode,flights.flights from flights,routes where routes.fcode=flights.fcode and routes.depart_airport=%s and routes.arrive_airport=%s",
        (nm, ba),
    )
    x = cr.fetchall()
    if len(x) != 0:
        print(x)
        m = PrettyTable(["FCODE", "Name_of_flights"])
        for u in x:
            m.add_row([u[0], u[1]])
        print(m)
        y = int(input("Enter FCODE to select the choice of Flight:".upper()))
        for u in x:
            if u[0] == y:
                print(u[0])
                print("Selected airline is:".upper(), u[1])
                break

        h1 = random.randint(250000, 350000)
        print("COST:", h1, "/SEAT")
        tr = random.randint(0, 120)
        if tr > 0:
            print("Seats available:".upper(), tr)
        if tr == 0:
            v(nm, ba)
        j = add_p()
        if tr >= j:

            print("DURATION OF JOURNEY:--", h, "HOURS", hh, "MINUTES.")
        else:
            print(
                "total no of passengers not matching with total infants+children+adults"
            )
            v(nm, ba)
        return h1
    else:
        print(
            "No airlines are assigned for the gven route. Sorry for the inconvenience caused.".upper()
        )
        fl()

    con.commit()


def gh():
    global cg
    cg = int(
        input(
            "PRESS 1 for economy'\n'press 2 for business'\n'press 3 for first class".upper()
        )
    )
    if cg == 1:
        print("SELECTED CLASS: ECONOMY")
    elif cg == 2:
        print("SELECTED CLASS: BUSINESS")
    elif cg == 3:
        print("SELECTED CLASS: FIRST CLASS")
    else:
        print("WRONG CHOICE!!!")
    return cg


def fl():
    global cg, ba, nm
    pr = int(input("Press 1 for one way and 2 for round trip:".upper()))
    if pr == 1:
        bom = "BOMBAY"
        pnq = "PUNE"
        maa = "CHENNAI"
        amd = "AHMEDABAD"
        raj = "RAJKOT"
        ccu = "KOLKATA"
        ixz = "ANDAMAN $ NICOBAR ISLANDS"
        cok = "KOCHI"
        Del = "DELHI"
        mt = PrettyTable(["Departing airport", "IATA"])
        mt.add_row([bom, "BOM"])
        mt.add_row([pnq, "PNQ"])
        mt.add_row([maa, "MAA"])
        mt.add_row([amd, "AMD"])
        mt.add_row([raj, "RAJ"])
        mt.add_row([ccu, "CCU"])
        mt.add_row([ixz, "IXZ"])
        mt.add_row([cok, "COK"])
        mt.add_row([Del, "DEL"])
        print(mt)
        nm = input("Enter departing IATA from the list of above airports:".upper())
        b = "BOMBAY"
        p = "PUNE"
        m = "CHENNAI"
        a = "AHMEDABAD"
        r = "RAJKOT"
        c1 = "KOLKATA"
        i = "ANDAMAN $ NICOBAR ISLANDS"
        c = "KOCHI"
        d = "DELHI"
        dx = "DUBAI"
        st = "SYDNEY"
        lnm = "LONDON"
        ml = "MELBORNE"
        mn = "MOSCOW"
        mt = PrettyTable(["Arrival airport", "IATA"])
        mt.add_row([b, "BOM"])
        mt.add_row([p, "PNQ"])
        mt.add_row([m, "MAA"])
        mt.add_row([a, "AMD"])
        mt.add_row([r, "RAJ"])
        mt.add_row([c1, "CCU"])
        mt.add_row([i, "IXZ"])
        mt.add_row([c, "COK"])
        mt.add_row([d, "DEL"])
        mt.add_row([dx, "DXB"])
        mt.add_row([st, "SYD"])
        mt.add_row([lnm, "LON"])
        mt.add_row([ml, "MEL"])
        mt.add_row([mn, "MOW"])
        # some left to add
        print(mt)
        ba = input("Enter arrival IATA from the list of above airports:".upper())
        if ba == "DXB" or ba == "SYD" or ba == "LON" or ba == "MEL" or ba == "MOW":
            year = int(input("Enter a year:".upper()))
            month = int(input("Enter a month:".upper()))
            day = int(input("Enter a day:".upper()))
            global d23
            d23 = date(year, month, day)
            print(
                "PRESS 1 for economy'\n'press 2 for business'\n'press 3 for first class".upper()
            )
            cg = int(input("enter choice:".upper()))
            if cg == 1:
                print("SELECTED CLASS: ECONOMY")
            elif cg == 2:
                print("SELECTED CLASS: BUSINESS")
            else:
                print("SELECTED CLASS: FIRST CLASS")
            if year > 2023:
                print("Registration will open shortly".upper())
                fl()
            else:
                ind(nm, ba)
        else:

            year = int(input("Enter a year:".upper()))
            month = int(input("Enter a month:".upper()))
            day = int(input("Enter a day:".upper()))
            d23 = date(year, month, day)
            if month >= 11 and day >= 10:
                if year > 2023:
                    print("Registration will open shortly".upper())
                    fl()
                else:
                    print(
                        "PRESS 1 for economy'\n'press 2 for business'\n'press 3 for first class".upper()
                    )
                    cg = int(input("enter choice:".upper()))
                    if cg == 1:
                        print("SELECTED CLASS: ECONOMY")
                    if cg == 2:
                        print("SELECTED CLASS: BUSINESS")
                    else:
                        print("SELECTED CLASS: FIRST CLASS")
                    v(nm, ba)
            else:
                print("PLEASE ENTER VALID DATE!!!")
                fl()

    else:
        bom = "BOMBAY"
        pnq = "PUNE"
        maa = "CHENNAI"
        amd = "AHMEDABAD"
        raj = "RAJKOT"
        ccu = "KOLKATA"
        ixz = "ANDAMAN $ NICOBAR ISLANDS"
        cok = "KOCHI"
        Del = "DELHI"
        mt = PrettyTable(["Departing airport", "IATA"])
        mt.add_row([bom, "BOM"])
        mt.add_row([pnq, "PNQ"])
        mt.add_row([maa, "MAA"])
        mt.add_row([amd, "AMD"])
        mt.add_row([raj, "RAJ"])
        mt.add_row([ccu, "CCU"])
        mt.add_row([ixz, "IXZ"])
        mt.add_row([cok, "COK"])
        mt.add_row([Del, "DEL"])
        print(mt)
        nm = input("Enter departing IATA from the list of above airports:".upper())
        b = "BOMBAY"
        p = "PUNE"
        m = "CHENNAI"
        a = "AHMEDABAD"
        r = "RAJKOT"
        c1 = "KOLKATA"
        i = "ANDAMAN $ NICOBAR ISLANDS"
        c = "KOCHI"
        d = "DELHI"
        dx = "DUBAI"
        st = "SYDNEY"
        lnm = "LONDON"
        ml = "MELBORNE"
        mn = "MOSCOW"
        mt = PrettyTable(["Arrival airport", "IATA"])
        mt.add_row([b, "BOM"])
        mt.add_row([p, "PNQ"])
        mt.add_row([m, "MAA"])
        mt.add_row([a, "AMD"])
        mt.add_row([r, "RAJ"])
        mt.add_row([c1, "CCU"])
        mt.add_row([i, "IXZ"])
        mt.add_row([c, "COK"])
        mt.add_row([d, "DEL"])
        mt.add_row([dx, "DXB"])
        mt.add_row([st, "SYD"])
        mt.add_row([lnm, "LON"])
        mt.add_row([ml, "MEL"])
        mt.add_row([mn, "MOW"])
        # some left to add
        print(mt)
        ba = input("Enter arrival IATA from the list of above airports:".upper())
        year1 = int(input("Enter a year:".upper()))
        month1 = int(input("Enter a month:".upper()))
        day1 = int(input("Enter a day:".upper()))
        d23 = date(year1, month1, day1)
        if year1 > 2023:
            print("Registration will open shortly".upper())
            fl()
        elif year1 <= 2023:
            year = int(input("Enter year of return:".upper()))
            month = int(input("Enter month:".upper()))
            day = int(input("Enter a day:".upper()))
            d23 = date(year, month, day)
            if year > 2023:
                print("Registration will open shortly".upper())
                fl()
            elif year < year1:
                print("Enter valid year".upper())
                fl()
            elif year == year1:
                if month < month1:
                    print("Enter valid month".upper())
                    fl()
                elif month == month1:
                    if day < day1:
                        print("enter valid day".upper())
                    else:
                        gh()
                        z = baa()
                        v(nm, ba)
                else:
                    gh()
                    z = baa()
                    v(nm, ba)

            else:
                gh()
                z = baa()
                v(nm, ba)

        else:
            gh()
            z = baa()
            v(nm, ba)


fl()
transaction()


def hr():
    global bbx
    global hhj
    global re
    bbx = 30 + hh
    if bbx >= 60:
        hhj = 8 + h + 1
        bbx = bbx - 60
        if bbx < 10:
            re = "0" + str(bbx)
        else:
            re = str(bbx)
    else:
        re = str(bbx)
        hhj = 8 + h


hr()
c = 12
tnoo = random.randint(10000000, 99999999)
x = datetime.datetime.now()
print(x.strftime("%c"))
print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)
print(
    nm.upper(),
    " -TO- ",
    ba.upper(),
    "\t\t\t",
    x.strftime("%c"),
    "\t\t\t\tTRIP ID:",
    random.randint(10000000000, 99999999999),
)
print(
    "------------------------------------------------------------------------------------------------------------------------------------------"
)
print("HONULULU.IN\t\t       ", nm.upper(), "\t\t\t  -TO-  \t\t\t", ba.upper())
print(
    str(h) + "hrs", str(hh) + "mins", "\t\t\t8:30 \t\t\t\t\t\t\t", str(hhj) + ":" + re
)
print("\t\t\t       ", d23, "   \t\t\t\t\t\t", d23)
print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)
print("PASSENGER DETAILS\t\tSEAT NO.\t\t\t\t\t\t\tTICKET NO.")
print(
    "-------------------------------------------------------------------------------------------------------------------------------------------"
)
if len(k99) != 0:
    for xxj in k99:
        c = c + 1
        print(xxj.upper(), "\t", "B" + str(c), "\t\t\t\t\t\t\t\t", tnoo)
if len(k8) != 0:
    for xxj in k8:
        c = c + 1
        print(xxj.upper(), "\t", "B" + str(c), "\t\t\t\t\t\t\t\t", tnoo)
print("FARE BREAK UP")
bc()
