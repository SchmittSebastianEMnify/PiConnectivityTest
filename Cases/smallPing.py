import subprocess

def SmallPing(addresses, size, times):
    result = ""
    for address in addresses:
        pingOutput = str(subprocess.check_output(['ping', '-c', str(times), '-s', str(size), address]))
        lines = pingOutput.split("\\n")
        for line in lines:
            result += line + "\n"
    return result