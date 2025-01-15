"""
This is a simple To-Do List program.
It allows users to add, remove, and view tasks in a list.
"""

from colorama import Fore, Back, Style

def display_menu(): #Small menu to display what can be done in this app
    print(Fore.YELLOW + "\nTo-Do List Menu:" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "\n1. Add Tasks \n2. Remove Tasks \n3. View Tasks \n4. Exit the App" + Style.RESET_ALL)

def add_tasks(tasks): #Function to add tasks to the list
    adding_task = input(Fore.CYAN + "\nEnter your task: " + Style.RESET_ALL)
    tasks.append(adding_task) #Tasks are added to the list using append
    print(Fore.LIGHTCYAN_EX + f"\n'{adding_task}' has been added to your list." + Style.RESET_ALL)

def remove_tasks(tasks):
    view_tasks(tasks) #Calling the function to view the tasks in the list
    if tasks: #If tasks are present in the list, it proceeds
        try:
            task_num = int(input(Fore.RED + "\nEnter the number of the task you wish to remove: " + Style.RESET_ALL))
            if 1 <= task_num <= len(tasks): #Checks if the task number is present in the list
                #If task number mentioned is more than 0 and within the list range, it proceeds
                removing_task = tasks.pop(task_num - 1) #Removes task successfully using pop
                print(Fore.LIGHTRED_EX + f"\n'{removing_task}' has been removed from your list." + Style.RESET_ALL)
            else:
                print(Fore.MAGENTA + "\nInvalid task number." + Style.RESET_ALL) 
                #If task number does not meet the conditions, it gives this message
        except ValueError: #This block catches error if user inputs non-numeric value
            print(Fore.MAGENTA + "\nInvalid input. Please enter a number." + Style.RESET_ALL)

def view_tasks(tasks):
    if not tasks: #If tasks are not present in the list, it gives this message
        print(Fore.MAGENTA + "\nYour list is empty!" + Style.RESET_ALL)
    else: #Since tasks are present in the list, we output the list
        print(Fore.GREEN + "\nYOUR TO-DO LIST: " + Style.RESET_ALL)

        #Viewing the list by using a for loop which iterates through the tasks list
        #index stores current position, task stores current value
        #enumerate() lets us loop over a list
        #start tells to start numbering index from 1 instead of 0

        for index, task in enumerate(tasks, start=1):
            print(Fore.LIGHTBLACK_EX + f"{index}. {task}" + Style.RESET_ALL) 
            #Outputs index and task. Example: 1. Buy Groceries

def main():
    print(Style.BRIGHT + "\nTO DO LIST APP" + Style.RESET_ALL)

    tasks = [] #Creating list to store tasks

    while True:
        display_menu() #Viewing the main menu
        ch = input(Fore.LIGHTBLUE_EX + "\nMake your choice: " + Style.RESET_ALL) 
        #Making a choice what to do with the to-do list app

        if ch == "1": #As per the choice, add function is called
            add_tasks(tasks)
        elif ch == "2": #As per the choice, remove function is called
            remove_tasks(tasks)
        elif ch == "3": #As per the choice, view function is called
            view_tasks(tasks)
        elif ch == "4": #As per the choice, if-else breaks and we exit the app
            print(Fore.LIGHTMAGENTA_EX + "\nThank you for using the app!" + Style.RESET_ALL)
            print("\n")
            break
        else: #If anything other than 1-4 is chosen, it is invalid
            print(Fore.MAGENTA + "\nInvalid choice." + Style.RESET_ALL)
if __name__ == "__main__": #Making sure only the main function is executed whenever necessary
    main()
