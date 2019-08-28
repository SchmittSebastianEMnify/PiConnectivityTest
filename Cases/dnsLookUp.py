import dns.resolver

def DnsLookUp(dnsServerIp, domainName):
    dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
    dns.resolver.default_resolver.nameservers = [dnsServerIp]

    try:
        myAnswers = dns.resolver.query(domainName, "A")
    except:
        return(["Error while dns lookup"])


    return myAnswers
