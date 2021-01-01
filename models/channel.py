from .storage import Storage

class Channel:

    def add(id):
        if(Channel.exist(id)):
            return
        channels = Storage.read('channels.json')
        channel = {
            'id': id
        }
        channels.append(channel)
        Storage.write('channels.json', channels)

    def exist(id):
        try:
            channels = Storage.read('channels.json')
        except FileNotFoundError:
            return False

        for channel in channels:
            if(channel['id'] == id):
                return True
        return False