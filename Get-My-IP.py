import socket

import socket

import socket
import requests
print(" ")
print("Your local IP is  " + socket.gethostbyname(socket.gethostname()))
print(" ")
try :
    print("Your public IP is " + requests.get("https://api.ipify.org").text)
except requests.ConnectionError:
    print("Connection failed...! *_*")
input("Press enter to exit.")