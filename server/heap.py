import os.path

class priorityHeap:
    def __init__(userName):
        if(os.path.isfile("users/" + userName)):
            print("exists")
        else:
            f = open("users/" + userName,"w+")
            #TODO init file
        

