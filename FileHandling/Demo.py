f=open("abc.txt", 'w')
print("File Name:-",f.name)
print("File Mode:-",f.mode)
print("File Readable:-",f.readable())
print("File Writable:-",f.writable())
print("File Closed:-",f.close)
f.close()
print("File Name:-",f.close)
