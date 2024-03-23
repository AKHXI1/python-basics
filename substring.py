fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
for fileName in fileList:
    if ".exe" in fileName:
        print(fileName)