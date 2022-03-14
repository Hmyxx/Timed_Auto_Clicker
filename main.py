import time
import os
# import pyautogui
import datetime
import numpy as np
import pyautogui

def realpathoftasks():
    newpath = 'AutoClickerTasks'
    if not os.path.exists(newpath):
        command = input(
            "AutoClickerTasks folder cannot be found \n Do you want to create a new AutoClickerTasks folder \n yes - no\n")
        if command == "yes":
            os.makedirs(newpath)
            print("Folder created")
        elif command == "no":
            return 0
    # print("Path of the AutoClickerTasks ->" ,os.path.realpath(newpath))
    return os.path.realpath(newpath)

def run():
    textfilecounter = 0
    file_arr = os.listdir(realpathoftasks())

    for filename in file_arr:
        if not filename.find(".TXT") == -1:
            textfilecounter = textfilecounter + 1

    alarm_hours = [[0 for i in range(2)] for j in range(textfilecounter)]
    alarm_day = []
    alarm_name = []
    k = 0

    for filename in file_arr:
        if filename.find(".TXT") == -1:
            continue
        with open(realpathoftasks() + "\\" + filename, "r") as file:
            m = 0
            alarm_day.append(file.readline())
            for line in file:
                if line:  # lines (ie skip them)
                    line = line.strip()
                    alarm_hours[k][m] = line
                    m = m + 1
        alarm_name.append(filename)
        k = k + 1

    del m, k, file_arr, filename, file, line

    #print(alarm_hours) #controller
    #print(alarm_name)

    while True:
        counter = 0
        for i in alarm_name:
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M:%A\n")
            alarm_time = f"{alarm_hours[counter][0]}:{alarm_hours[counter][1]}:{alarm_day[counter]}"
            print(alarm_time)
            print(now)
            if now == alarm_time:
                execute_task(i)
                time.sleep(60)
            counter = counter + 1
        time.sleep(1)

def execute_task(alarm_name):
    alarm_path = realpathoftasks() + "\\" + alarm_name
    alarm_path = alarm_path[:-4]
    ss_name_arr = os.listdir(alarm_path)
    counter = 0
    pyautogui.hotkey('winleft', 'd')
    for ss_name in ss_name_arr:
        Find_n_click(alarm_path + "\\" + str(counter) + ".png")
        counter=counter+1

def Find_n_click(ss_alarm_path):
    seconds = 0
    while seconds != 4:
        print(ss_alarm_path)
        print("ARIYORUM")
        ToDo = pyautogui.locateOnScreen(ss_alarm_path,grayscale=True,confidence=0.9)
        if not ToDo == None:
            time.sleep(1)
            pyautogui.click(ToDo)
            print("BULDUM")
            time.sleep(1)
            break
        ToDo = None
        time.sleep(0.5)
        seconds=seconds+0.5

def addtask():
    taskname = input("Write the taskname : ")
    tasknametxt = taskname + ".TXT"
    arr = os.listdir(realpathoftasks())
    for i in arr:  # Dosya bulunuyor mu kontrol
        if i == tasknametxt:
            print("This task already exists")
            time.sleep(3)
            return

    alarmhour = input("Task initialization time (24 hours configuration)\n Hour = ")
    alarmhour = int(alarmhour)
    if alarmhour < 10:
        alarmhour = str(alarmhour)
        alarmhour = "0" + alarmhour
    alarmhour = str(alarmhour)
    alarmminute = input("Minute = ")
    alarmminute = int(alarmminute)
    if alarmminute < 10:
        alarmminute = str(alarmminute)
        alarmminute = "0" + alarmminute
    alarmminute = str(alarmminute)

    daynames = {"1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday", "5": "Friday", "6": "Saturday",
                "7": "Sunday"}
    alarmday = input("Write with number (ex:1 for monday) Day = ")
    alarmday=str(alarmday)
    os.system('cls')

    with open(realpathoftasks() + "\\" + tasknametxt, "w+") as file:
        file.write(daynames.get(alarmday) + "\n" + alarmhour + "\n" + alarmminute)
    os.makedirs(realpathoftasks() + "\\" + taskname)
    print("Task is added now you can add the screenshots of task")
    time.sleep(2)
    os.system('cls')

def deletetask():
    print(os.listdir(realpathoftasks()))
    task = input("Choose the task you want to delete (without .txt): ")
    taskpathtxt = realpathoftasks() + "\\" + task + ".TXT"
    if os.path.exists(taskpathtxt):
        os.remove(taskpathtxt)
    else:
        print("The file does not exist")

def no_such_action():
    print("There is no such command")

def print_menu():
    print("Commands list \n run \n addtask \n deletetask")

def main():
    actions = {"run": run, "addtask": addtask, "deletetask": deletetask}
    while True:
        print_menu()
        selection = input("Your selection: ")
        if "quit" == selection:
            return
        to_do = actions.get(selection, no_such_action)
        os.system('cls')
        to_do()

if __name__ == "__main__":
    main()
