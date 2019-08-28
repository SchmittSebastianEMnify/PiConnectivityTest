import Cases.dnsLookUp as dns
import Cases.smallPing as sPing
from config import *

result = 'Start:\n\n'


result += "ip addresses for domain " + domainName + " with " + dnsServerIp + " as dns server:\n"

ips = dns.DnsLookUp(dnsServerIp, domainName)
for ip in ips:
    result += str(ip) + "\n"

result += sPing.SmallPing(hostsToPing, sizeInByte, numberOfPings)

print(result)

log = open("log.txt", "w+")
log.write(result)