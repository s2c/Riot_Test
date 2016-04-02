import os

def debugger(staus,number):
    print status + " data " + str(i)


def set_path_to_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print script_dir
    up_dir = os.path.join( script_dir, '..' )
    print up_dir
    test = os.path.join( up_dir, 'data/matches.json' )

def get_data():
    i = 0
    set_pat_to_data()
    data_file = open(test,"w")
    url = 'https://s3-us-west-1.amazonaws.com/riot-api/seed_data/matches1.json'
    r = requests.get(url)
    data = r.json()
    debugger(i)
    json.dump(data,data_file,indent=4)
    data_file.close()
