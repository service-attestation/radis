from flask import Flask
import time
import random
import hashlib
import requests

app = Flask(__name__)

@app.route("/unlockDoor/<cmd>/<hash>", methods=["GET"])
def unlockDoor(cmd, hash):
    if int(cmd) is 1:
        response = unlock()
    else:
        response = lock()
    hash_object = hashlib.sha384(response.encode())
    hex_dig = hash_object.hexdigest()
    return response + " " + hex_dig
    #return response

def lock():
    return "Locking_Door"

def unlock():
    return "Unlocking_Door"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='7003')
