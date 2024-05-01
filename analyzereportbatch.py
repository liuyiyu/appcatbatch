#open a json file
#parse the json file
#extract the data
#analyze the data
#return the data

import json
import os

def analyze_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data



def analyze_issues(filename):
    # i.e. 'C:\\dev\\appcatbatch\\report\\hellospring.report\\api\\issues.json'
    jsondata = analyze_json_file (filename)

    print ("#############################################")
    print ('analyzeing:' + filename)
    print ("#############################################")
    data = jsondata[1]['issues']['information']
    for issues in data:
        if( issues['name'] == "S3 found in the application"):
            print (issues['affectedFiles'])
            
#list first level  folder in a directory
def list_folders(path):
    return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

folders =  list_folders(".\\report")

for folder in folders:
    analyze_issues(".\\report\\" + folder + "\\api\\issues.json")

