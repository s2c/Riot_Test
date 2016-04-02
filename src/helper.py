import os
import requests
import json

def debugger(status,number):
    print status + " data " + str(number)


def set_path_to_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
#    print script_dir
    up_dir = os.path.join( script_dir, '..' )
#    print up_dir
    test = os.path.join( up_dir, 'data/matches.json' )
    return test

def is_zero_file(fpath):
    return False if os.path.isfile(fpath) and os.path.getsize(fpath) > 0 else True

def get_data():
    i = 1
    path = set_path_to_data()
    if is_zero_file(path):
        data_file = open(path,"w")
        url = 'https://s3-us-west-1.amazonaws.com/riot-api/seed_data/matches1.json'
        r = requests.get(url)
        data = r.json()
        debugger("started",i)
        json.dump(data,data_file,indent=4)
        debugger("finished",i)
        data_file.close()
        print "Success!"
    #print "something went wrong:file exists and is filled, or error"
    return path
