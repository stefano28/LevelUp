import json

class Storage:

    def read(file_name):
        try:
            f = open('AppData/' + file_name, 'r')
            json_data = json.load(f)
            f.close()
        except FileNotFoundError:
            Storage.create(file_name)
            json_data = []
        return json_data

    def create(file_name):
        f = open('AppData/' + file_name, 'x')
        f.write("[]")
        f.close()

    def write(file_name, data):
        f = open('AppData/' + file_name, 'w')
        f.write(json.dumps(data, indent=4))
        f.close()