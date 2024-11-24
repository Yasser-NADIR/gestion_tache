import requests
from requests.auth import HTTPBasicAuth

url = 'https://10.253.55.155'
path = '/policy/api/v1/infra/lb-virtual-servers'
username = 'admin'
password = 'Ecocenter777*'


response = requests.get(url+path, auth=HTTPBasicAuth(username, password), verify=False)

if response.status_code == 200:
    json_data = response.json()
    print("Response JSON:")
    for result in json_data['results']:
        if result['display_name'].find('VIP') != -1:
            print(f'name: {result['display_name']}, ports: {[port for port in result['ports'] if int(port)>=50000]}')
    
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print("Response:", response.text)


# import aiohttp
# import asyncio

# url = 'https://10.253.55.155'
# path = '/policy/api/v1/infra/lb-virtual-servers'
# username = 'admin'
# password = 'Ecocenter777*'

# async def fetch_data(url, username, password):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, auth=aiohttp.BasicAuth(username, password), ssl=False) as response:
#             if response.status == 200:
#                 json_data = await response.json()
#                 print("Response JSON:")
#                 for result in json_data['results']:
#                     print(f'name: {result['display_name']}, ports: {result['ports']}')
#             else:
#                 print(f"Failed to retrieve data: {response.status}")
#                 print("Response:", await response.text())

# asyncio.run(fetch_data(url+path, username, password))