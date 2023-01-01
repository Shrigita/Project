import os
import psutil
import time
from sys import *

def ProcessDisplay(log_dir = "Marvellous"):
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

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms =proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

def main():
    print("--------------Shrigita Automation---------------")

    print("Automation script started with name : ",argv[0])

    if(len(argv) != 2):
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
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()