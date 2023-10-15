import zipfile
filename = "./zip-25000.zip"
path = "./"
password="./password.txt"

for i in range(25000):
    


    with open("./password.txt","r") as f:
        passwd=f.read()
        passwd=passwd.strip()


        
        
    with zipfile.ZipFile(filename, "r") as zp:
        try:
            zp.extractall(path=path, pwd=passwd.encode())
            
            
        except RuntimeError as e:
            print(e)
            
    filename=path+"zip-"+str(24999-i)+".zip"
