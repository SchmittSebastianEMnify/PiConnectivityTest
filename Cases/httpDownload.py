import urllib.request

def HttpDownload(url, path):
    result = ""
    try:
        urllib.request.urlretrieve(url, path)
        result += "download from " + url + " to " + path + " successful"
        print("download from " + url + " to " + path + " successful")
    except:
        result += "http download failed"
        print("http download failed")

    return result