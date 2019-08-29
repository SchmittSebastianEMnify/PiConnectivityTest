#Case 1: dns look up
dnsServerIp = '8.8.8.8'
domainName = 'www.stackoverflow.com'

#Case 2: small pings
hostsToPing1 = ['www.goonn,gle.com', 'www.ehkjhkmnify.de']
sizeInByte1 = 64
numberOfPings1 = 3

#Case 3: large pings
hostsToPing2 = ['www.goffffffdsogle.com', 'www.emndsfgify.de']
sizeInByte2 = 20
numberOfPings2 = 2

#Case 4: http Dowload
url = 'https://wiki.ubuntu.com/'
path = '$(PWD)/ubuntuWiki.html'
