import sys
import os
import shutil


def func(path):
    folders = os.listdir(path)
    name= list()
    extn = list()
    x=0
    file_no = 0
    folder_no = 0
    file_=list()
    fold_=list()
    for i in folders:
     p,q = os.path.splitext(i)
     x +=1
     if os.path.isfile(os.path.join(path,i)):
         file_no +=1
         file_.append(i)
         print(str(x)+"."+i+"  - - > FILE")
     else:
         folder_no +=1
         fold_.append(i)
         print(str(x)+"."+i+"  - - > FOLDER")

    return file_,fold_




 
path1 = "D:\\PERSONAL\\PYTHON\\PySort\\folder 2\\fold 2"

print(path1)
 

file = list()
folder = list()
file,folder = func(path1)

##print(file)
##print(folder)


for i in file:
    if os.path.isfile(os.path.join(path1,i)):
     p,q = os.path.splitext(i)
     q=q[1:]
     print(p," ",q)
     if os.path.exists(os.path.join(path1,q)):
       shutil.move(os.path.join(path1,i),os.path.join(path1,q))
     else:
       os.mkdir(os.path.join(path1,q))
       shutil.move(os.path.join(path1,i),os.path.join(path1,q))


