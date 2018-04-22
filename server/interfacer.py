import json
import requests

class Interfacer():
    def __init__(front_end_url, port):
        self.fe_url = front_end_url
        self.port = port
    
    def send(queue, uid):
        output_raw = []

        for element in queue:
            entry = {}
            entry['name'] = element.name
            entry['due_date'] = element.due_date

            output_raw.append(element)

        json_str = json.dumps(output_raw)
        

    def get():
        pass
