import requests
import re

def yandex_geolocator(address):
    address = address.replace(' ', '%20')
    address = re.sub(r'[^\w\s]', '', address)
    
    r = requests.get(f'https://suggest-maps.yandex.com/suggest-geo?add_chains_loc=1&add_coords=1&add_rubrics_loc=1&bases=geo,biz,transit&client_reqid=1683724525699_249094&custom_ranking=not_sampled_tiers&fullpath=1&lang=en_US&ll=-0.12767300000000148,51.50327850016298&origin=maps-search-form&outformat=json&part={address_for_yandex}&pos=14&spn=0.0009140232783693136,0.0012886280394397431&v=9&yu=172889561681405494')

    data = r.json()

    grid = str(data['results'][0]['pos']).split(',')
    
    lon, lat = grid[0], grid[1]
    
    return lat,lon
