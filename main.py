import Cases.dnsLookUp as dns
import Cases.ping as sPing
import Cases.httpDownload as httpDownload
import time
from config import *

result = 'Start:\n\n'
print("Start:")

result += "ip addresses for domain " + domainName + " with " + dnsServerIp + " as dns server:\n"
print("ip addresses for domain " + domainName + " with " + dnsServerIp + " as dns server:")

ips = dns.DnsLookUp(dnsServerIp, domainName)
for ip in ips:
    result += str(ip) + "\n"

result += "\n\nSmall Pings:\n"
print("\n\nSmall Pings:")
result += sPing.Ping(hostsToPing1, sizeInByte1, numberOfPings1)

time.sleep(0.5)

result += "\nLarge Pings:\n"
print("Large Pings:")
result += sPing.Ping(hostsToPing2, sizeInByte2, numberOfPings2)

result += "\nhttp download:\n"
print("http download:")
result += httpDownload.HttpDownload(url, path)
print("\n")

log = open("log.txt", "w+")
log.write(result)
log.close()