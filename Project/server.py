import socket
import pickle

host="127.0.0.1"
port=4337


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)



s.bind((host,port))


s.listen()


conn,addr=s.accept()




gercekcumle="KULE"
yazilacakcumle=["K","*","*","*"]

if conn:
    print(f"Kullanıcı basariyla bağlandı:{addr}")
    print("K***")
    count=0
    while True:
        count=count+1
        if count == 5:
            print("\nNe yazıkki kalan hakkınız kalmamıştır.")




        ldata=conn.recv(1024)

        cumle = ldata.decode("utf-8")
        if cumle == gercekcumle:
            print("Tebrikler")
            dat="1"
            conn.send(dat.encode("utf-8"))

            conn.close()
            break
        else :
            dat = "0"
            if count==5:
                dat="10"
            conn.send(dat.encode("utf-8"))
            if dat=="10":
                conn.close()
                break

        i=0
        while True:
            if gercekcumle[i] in cumle:
                if cumle[i] == gercekcumle[i]:

                    yazilacakcumle[i]=cumle[i]

                else:
                    yazilacakcumle[i]=cumle[i].lower()





            else:
                yazilacakcumle[i]="*"


            if i == 3:
                break
            i = i + 1

        data900=pickle.dumps(yazilacakcumle)
        conn.send(data900)








