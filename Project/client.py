import socket
import pickle





host="127.0.0.1"
port=4337


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))
print("K***")
j=1

while True:
    print("\n")




    data90 = input(" 4 Haneli cümle giriniz:")
    s.send(data90.encode("utf-8"))

    da=s.recv(1024)
    if da.decode("utf-8")=="1":
        print("Tebrikler")
        s.close()
        break
    if da.decode("utf-8")=="10":
        print("Kalan hakkınız bitmiştir")
        s.close()
        break




    ldata = s.recv(1024)
    data1000=pickle.loads(ldata)
    j=0






    while j<4:
        print(data1000[j],end="")
        j=j+1





