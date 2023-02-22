import os
import sys

help_text='''
Usage: python setup-django [enviroment name] [project name]
setup-django is simple Python script automating the setup up of the Django Enviroment easy by one command,
seting up stepes:
[1] Virtual Enviromnet Made.
[2] Virtual Enviromnet Activited.
[3] Django Installing Done.
[4] Project starting Done.
[5] Django Server is Running !!!

Notce: If your OS is linux may you need to use "python3"
Notce: This script isn't alternative to understanding how django's enviroments work

\033[0;31;40msetup-django v1.1\033[0m

By: \033[0;34;40mMohanadBadra - Palestine\033[0m
'''
try:
    if sys.argv[1] == '-h' or sys.argv[1] == "--help" or sys.argv[1] == "/?":
        print (help_text)
        quit()
except Exception:
    pass

try:
    virtenv_name = sys.argv[1]
except:
    virtenv_name = "virtenv"
    
try:
    project_name = sys.argv[2]
except:
    project_name = "my_project"


# Finding out for same enviroments.
find_out = os.popen("ls").read()
find_out2 = os.popen("dir /b").read()
finded = str.split(find_out) + str.split(find_out2)

while str(virtenv_name) in finded or virtenv_name == "" or " " in str(virtenv_name):
    print("There is some enviroment by same NAME, pleas use another [enviroment name]")
    print("Usage: python setup-django [enviroment name] [project name]")
    print("Help: python setup-django -h\n")
    virtenv_name = input("[^C to cancel] Pleas enter a new name enviroment name: ")
    print("Notice: any spaces will removed")
    virtenv_name = virtenv_name.replace(" ","")
    
    
# Virtual Enviromnet Mading.
os.system(f"python -m venv {virtenv_name}")

print("\033[0;32;40m[*] Virtual Enviromnet Made\033[0m")

# Virtual Enviromnet Activing
os.system(f"{virtenv_name}\Scripts\\activate") #Important

print("\033[0;32;40m[*] Virtual Enviromnet Activited\033[0m")

# Django Installing
os.system("pip install django")

print("\033[0;32;40m[*] Django Installing Done\033[0m")

# Project starting
set_project = os.system(f"cd {virtenv_name} && django-admin startproject {project_name}")
str_project = str(set_project)

print("\033[0;32;40m[*] Project starting Done\033[0m")

# Django Server Running
os.system(f"cd {virtenv_name} && cd {project_name} && python manage.py runserver")

print("\033[0;32;40m[!] Django Server is Running...\033[0m")
print(f"virtual_enviroment: {virtenv_name}\nproject_name: {project_name}\nDone, and ready now..!")


# By: MohanadBadra - Palestine
