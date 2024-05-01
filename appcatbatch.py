import os

def list_folders(path):
    return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

folders =  list_folders(".\\src")

# run bat file
for folder in folders:
    os.system("appcatcli.bat " + folder)
