import urllib.request
import logging

def HttpDownload(url, path):
    if url == "" or path == "":
        logging.error("url or path in config not set")
        return 0

    logging.info("start download from %s to %s", url, path)
    try:
        urllib.request.urlretrieve(url, path)
        return 1
    except:
        logging.error("download from %s to %s failed", url, path)
        return 0
