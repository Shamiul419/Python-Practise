helloFile = open("/home/nirjhor/pytext/hello.text",)
print(helloFile.readline())
#print(helloFile.readline())
helloFile.close()
mm = open("sami.txt", 'w')
mm.write("sami")
mm.close()
import os
print(os.getcwd())