#f dotenv import load_dotenv
#from app import app, login_manager
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect
import os, os.path
import io
import sys

#load_dotenv()

#APP_KEY = os.environ.get("DBX_KEY")
#APP_SECRET = os.environ.get("DBX_SECRET")

debug = False

def authenticate():
    #TODO change this before deployment.
    APP_KEY = "FAKE_KEY"
    APP_SECRET = "FAKE_SECRET"

    auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

    authorize_url = auth_flow.start()
    print("1. Go to: " + authorize_url)
    print("2. Click \"Allow\" (you might have to log in first).")
    print("3. Copy the authorization code.")
    auth_code = input("Enter the authorization code here: ").strip()

    try:
        oauth_result = auth_flow.finish(auth_code)
    except Exception as e:
        print('Error: %s' % (e,))
        exit(1)

    return oauth_result


def download(oauth_result, download_list):
    with dropbox.Dropbox(oauth2_access_token=oauth_result.access_token) as dbx:

        dbx.users_get_current_account()
        print("Successfully set up client!")

        # Gather list of files
        for entry in download_list:
            local_path = entry['dest']
            remote_path = entry['src']
            src_dirs = entry['src'].split('/')
            try:
                file_list = dbx.files_list_folder(remote_path, recursive=True)
                list_of_files = [x.name for x in file_list.entries if x.name not in src_dirs]

                # debug
                if debug:
                    print(list_of_files)

                # download
                for file in list_of_files:
                    if (not os.path.isfile(local_path + file)):
                        print('Downloading file from: ' + remote_path + file + ', to: ' + local_path + file)
                        dbx.files_download_to_file(local_path + file, remote_path + file)
                    else:
                        print("File Already Exists!")
            except:
                print(remote_path +": File Not Found.")


def readfile(fn):
    fList = []
    with open(fn, "r+") as f:
        while line := f.readline():
            entry = {}
            line = line.strip()
            line = line.split(':')
            if (len(line) == 2):
                entry['src'] = line[0][:-1]
                entry['dest'] = line[1][1:]
                fList.append(entry)
            else:
                print('Formatting error')
    # debug
    if debug:
        print("File List")
        print(fList)

    return fList


def main(argv):

    input_file = ""
    if (len(argv) < 0):
        print("This script requires an input file of source and destination directories")
    elif (len(argv) > 1):
        print("This script requires only 1 argument")
    else:
        input_file = argv[0]
        fList = readfile(input_file)
        oauth_result = authenticate()
        download(oauth_result, fList)

if __name__ == "__main__":
    main(sys.argv[1:])
