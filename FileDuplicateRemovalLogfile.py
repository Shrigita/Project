import os
from sys import *
import hashlib
import time

def DeleteFiles(dict1):
    results = list(filter(lambda x:len(x) > 1,dict1.values()))

    icnt = 0

    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt +=1
                if icnt >=2:
                    os.remove(subresult)
            icnt = 0
    else:
        print("No Duplicate Files Found....")



def hashfile(path,blocksize=1024):
    afile =open(path,'rb')
    hasher =hashlib.md5()
    buf =afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf =afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()


def FindDup(path):
    flag = os.path.isabs(path)
    if flag == False:
        path =os.path.abspath(path)
    
    exists =os.path.isdir(path)

    dups = {}
    if exists :
        for dirName,Subdirs,fileList in os.walk(path):
            for filen in fileList:
                path=os.path.join(dirName,filen)
                file_hash =hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]
        return dups
    else:
        print("Invalid path")

def ProcessDisplaylog(dict1,log_dir = "Marvellous1"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator ="_" * 80
    log_path = os.path.join(log_dir,"MarvellousLog%s.log"%(time.ctime()))
    f = open(log_path,'w')
    f.write(separator +"\n")
    f.write("Marvellous Infosystem ProcessLogger :"+time.ctime()+"\n")
    f.write(separator + "\n")
  
    results = list(filter(lambda x:len(x) > 1,dict1.values()))

    if len(results) > 0:
        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    listprocess.append(subresult)

    for element in listprocess:
        f.write("%s\n" % element)
                  

def main():
    print("--------------Shrigita Automation---------------")

    print("Automation script started with name : ",argv[0])

    if(len(argv) != 3):
        print("Error : Insufficient arguments")
        print("Use -h for help and -u for usage of the script")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : this script is used to perform ------")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Provide ___number of argument as")
        print("First Argument as :______")
        print("Second Argument as :______")
        exit()
    try:
        arr ={}
        startTime =time.time()
        arr=FindDup(argv[1])
        ProcessDisplaylog(arr,argv[2])
        DeleteFiles(arr)
        endTime =time.time()

        print('Took %s seconds to evaluate'%(endTime -startTime))

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()