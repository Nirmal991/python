def date():
    s_input = input("Enter the date in DD/MM/YYYY format: ")

    split_input = s_input.split('/')

    if(len(split_input) != 3 ):
        print(f"Invalid input try in given format")
        return

    day = int(split_input[0])
    month = int(split_input[1])
    year = int(split_input[2])  

    months = ("January", "feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

    if month < 1 or month > 12:
        print("Invalid month")
        return
    
    leap_year = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

    if month == 2:
        if leap_year:
            max_day = 29
        else: 
            max_day = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_day = 30
    else: 
        max_day = 31

    if day <= 0 or day > max_day:
        print("Invalid date")
        return

    print(f"{months[month - 1]} {day}, {year}")

def main():
    date()

main()
            
