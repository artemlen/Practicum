#Import modules
import socket
from datetime import datetime
import time
import threading

#needs to be downloaded!
import pyprind

#Time of start
t1 = datetime.now()

#Number of ports:
N = 65536

#Enter host adress
host = input("Enter Host Adress: ")
ip = socket.gethostbyname(host) #Translate host to ipv4

#Print out
print("")
print("*" * 45)
print("Please wait, Scanning the Host ---->", ip)
print("*" * 45)
print("")

#Scaner function
spisok = []
spisok1 = []
def scanner(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #it use for Creates a stream socket
            sock.settimeout(0.1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                stroka = int("%d" %(port))
                spisok.append(stroka)
                print("\nПорт %d открыт" %(port))
                sock.close()  
            else:
                stroka1 = int("%d" %(port))
                spisok1.append(stroka1)
        except:
            pass

#Progress bar
Progress_bar = pyprind.ProgBar(N)


#Threading function
def thread_func(start, end):
    for i in range(start,end):
        scanner(ip,i)
        Progress_bar.update()

#Threading
thr1 = threading.Thread(target = thread_func, args = (0,int(N/16)))
thr2 = threading.Thread(target = thread_func, args = (int(N/16),int(N/16)*2))
thr3 = threading.Thread(target = thread_func, args = (int(N/16)*2,int(N/16)*3))
thr4 = threading.Thread(target = thread_func, args = (int(N/16)*3,int(N/16)*4))
thr5 = threading.Thread(target = thread_func, args = (int(N/16)*4,int(N/16)*5))
thr6 = threading.Thread(target = thread_func, args = (int(N/16)*5,int(N/16)*6))
thr7 = threading.Thread(target = thread_func, args = (int(N/16)*6,int(N/16)*7))
thr8 = threading.Thread(target = thread_func, args = (int(N/16)*7,int(N/16)*8))
thr9 = threading.Thread(target = thread_func, args = (int(N/16)*8,int(N/16)*9))
thr10 = threading.Thread(target = thread_func, args = (int(N/16)*9,int(N/16)*10))
thr11 = threading.Thread(target = thread_func, args = (int(N/16)*10,int(N/16)*11))
thr12 = threading.Thread(target = thread_func, args = (int(N/16)*11,int(N/16)*12))
thr13 = threading.Thread(target = thread_func, args = (int(N/16)*12,int(N/16)*13))
thr14 = threading.Thread(target = thread_func, args = (int(N/16)*13,int(N/16)*14))
thr15 = threading.Thread(target = thread_func, args = (int(N/16)*14,int(N/16)*15))
thr16 = threading.Thread(target = thread_func, args = (int(N/16)*15,int(N/16)*16))
thr1.start()
thr2.start()
thr3.start()
thr4.start()
thr5.start()
thr6.start()
thr7.start()
thr8.start()
thr9.start()
thr10.start()
thr11.start()
thr12.start()
thr13.start()
thr14.start()
thr15.start()
thr16.start()
thr1.join()
thr2.join()
thr3.join()
thr4.join()
thr5.join()
thr6.join()
thr7.join()
thr8.join()
thr9.join()
thr10.join()
thr11.join()
thr12.join()
thr13.join()
thr14.join()
thr15.join()
thr16.join()


#Time of end
t2 = datetime.now()

#Result time
common = t2-t1
print("Total time of program: ", common)
print("")

#print out list of opened ports
spisok.sort()
print('Список открытых портов: ', spisok)

#list of closed ports
#spisok1.sort()
#print('Список закрытых портов: ', spisok1)



