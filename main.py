import wazuhServer
import json

eventsType = [
    {
        "name": "Security",
        "types": [
            {
                "name": "Login Success",
                "case": "Brute Force",
                "sources": [
                    {
                        "name": "Windows",
                        "ids" : [60122]
                    }
                ]
            }
        ]
    }
]


def main():
    f = open('db.json')
    data = json.load(f)
    for log in data['logs']:
        user = log['_source']['data']['win']['eventdata']['targetUserName']
        

main()