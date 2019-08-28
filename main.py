import Cases.dnsLookUp as dns
import Cases.ping as sPing
from config import *

result = 'Start:\n\n'


result += "ip addresses for domain " + domainName + " with " + dnsServerIp + " as dns server:\n"

ips = dns.DnsLookUp(dnsServerIp, domainName)
for ip in ips:
    result += str(ip) + "\n"

result += "\n\nSmall Pings\n"
result += sPing.Ping(hostsToPing1, sizeInByte1, numberOfPings1)

result += "Large Pings\n"
result += sPing.Ping(hostsToPing2, sizeInByte2, numberOfPings2)

print(result)

log = open("log.txt", "w+")
log.write(result)