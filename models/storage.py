import json

class Storage:

    def read(file_name):
        f = open('AppData/' + file_name, 'r')
        json_data = json.load(f)
        f.close()
        return json_data

    def write(file_name, data):
        try:
            json_data = Storage.read(file_name)
        except FileNotFoundError:
            f = open('AppData/' + file_name, 'x')
            json_data = []
            f.close()
        json_data.append(data)
        f = open('AppData/' + file_name, 'w')
        f.write(json.dumps(json_data, indent=4))
        f.close()