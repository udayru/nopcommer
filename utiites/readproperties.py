import configparser

config = configparser.RawConfigParser()
config.read('./configurations/config.ini')

class readdata:

    @staticmethod
    def seturl():
        url=config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def setusername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def setpassword():
        password = config.get('common info', 'password')
        return password