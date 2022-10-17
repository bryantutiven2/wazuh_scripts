
from elasticsearch import Elasticsearch
import json

def connectElastic():
    try:
        client = Elasticsearch(
            'https://admin:oGOUni3qvZT5zUNVX2Tl19pQbcaGA8s7@192.168.255.3:9200',
            verify_certs=False
            )

        
        info = client.info()
        print(info)

        print("\nQuery")
        query_body = {
            "from" : 0, "size" : 10,
            "query": {
                "bool":{
                    "must":[
                        {
                            "match": {
                                "agent.name": "AD-Skytechnosa"
                            },
                        },
                        {
                        "bool": {
                                "should": [
                                    {"term": {"rule.id": 60137}},
                                    # {"term": {"rule.id": "18125"}},
                                    # {"term": {"rule.id": "18156"}},
                                    # {"term": {"rule.id": "18157"}}
                                ]
                            }
                        }
                    ],
                    "filter": [
                        {
                            "range": {
                                "timestamp": {
                                    "gte": "2022-09-10T16:20:31", 
                                    "lte": "2022-10-13T16:20:31"
                                }
                            }           
                        }
                    ],
                },
            }
        }
        resp = client.search(index="wazuh-alerts-4.x-2022.10.13", body=query_body)

        print(json.dumps(resp, indent=4))
        # indexes = client.indices.get('*')
        # print(json.dumps(indexes, indent=4))
        print("Connection to ES Server successful")
    except:
        print("Unable to connect to server")
        exit(1)

   