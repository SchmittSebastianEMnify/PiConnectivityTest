import Cases.dnsLookUp as dns
import Cases.ping as ping
import Cases.httpDownload as httpDownload
import configparser
import logging
import sys

def GetConfigValue(section, name, config):
    try:
        return config.get(section, name)
    except:
        logging.critical("config.ini corrupted")
        exit()


logginglevels = {
    "DEBUG" : 10,
    "INFO" : 20,
    "WARNING" : 30,
    "ERROR" : 40,
    "CRITICAL" : 50
}

config = configparser.ConfigParser()
try:
    config.read('config.ini')
except:
    logging.basicConfig(format='%(asctime)s: %(message)s')
    logging.critical("config.ini file not found")
    exit()

if len(sys.argv) > 2:
    logging.basicConfig(format='%(asctime)s: %(message)s')
    logging.critical("to many commandline parameters")
    exit()

logLevel = ""
if len(sys.argv) == 2:
    logLevel = str(sys.argv[1])
else:
    logLevel = GetConfigValue('logging', 'loglevel', config)

intLogLevel = logginglevels.get(logLevel.upper(), 20)

logFile = GetConfigValue("logging", "logFile", config)

logging.basicConfig(level=intLogLevel, format='%(asctime)s: %(message)s', filename=logFile)

if logginglevels.get(logLevel.upper(), None) == None:
    logging.warning("log level %s doesnt exist. Using log level INFO as default", logLevel.upper())

logging.info("------starting tests--------")

dnsServerIp = GetConfigValue("dnsLookUp", "dnsServerIp", config)
domainName = GetConfigValue("dnsLookUp", "domainName", config)

if dns.DnsLookUp(dnsServerIp, domainName):
    logging.info("dns look up successful")
else:
    logging.error("dns look up failed")

htp1 = GetConfigValue("smallPing", "hostToPing", config)
size1 = GetConfigValue("smallPing", "sizeInByte", config)
number1 = GetConfigValue("smallPing", "numberOfPings", config)

if ping.Ping(htp1, size1, number1):
    logging.info("small ping successful")
else:
    logging.error("small ping failed")

htp2 = GetConfigValue("largePing", "hostToPing", config)
size2 = GetConfigValue("largePing", "sizeInByte", config)
number2 = GetConfigValue("largePing", "numberOfPings", config)

if ping.Ping(htp2, size2, number2):
    logging.info("large ping successful")
else:
    logging.error("large ping failed")

url = GetConfigValue("httpDownload", "url", config)
path = GetConfigValue("httpDownload", "path", config)

if httpDownload.HttpDownload(url, path):
    logging.info("http download successful")
else:
    logging.error("http download failed")