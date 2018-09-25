from flask import Flask
import time
import random
import hashlib
import requests

app = Flask(__name__)


@app.route("/checkImage/<data>/<hash>", methods=["GET"])
def checkImage(data, hash):
    cmd = "0"
    member = searchFamily(data)
    if not member:
        verifyUnknownImage(data)
        return notify(data)
    else:
        cmd = "1"

        hash_object = hashlib.sha384(cmd.encode())
        hex_dig = hash_object.hexdigest()
        r = requests.get("http://0.0.0.0:7003/unlockDoor/" + cmd + "/" + hex_dig)
        response = r.text
        return response

def searchFamily(currentImage):
    familyArray = ["image1", "image2"]
    if currentImage not in familyArray:
        return 0
    else:
        return 1

def verifyUnknownImage(currentImage):
    return "Verifying_the_unknown_image"

def notify(currentImage):
    return "Notification:_Unknown image"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='7002')
