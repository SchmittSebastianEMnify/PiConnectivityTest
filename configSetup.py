from configparser import ConfigParser

config = ConfigParser()

config['dnsLookUp'] = {
    'dnsServerIp': '',
    'domainName': '',
}

config['smallPing'] = {
    'hostToPing': '',
    'sizeInByte': '',
    'numberOfPings': ''
}

config['largePing'] = {
    'hostToPing': '',
    'sizeInByte': '',
    'numberOfPings': ''
}

config['httpDownload'] = {
    'url': '',
    'path': ''
}

config['logging'] = {
    'logLevel': '',
    'logFile': ''
}

with open('./config.ini', 'w') as f:
    config.write(f)