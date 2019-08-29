import subprocess

def Ping(addresses, size, times):
    result = ""
    for address in addresses:
        try:
            output = ""
            pingOutput = str(subprocess.check_output(['ping', '-c', str(times), '-s', str(size), address]))
            lines = pingOutput.split("\\n")
            output += lines[0][2:] + "\n"
            for i in range(-3, -1, 1):
                output += lines[i] + "\n"
            output += "\n"
            print(output)
            result += output
        except Exception:
            result += "\nping to " + address + " failed\n\n"
            print("\nping to " + address + " failed\n")

    return result