# Brandon Escamilla PSID: 1823960
month = int(input("Please enter the current month:\n"))
day = int(input("Please enter the current date:\n"))
year = int(input("Please enter the current year:\n"))

bmonth = int(input("Please enter your birth month:\n"))
bday = int(input("Please enter your birth date:\n"))
byear = int(input("Please enter your birth year:\n"))

if month < bmonth:
    if day < bday:
        age = year - byear
        age -= 1
        print("Birthday Calculator\n")
        print("Current Day")
        print("Month:", month)
        print("Day:", day)
        print("Year:", year)
        print()
        print("Birthday")
        print("Current Day")
        print("Month:", bmonth)
        print("Day:", bday)
        print("Year:", byear)
        print()
        print("You are", age, "year(s) old.")
    if day > bday:
        age = year - byear
        age -= 1
        print("Birthday Calculator\n")
        print("Current Day")
        print("Month:", month)
        print("Day:", day)
        print("Year:", year)
        print()
        print("Birthday")
        print("Current Day")
        print("Month:", bmonth)
        print("Day:", bday)
        print("Year:", byear)
        print()
        print("You are", age, "year(s) old.")
if month > bmonth:
    if day < bday:
        age = year - byear
        print("Birthday Calculator\n")
        print("Current Day")
        print("Month:", month)
        print("Day:", day)
        print("Year:", year)
        print()
        print("Birthday")
        print("Current Day")
        print("Month:", bmonth)
        print("Day:", bday)
        print("Year:", byear)
        print()
        print("You are", age, "year(s) old.")
    if day > bday:
        age = year - byear
        print("Birthday Calculator\n")
        print("Current Day")
        print("Month:", month)
        print("Day:", day)
        print("Year:", year)
        print()
        print("Birthday")
        print("Current Day")
        print("Month:", bmonth)
        print("Day:", bday)
        print("Year:", byear)
        print()
        print("You are", age, "year(s) old.")
if month == bmonth:
    if day < bday:
        age = year - byear
        age -= 1
        print("Birthday Calculator\n")
        print("Current Day")
        print("Month:", month)
        print("Day:", day)
        print("Year:", year)
        print()
        print("Birthday")
        print("Current Day")
        print("Month:", bmonth)
        print("Day:", bday)
        print("Year:", byear)
        print()
        print("You are", age, "year(s) old.")
    if day > bday:
        age = year - byear
        print("Birthday Calculator\n")
        print("Current Day")
        print("Month:", month)
        print("Day:", day)
        print("Year:", year)
        print()
        print("Birthday")
        print("Current Day")
        print("Month:", bmonth)
        print("Day:", bday)
        print("Year:", byear)
        print()
        print("You are", age, "year(s) old.")
    if day == bday:
        age = year - byear
        print("Birthday Calculator\n")
        print("Current Day")
        print("Month:", month)
        print("Day:", day)
        print("Year:", year)
        print()
        print("Birthday")
        print("Current Day")
        print("Month:", bmonth)
        print("Day:", bday)
        print("Year:", byear)
        print()
        print("Happy Birthday!")
        print("You are", age, "year(s) old.\n")