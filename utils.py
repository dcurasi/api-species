from constant import BASE_URL, TOKEN


import constant
import requests

def getRegions():
    response = requests.get(BASE_URL + "region/list?token=" + TOKEN)
    if(response.status_code != 200):
        print("An error occurred!")
        return False
    if(response.json().get('error')):
        print(response.json().get('error'))
        return False
    return response.json()

def getSpeciesFromRegion(region_id, page = 0):
    response = requests.get(BASE_URL + "species/region/" + region_id + "/page/" + str(page) + "?token=" + TOKEN)
    if(response.status_code != 200):
        print("An error occurred!")
        return False
    if(response.json().get('error')):
        print(response.json().get('error'))
        return False
    return response.json()

def getConservationMeasures(specie_id, region_id):
    response = requests.get(BASE_URL + "measures/species/id/" + str(specie_id) + "/region/" + region_id + "?token=" + TOKEN)
    if(response.status_code != 200):
        print("An error occurred!")
        return False
    if(response.json().get('error')):
        print(response.json().get('error'))
        return False
    return response.json()