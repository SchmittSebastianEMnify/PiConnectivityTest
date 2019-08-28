import subprocess

def Ping(addresses, size, times):
    result = ""
    for address in addresses:
        try:
            pingOutput = str(subprocess.check_output(['ping', '-c', str(times), '-s', str(size), address]))
            lines = pingOutput.split("\\n")
            result += lines[0][2:] + "\n"
            for i in range(-3, -1, 1):
                result += lines[i] + "\n"
            result += "\n\n"
        except:
            result += "\nping to " + address + " failed\n\n"

    return result