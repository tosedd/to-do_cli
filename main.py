# CLI To-Do script
# Todor Todorovski 2023
''' 1: The programme on starts shows the previously added to-do's (if any). In the case of none, prints a sentence.
    2: The programme waits 8-10sec. and prompts the user if he wants to add a new todo(y/n). Prompts is separated graphically
    from the first function.
    3:If yes>prompt to enter and add the todo to the list. If no>"Bye".
    >>The programme stores its data on a separate file
    4: The programme automatically sets int values to every task created [task [1], task [2]...]
'''
import time
import csv
import pandas

# Iterates over the tasks
def tasks():
    print("Hello, these are your tasks:")
    with open(r"C:\Users\11\Desktop\Python projects\task_manager\tasks.csv", "r") as file:
        reader = csv.reader(file, delimiter=" ")
        for lines in reader:
            print(" ".join(lines))
        time.sleep(1)
        main()

# MAIN Function, runs after the printing of tasks
def main():
    task_manage = input("Do you want to add/delete a new todo? [add/del]: ")
    if task_manage == "add":
        task_name = input("Please state task name: ")
        task_field = input("Please specify task field: ")
        task_time = input("Please specify due date: ")
        with open(r"C:\Users\11\Desktop\Python projects\task_manager\tasks.csv", "a") as file:
            write = csv.writer(file, delimiter = " ")
            write.writerow([task_name, task_field, task_time])
        print("Task added sucessfully!")
    elif task_manage == "del":  
        delete_tasks()

# Function to delete tasks
def delete_tasks():
        time.sleep(1)
        df = pandas.read_csv(r"C:\\Users\\11\Desktop\\Python projects\\task_manager\\tasks.csv")
        print(df)
        del_row = int(input("Which tasks whould you like to delete? [type corresponsing row] "))
        df = df.drop(index = del_row)
        df.to_csv(r"C:\\Users\\11\Desktop\\Python projects\\task_manager\\tasks.csv", index = False)
        print("Task sucessfully deleted!")

tasks()