import json
import requests
import urllib3
from base64 import b64encode

def conectWazuh():

    # Disable insecure https warnings (for self-signed SSL certificates)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Configuration
    protocol = 'https'
    host = '192.168.255.5'
    port = 55000
    user = 'wazuh-wui'
    password = '5Kyt3chNOS4*2022$$'
    login_endpoint = 'security/user/authenticate'

    login_url = f"{protocol}://{host}:{port}/{login_endpoint}"
    basic_auth = f"{user}:{password}".encode()
    login_headers = {'Content-Type': 'application/json',
                    'Authorization': f'Basic {b64encode(basic_auth).decode()}'}

    print("\nLogin request ...\n")
    response = requests.get(login_url, headers=login_headers, verify=False)
    token = json.loads(response.content.decode())['data']['token']
    print(token)

    # New authorization header with the JWT token we got
    requests_headers = {'Content-Type': 'application/json',
                        'Authorization': f'Bearer {token}'}

    print("\n- API calls with TOKEN environment variable ...\n")

    print("Getting API information:")

    response = requests.get(f"{protocol}://{host}:{port}/?pretty=true", headers=requests_headers, verify=False)
    print(response.text)

    print("\nGetting groups")

    response = requests.get(f"{protocol}://{host}:{port}/groups", headers=requests_headers, verify=False)
    print(json.dumps(response.json(), indent=4))

    print("\nGetting agents status summary:")

    response = requests.get(f"{protocol}://{host}:{port}/agents/summary/status?pretty=true", headers=requests_headers, verify=False)
    print(response.text)

    print("\nAgents to group default")
    response = requests.get(f"{protocol}://{host}:{port}/agents?group=default", headers=requests_headers, verify=False)
    print(json.dumps(response.json(), indent=4))
    
    # print("\nAgents active:")
    # response = requests.get(f"{protocol}://{host}:{port}/agents?status=active", headers=requests_headers, verify=False)
    # print(json.dumps(response.json(), indent=4))

    print("\nEnd of the script.\n")