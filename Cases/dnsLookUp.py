import dns.resolver

def DnsLookUp(dnsServerIp, domainName):
    if dnsServerIp == "" or domainName == "":
        print("dns server or domain name not configured")

    dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
    dns.resolver.default_resolver.nameservers = [dnsServerIp]

    try:
        myAnswers = dns.resolver.query(domainName, "A")
        for ip in myAnswers:
            print(str(ip))
    except:
        return(["Error while dns lookup"])
        print("Error while dns lookup")


    return myAnswers
