#libraries
import re

#main
def main():
    print("welcome to my modest system")
    print('\t 1-signup ')

    choice = int(input())

    if choice == 1:
        signup()

def signup():
    
    while(True):
        Email = input("Email address :  ")
        Password = input("password : ")
        if is_email_valid(Email):
            break
        else:
            print("email not valid")
            

    print(is_password_strong(Password))

    


    

#email validator 
def is_email_valid(Email):
    
    pattern = re.compile(r"[a-zA-Z0-9.-_]+@[a-zA-Z0-9]+\.com")


    if pattern.search(Email):
        if pattern.search(Email).group(0) == Email:
            return True
        else:
            return False


#password validator
def is_password_strong(password):
    
    points = 0

    patterns = [r"[A-Z]",r"[a-z]",r"[0-9]"]
    
    patterns = list(map(re.compile , patterns))

    for pattern in patterns:
        
        if pattern.search(password):
            points += 1

    if points == 0:
        return "input a valid password please"
    elif points == 1:
        return "weak password"
    elif points == 2:
        return "medium password"
    else:
        return "strong password"

    
main()
            
