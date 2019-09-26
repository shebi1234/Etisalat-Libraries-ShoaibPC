from configparser import ConfigParser


class Variables(object):
    def variable1(self):
        try:
            config = ConfigParser()
            config.read('libraries/Config.ini')
            return config.get('Path', 'filepath')
        except Exception as e:
            raise e
