from configparser import ConfigParser


class variables(object):
    def variable1(self):
        try:
            config = ConfigParser()
            config.read('Libraries/Config.ini')
            return config.get('dir', 'filepath')
        except Exception as e:
            raise e

    def variable2(self):
        try:
            config = ConfigParser()
            config.read('Libraries/Config.ini')
            return config.get('targetpath', 'targetdir')
        except Exception as e:
            raise e