from requests import get
import socket
def get_public_ip():
    ip = get('https://api.ipify.org').text
    return ip
def get_local_ip():
    s = socket.socket(socket.AF_INET)
    try:
        s.connect(('google.com',80))
        ip=s.getsockname()[0]
        s.close()
    except:
        ip = 'N/A'
    return ip

print("Public (Router): " +get_public_ip())
print("Local (Device): " +get_local_ip())