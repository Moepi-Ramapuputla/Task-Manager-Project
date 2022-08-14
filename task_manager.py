#Program which keep track of users and restricts access using passwords

from datetime import date
today = date.today()


input_name = input("Enter name here : ")
input_password = input("Enter password here :")


contents = ""
with open('user.txt', 'r+') as f:
        for line in f:
            contents += line



#adding username and password to file
    

current_users = contents
current_string = str(contents)
    


    #check string to check if name entered is part of database name
x = current_string.find( input_name )
    #print(x) #just test

if x >= 0 :

    print("Name is Correct :")

else:
    print("Name is Incorrect :")

    #check string 2nd time to check the full string so if both name and password are present # so checks if ["admin", "adm1n"] matches exactly. # this way only works if both password and name match

y = current_string.find(f"['{input_name}', '{input_password}']")
    #print(x) # just a test

if y >= 0 :

    print("Password is Correct :")

else:
    print("Passwords is Incorrect :")
            

#part 2
if (x>=0) and (y>=0) :

    menu = ""

    while (menu != "r") or (menu != "a") or (menu != "va") or (menu != "vm") or (menu != "e"):

            menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
ds - display stats

e - Exit
: ''').lower()
            if menu == 'r':

                pass
        
                if input_name=="admin":
                    new_name = input ("Enter your new register name :" )
                    new_password = input ("Enter your new register password :" )
                    password_confirm = input("Reenter password to confirm :")

                    if new_password == password_confirm :
                        with open ('user.txt' , 'a+') as f :
                            f.write(f"['{new_name}', '{new_password}']\n")

                    else:
                                password_confirm = input("Incorrect password. Reenter password to confirm :")
                                if new_password == password_confirm :
                                    with open ('user.txt' , 'a+') as f :
                                        f.write(f"['{new_name}', '{new_password}']\n")
                else:
                    print("Only admin has access")

            elif menu == 'a':

                pass
                user_task = input ("Enter username of the person responsible for task :" )
                title_task = input ("Enter title of the task:" )
                descrip_task = input ("Enter description of the task :" )
                due_task = input ("Enter date when task is due :" )

                with open ('tasks.txt' , 'a+') as f :
                    f.write(f"{user_task}, {title_task}, {descrip_task}, {today}, {due_task}, No\n")

            elif menu == 'va':
                pass

                file = open(f'tasks.txt', 'r')
                string_file = file.read().strip()
                onesplit_List = string_file.replace("\n",",").split(",")

                a=0
                b=1
                c=2
                d=3
                e=4
                f=5

                while(a < len(onesplit_List)):
                    print(f"Task :\t\t {onesplit_List[b]}")
                    print(f"Assigned to :\t  {onesplit_List[a]}")
                    print(f"Date assigned :\t {onesplit_List[d]}")
                    print(f"Due Date :\t {onesplit_List[e]}")
                    print(f"Task Complete:\t {onesplit_List[f]}")
                    print(f"Task description:{onesplit_List[c]}\n")
                    a += 6
                    b += 6
                    c += 6
                    d += 6
                    e += 6
                    f += 6
                
            elif menu == 'vm':
                pass

                file = open(f'tasks.txt', 'r')
                string_file = file.read().strip()
                onesplit_List = string_file.replace("\n",",").split(",")

                a=0
                b=1
                c=2
                d=3
                e=4
                f=5

        
                if f"{onesplit_List[a]}" == input_name:
                    print(f"Task :\t\t {onesplit_List[b]}")
                    print(f"Assigned to :\t  {onesplit_List[a]}")
                    print(f"Date assigned :\t {onesplit_List[d]}")
                    print(f"Due Date :\t {onesplit_List[e]}")
                    print(f"Task Complete:\t {onesplit_List[f]}")
                    print(f"Task description:{onesplit_List[c]}\n")
                        

            elif input_name == "admin":
                if menu == 'ds':

                     task_file = open("tasks.txt","r")
                     line_num = len(task_file.readlines())
                     print(f"Total number of tasks is : {line_num}")

                     user_file = open("user.txt","r")
                     line_num2 = len(user_file.readlines())
                     print(f"Total number of users is : {line_num2}\n")
                     
                    

            elif menu == 'e':
               print('Goodbye!!!')
               exit()

            else:
                print("You have made a wrong choice, Please Try again")
