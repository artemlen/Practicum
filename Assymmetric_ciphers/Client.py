import socket


def pg_key_gen(g, p, Ksc):
    Kpc = str(g ** Ksc % p)
    return Kpc


def key_gen(Kps, Ksc, p):
    K = (Kps ** Ksc) % p
    return K


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


def Client():
    sock = socket.socket()
    sock.setblocking(1)
    sock.connect(('127.0.0.1', 8089))

    Ksc = int(input('Enter your secret key:\n>'))

    data = sock.recv(1024).decode()
    data = data.split(' ')
    g = int(data[1])
    p = int(data[2])
    Kps = int(data[0])

    Kpc = pg_key_gen(g, p, Ksc)
    print("Your private key is generated")
    sock.send(Kpc.encode())

    K = key_gen(Kps, Ksc, p)
    print("Total key is generated\n")

    data = sock.recv(1024).decode()
    data = deshif(data, K)
    print(data)

    while True:
        msg = input()
        if msg == 'exit':
            break
        else:
            msg = shif(msg, K)

            sock.send(msg.encode())
        try:
            data = sock.recv(1024).decode()
        except:
            print("Server stoped ")
            break
        data = deshif(data, K)
        print(data)

    sock.close()


Client()
