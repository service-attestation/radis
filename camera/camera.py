from flask import Flask
# from picamera import PiCamera
import time
import random
import hashlib
import requests

app = Flask(__name__)

@app.route("/")
def captureImage():

    # camera = PiCamera()

    capturesArray = ["image1", "image2", "image3"]
    if motion>-1:
        val = capturesArray[figIndex]
        hash_object = hashlib.sha1(val.encode())
        hex_dig = hash_object.hexdigest()
        r = requests.get("http://0.0.0.0:7002/checkImage/" + val + "/" + hex_dig)
        response = r.text
        #data = response.split(" ")
        #output = data[0]
        #hash = data[1]
        return response
    else:
        return("No motion detected")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='7001')
