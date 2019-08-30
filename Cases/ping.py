import subprocess
import logging

def Ping(address, size, times):
    if (not address) or size == 0 or times == 0:
        logging.error("address, size or number of times for ping in config not set")
        return 0

    logging.info("Starting ping to %s with size %s bytes %s times", address, size, times)
    try:
        pingOutput = str(subprocess.check_output(['ping', '-c', times, '-s', size, address]))
    except:
        logging.error("ping to host %s failed", address)
        return 0

    pingOutput = pingOutput[:-1].split('\\n')
    for line in pingOutput[1:-1]:
        logging.debug(line)
    return 1



