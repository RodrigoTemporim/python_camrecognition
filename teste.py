import os

DirPath = 'conhecidos'
Files = os.listdir(DirPath)
for File in Files:
    imgPath = os.path.join(DirPath, File)
    print(imgPath)