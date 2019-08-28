import sh
import subprocess
import dns
import dns.resolver
import socket
import urllib.request

address = "8.8.8.8"
print("-----------")

pingOutput = str(subprocess.check_output(['ping', '-c', '1', '-s', '1024', address]))
lines = pingOutput.split("\\n")
for line in lines:
    print(line)

print("-----------")

myResolver = dns.resolver.Resolver()
myAnswers = myResolver.query("www.reddit.com", "A")
for rdata in myAnswers:
    print(rdata)

print("-----------")

print(socket.gethostbyname('www.youtube.com'))

print("-----------")

url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
urllib.request.urlretrieve(url, '/home/user/Downloads/cat.jpg')