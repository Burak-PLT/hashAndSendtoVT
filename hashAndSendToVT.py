import sys
import requests
import hashlib

file = input("Please enter directory of file: ")
file = file.strip('"')
url = "https://www.virustotal.com/vtapi/v2/file/report"
BLOCKSIZE = 65536

hasher = hashlib.sha1()

with open(file, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)

fileHash = str(hasher.hexdigest())

parameters = {'apikey': <YOUR_API_KEY_HERE>, 'resource': fileHash}

response = (requests.get(url, params=parameters)).json()

if response['response_code'] == 0 :
    print(response['verbose_msg'])
elif response['response_code'] == 1 :
    print(response['scans'])
    print("Detected: " + str(response['positives']) + "/" + str(response['total']))
else :
    print("Something went wrong.")

exitmsg = input("Press any key to exit!")
