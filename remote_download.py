import configparser

config=configparser.ConfigParser()
config.read('rd.ini')
print(config['remote_server']['address'])