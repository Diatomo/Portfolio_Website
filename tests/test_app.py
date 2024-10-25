
import requests
import os

from dotenv import load_dotenv

load_dotenv()




'''
    Test all pages
'''
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

#extra '/' at end of endpoint because it is an index of a blueprint
def test_musicfest(client):
    response = client.get("/musicfest/")
    assert response.status_code == 200

def test_synthclips(client):
    response = client.get("/synthjam")
    assert response.status_code == 200

def test_photoviewer(client):
    response = client.get("/photoviewer/login")
    assert response.status_code == 200

def test_photoviewer_demo(client):
    response = client.get("/photoviewer/demo")
    assert response.status_code == 200

def test_photoviewer_demo(client):
    response = client.get("/photoviewer/demo_upload")
    assert response.status_code == 200

def test_trivco(client):
    response = client.get("/trivco")
    assert response.status_code == 200

def test_tias(client):
    response = client.get("/old_tias")
    assert response.status_code == 200

#external link
def test_asteroids(client):
    url = 'https://py2.codeskulptor.org/#user49_GFkrajcmPH_1.py'
    response = requests.get(url)
    assert response.status_code == 200


'''
    Test photoviewer login
'''

#Test reirected from protected pages
def test_redirect_photoviewer_menu(client):
    response = client.get("/photoviewer/")
    assert response.status_code == 302

def test_redirect_photoviewer_upload(client):
    response = client.get("/photoviewer/upload")
    assert response.status_code == 302

def test_redirect_photoviewer_photo(client):
    response = client.get("/photoviewer/family_photos/2024/Michigan/photo")
    assert response.status_code == 302


'''
    Test photoviewer login
'''
def sim_login(client):
    FAMILY_USERNAME = os.environ.get("FAMILY_USERNAME")
    FAMILY_PASSWORD = os.environ.get("FAMILY_PASSWORD")
    response = client.get('/photoviewer/login')
    csrf_token = response.data.decode().split('name="csrf_token" type="hidden" value="')[1].split('"')[0]


    #encodes data to be form data (required form WTF validation)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html'
    }

    data = {
        'csrf_token': csrf_token,
        'username': FAMILY_USERNAME,
        'password': FAMILY_PASSWORD,
        'submit': 'Submit'
    }

    response = client.post('/photoviewer/login', data=data, headers=headers)
    return client


#Test redirected from protected pages
def test_redirect_photoviewer_index_after_login(client):
    sim_login(client)
    response = client.get("/photoviewer/")
    assert response.status_code == 200

def test_redirect_photoviewer_upload_after_login(client):
    sim_login(client)
    response = client.get("/photoviewer/upload")
    assert response.status_code == 200

def test_redirect_photoviewer_photo_after_login(client):
    sim_login(client)
    response = client.get("/photoviewer/family_photos/2024/Michigan/photo")
    assert response.status_code == 200
