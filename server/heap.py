import os.path
import json

#Priority formula:
#100/(daysTilDue)*(difficulty)

class taskList:
    class task:
        def __init__(name,difficulty,duedate,repeat):
            self._name = name
            self._difficulty = difficulty
            self._duedate = duedate
            self._repeat = repeat

    def getTasks(userName):
        if(os.path.isfile("users/" + userName)):
            print("exists")
            f = open("users/" + userName,"w")
        else:
            f = open("users/" + userName,"w+")
            #TODO init file
        json_dict = json.loads(f)

        #TODO create JSON object and return it in priority queue older
        for task in json_dict['tasks']:
            print(task)
        return 0;

    def addTask(userName,name,difficulty,duedate,repeat):
        f = open("users/" + userName,"w")
        #TODO create hash somehow?
        #TODO append json file
    
    def removeTask(userName,taskHash):
        print("totally removing it")
        #TODO actually remove teh task
