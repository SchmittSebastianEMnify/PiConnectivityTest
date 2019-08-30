import dns.resolver
import logging

def DnsLookUp(dnsServerIp, domainName):
    if dnsServerIp == "" or domainName == "":
        logging.error("dns server or domain name in config not set")
        return 0

    logging.info("dns look up for domain %s with %s as dns server", domainName, dnsServerIp)
    dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
    dns.resolver.default_resolver.nameservers = [dnsServerIp]

    try:
        result = dns.resolver.query(domainName, "A")
        for ip in result:
            logging.debug(str(ip))
        return 1
    except:
        logging.error("host Name not known")
        return 0

