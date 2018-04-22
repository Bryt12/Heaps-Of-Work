import os.path
import json

#Priority formula:
#100/(daysTilDue)*(difficulty)

def getTasks(userName):
    if(os.path.isfile("users/" + userName)):
        print("exists")
    else:
        f = open("users/" + userName,"w+")
        #TODO init file
        f.close()
    f = open("users/" + userName,"r")
    json_dict = json.loads(f.read().strip())


    #TODO create JSON object and return it in priority queue older
    
    #id
    #task_name
    #time_to_do
    #default = false
    #done = false
    #hash
    #how_long_it_takes

    for task in json_dict['tasks']:
        print(task)
    return 0;

def addTask(userName,name,difficulty,duedate,timeToDo,repeat):
    f = open("users/" + userName,"w")
    h = generateHash(dudedate,difficulty,name)
    
    #TODO append json file

def removeTask(userName,taskHash):
    print("totally removing it")
    #TODO actually remove the task

def generateHash(dudedate,difficulty,name):
        return hash(str(duedate)+str(difficulty)+str(name))


