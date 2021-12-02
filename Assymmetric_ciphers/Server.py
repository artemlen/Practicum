import socket
import csv
import os

file = os.path.join(os.getcwd(), 'keys.csv')
with open (os.path.join(os.getcwd(), 'keys.csv'), 'r+') as fl:
    t = 0
    for line in csv.reader(fl):
        if t == 0:
            p = int(''.join(line))
        elif t == 1:
            g = int(''.join(line))
        elif t == 2:
            a = int(''.join(line))
        t += 1



def key_gen(kpc):
    global a, g, p
    K = (int(kpc) ** a) % p
    return K


def pg_key_gen(conn, p, g):
    with open(os.path.join(os.getcwd(), 'keys.csv'), 'r+') as f:
        i = 0
        for line in csv.reader(f):
            if i == 3:
                Kps = int(''.join(line))
            i += 1
    msg = str(Kps) + ' ' + str(g) + ' ' + str(p)
    conn.send(msg.encode())
    return Kps




def check_ksc(kpc):
    global file
    with open(file, 'r+') as fl:
        know = False
        for line in csv.reader(fl):
            if kpc in line:
                know = True
                return True
        if know == False:
            return False


def shif(wd, k):
    msgl = list(wd)
    for i in range(len(msgl)):
        msgl[i] = chr(ord(msgl[i]) + k)
    wd = ''.join(msgl)
    return wd


def deshif(wd, k):
    msgl = list(wd)
    for i in range(len(msgl)):
        msgl[i] = chr(ord(msgl[i]) - k)
    wd = ''.join(msgl)
    return wd


def Server_work():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 8089))
    sock.listen(0)

    while True:
        conn, addr = sock.accept()
        print(addr)
        pg_key_gen(conn, p, g)
        kpc = conn.recv(1024).decode()
        print("Client's public key recieved")
        if check_ksc(kpc) == True:
            print("Client found")
            pass
        else:
            print("Client is not known")
            conn.close()
            continue
        print("key is generated")


        K = key_gen(kpc)
        conn.send(shif("Now you in the server (type exit to finish Server)", K).encode())

        while True:
            try:
                data = conn.recv(1024).decode()
            except:
                break
            data = deshif(data, K)
            print(data)
            msg = "recieved: " + data
            msg = shif(msg, K)
            conn.send(msg.encode())
        conn.close()


Server_work()
