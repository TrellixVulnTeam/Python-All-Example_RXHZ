import socket
host="https://www.facebook.com/"
try:
    addr=socket.gethostbyname(host)
    print("IP Address:-",+addr)
except socket.gaierror:
    print("The website does not exist...")