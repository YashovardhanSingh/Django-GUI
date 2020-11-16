import subprocess
import time
import threading

def checkPython():
    process = subprocess.run(['python','exit()'],shell=True, capture_output = True)
    if process.returncode != 2:
        print("Python not installed")


def checkPip():
    process = subprocess.run(['pip'],shell=True, capture_output = True)
    if process.returncode:
        print("Pip is not working, please fix pip")


def checkDjango():
    process = subprocess.run(['django-admin'],shell=True, capture_output = True)
    if process.returncode:
        print("Django not installed")
        # subprocess.run(['pip', 'install', 'django'], shell=True, text = True)

def checkVirtualenv():
    process = subprocess.run(['virtualenv'],shell=True, capture_output = True)
    if process.returncode != 2:
        print("Virtualenv is not installed") 
        # subprocess.run(['pip', 'install', 'virtualenv'], shell=True, text = True)

def checkNpm():
    process = subprocess.run(['npm'],shell=True, capture_output = True, text=True)
    if "is not recognized as an internal or external command" in process.stderr:
        print("NPM not installed")

if __name__ == "__main__":
    start = time.time()

    t1 = threading.Thread(target=checkPython)
    t2 = threading.Thread(target=checkPip)
    t3 = threading.Thread(target=checkDjango)
    t4 = threading.Thread(target=checkVirtualenv)
    t5 = threading.Thread(target=checkNpm)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
        
    end = time.time()
    
    print(end - start)


