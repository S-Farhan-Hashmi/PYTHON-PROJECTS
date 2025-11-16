import getpass
print("Hellow, welcome to password manager")
def addpassword():
    a=input("Enter website name : ").lower()
    b=input("Enter username : ").lower()
    c=input("Enter password :")
    with open("passwords.txt","a") as file:
        file.write(f"{a},{b},{c}\n")
    print("passwords saved successfully")
def viewpassword():
    try:
        with open ("passwords.txt","r") as file:
            e=file.readlines()
        if not e:
            print("No passwords saved yet ")
            return
        print("Your saved passwords are : ")
        for i in e:
            website,username,password=i.strip().split(",")
            print(f"website : {website}, username : {username} ,  password : {password}")
    except FileNotFoundError:
        print("No file found , please add passowrd to view")
def searchpassword():
    f=input("Enter website to search password : ").lower()
    try:
        with open("passwords.txt","r") as file:
            g=file.readlines()
        h=list(filter(lambda x: f in x.lower(),g))
        if h :
            print("Here is ur matching entries : ")
            for i in h:
                website,username,password=i.strip().split(",")
                print(f"website : {website}, username : {username} , password : {password} ")
        else:
            print("No matching results found")
    except FileNotFoundError:
        print("No passwords found , please add passwords to view")
def main():
    def x(y=1):
        if y>3:
            print("To many attempts pls try again later")
            return
        d=getpass.getpass("Enter master password : ")
        if d=="topper":
            print("Welcome back ")
            while True :
                print("How can we help u today")
                print("Enter 1 to add new password")
                print('Enter 2 to view passwords')
                print("Enter 3 to search existing passwords ")
                print("Enter 4 to exit ")
                l=int(input("Enter your desired choice : "))
                if l==1:
                    addpassword()
                elif l==2:
                    viewpassword()
                elif l==3:
                    searchpassword()
                elif l==4:
                    print("Thank you, please visit again")
                    break
                else:
                    print("Invalid input, please try again")
        else:
            print("Opps , wrong password ")
            x(y+1)
    x()
main()

    

    
    