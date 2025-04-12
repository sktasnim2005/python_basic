# Match-case statement (switch): An alternative to using many 'elif' statements
#                                                          Execute some code if a value matches a 'case'
#                                                          Benefits: cleaner and syntax is more readable

#Part  1
print("------------------------- PArt 1 General way ------------------------------------------")

def day_of_week(day):
    if day == 1:
        return "It's Saturday"
    elif day == 2:
        return "It's Sunday"
    elif day == 3:
        return "It's Monday"
    elif day == 4:
        return "It's Tuesday"
    elif day == 5:
        return "It's Wednesday"
    elif day == 6 :
        return "It's Thursday"
    elif day == 7:
        return "It's Friday"
    else :
        return "Not a vaid day!"
    
print(day_of_week(1))



#Part  2
print("\n------------------------- PArt 2 Match-Case  ------------------------------------------\n")

def num_of_week(days):
    match days:
        case 1:
            return "It's Saturday"
        case 2:
            return "It's Sunday"
        case 3:
            return "It's Monday"
        case 4:
            return "It's Tuesday"
        case 5:
            return "It's Wednesday"
        case 6 :
            return "It's Thursday"
        case 7:
            return "It's Friday"
        case _ :                     # insted of else here we used case uderscore _
            return "Not a vaid day!"

print(num_of_week(5))




#Part  3
print("\n------------------------- PArt 3 Match-Case  ------------------------------------------\n")

def is_weekend(day):
    match day:
        case "Friday":
            return True
        case "Saturday":
            return True
        case _ :                     
            return False

print(is_weekend("Sunday"))

#Part  4
print("\n------------------------- PArt 4  ------------------------------------------\n")

def is_weekend(day):
    match day:
        case "Friday" | "Saturday" :
            return True
        case _ :                     
            return False

print(is_weekend("Saturday"))