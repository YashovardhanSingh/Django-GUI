import subprocess
import os
import time

def startProject(directory, name):
    subprocess.run(f'''cd {directory} && django-admin startproject "{name}"''', shell=True)
    print("Project Created")

def openExistingProject(directory):
    dirs = subprocess.run(f'cd {directory} && dir', shell=True, capture_output = "True", text = True).stdout
    if "manage.py" in dirs:
        print(f"Django Project in {directory}")
        return directory
        #Maybe add for correct manage.py check

    else:
        print("No Django Project")
        return ""

def startApp(DjangoProject, appName):
    subprocess.run(f'''cd {DjangoProject} && python manage.py startapp "{appName}"''', shell=True)
    print("App Created")

def makeMigrations(DjangoProject):
    output = subprocess.run(f"cd {DjangoProject} && python manage.py makemigrations", shell=True, capture_output=True, text=True)
    print(f"{output}\nMigrations Made")

def migrate(DjangoProject):
    output = subprocess.run(f"cd {DjangoProject} && python manage.py migrate", shell=True, capture_output=True, text=True)
    print(f"{output}\nMigrated to Database")

def createSuperUser(DjangoProject,username,email,password, passwordAgain):
    if password == passwordAgain:
        subprocess.run(f'''cd {DjangoProject} && python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('{username}', '{email}', '{password}');"''', shell=True) 
        print("Super User created")

    else:
        print("Passwords don't match")

def runServer(DjangoProject, port=8000):
    # cmdPath = os.path.join(os.environ['WINDIR'], r'system32\cmd.exe')
    file = open('runServer.bat', 'w+')
    file.write(f'cd {DjangoProject}\npython manage.py runserver {port}')
    file.close()
    os.startfile('runServer.bat')
    time.sleep(2)
    os.remove('runServer.bat')

if __name__ == "__main__":

    directory = r'''C:\Users\Milind\Desktop\Test Dir\MilindApp'''
    # project_name = input("Enter Project Name: ")
    # startProject(directory,project_name)
    startApp(openExistingProject(directory), "AppName")
    migrate(openExistingProject(directory))
    createSuperUser(openExistingProject(directory),"helloworld","email@emailgmail.com","testPassword1234","testPassword1234")
    runServer(openExistingProject(directory), 5050)
