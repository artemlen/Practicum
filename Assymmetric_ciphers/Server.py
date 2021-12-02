import pickle
import socket
from random import randint


HOST = '127.0.0.1'
PORT = 8083

def shif(wd, key):
    res = [chr(ord(wd[i]) ^ key) for i in range(len(wd))]
    return ''.join(res)


def send(conn, msg, K):
    msg = shif(msg, K)
    conn.send(pickle.dumps(msg))


def rec(conn, K):
    msg = pickle.loads(conn.recv(1024))
    msg = shif(msg, K)
    return msg


sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

msg = conn.recv(1024)
p, g, A = pickle.loads(msg)
b = randint(10, 250)
B = g ** b % p
conn.send(pickle.dumps(B))
K = A ** b % p




while True:
    try:
        msg = rec(conn, K)
        print(msg)
        send(conn, msg, K)
    except:
        break
conn.close() 