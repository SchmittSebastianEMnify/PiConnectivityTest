import dns.resolver

def DnsLookUp(dnsServerIp, domainName):
    dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
    dns.resolver.default_resolver.nameservers = [dnsServerIp]

    myAnswers = dns.resolver.query(domainName, "A")
    return myAnswers
