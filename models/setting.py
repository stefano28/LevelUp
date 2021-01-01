from .storage import Storage

class Setting:

    def set_comunication_channel_id(comunication_channel_id):
        settings = Storage.read('settings.json')
        settings['comunication_channel_id'] = int(comunication_channel_id)
        Storage.write('settings.json', settings)

    def get_comunication_channel_id():
        settings = Storage.read('settings.json')
        return settings['comunication_channel_id']