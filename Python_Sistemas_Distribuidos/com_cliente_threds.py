from socket import  *
import threading
import sys

def recebe():
        while True:
                data = s.recv (4096)
#                if len(data) == 0:
#                        break
                print (data.decode('UTF-8'))        

s = socket ()

#meusbytes=str.encode (minhastr, "UTF-8")
#print (meusbytes)

servidor="10.10.13.3"
porta=8753

s.connect((servidor, porta))
t = threading.Thread(target=recebe,args=())
t.start()

while True:
        print ("Frase:", end=' ')
        ss=""
        
        c = input()
        if(c == ' '):
                 continue        

        if (c == '\n'):
        	 break
                
        ss+=c
        s.send (str.encode(ss , "UTF-8"))



s.close ()
