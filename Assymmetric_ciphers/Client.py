import pickle
import socket
from random import randint

HOST = '127.0.0.1'
PORT = 8083

def shif(wd, key):
    res = [chr(ord(wd[i]) ^ key) for i in range(len(wd))]
    return ''.join(res)

def rec(sock, K):
    msg = pickle.loads(sock.recv(1024))
    msg = shif(msg,K)
    return msg

def send(sock, msg, K):
    msg = shif(msg, K)
    sock.send(pickle.dumps(msg))

sock = socket.socket()
sock.connect((HOST, PORT))
p, g, a = [randint(0,250) for i in range(3)]
A = g ** a % p
sock.send(pickle.dumps((p, g, A)))
B = pickle.loads(sock.recv(1024))
K = B ** a % p
print('Enter text')
msg = input()



while msg != 'exit':
    send(sock,msg, K)
    print(rec(sock,K))
    msg = input()
sock.close()