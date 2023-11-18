import time
import csv
import pandas

# Iterates over the tasks
def tasks():
    print("Hello, these are your tasks:")
    with open(r"tasks.csv", "r") as file:
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
        with open(r"tasks.csv", "a") as file:
            write = csv.writer(file, delimiter = " ")
            write.writerow([task_name, task_field, task_time])
        print("Task added sucessfully!")
    elif task_manage == "del":  
        delete_tasks()

# Function to delete tasks
def delete_tasks():
        time.sleep(1)
        df = pandas.read_csv(r"tasks.csv")
        print(df)
        del_row = int(input("Which tasks whould you like to delete? [type corresponsing row] "))
        df = df.drop(index = del_row)
        df.to_csv(r"tasks.csv", index = False)
        print("Task sucessfully deleted!")

tasks()
