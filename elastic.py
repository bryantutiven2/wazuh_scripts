
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
        # query_body = {
        #     # "from" : 0, "size" : 10,
        #     "query": {
        #         "bool":{    
        #             "must":[
        #                 # {"term": {"agent.name": "CCTVM01"}},
        #                 {
        #                     "match": {
        #                         "agent.name": "CCTVM01"
        #                     },
        #                 },
        #                 {
        #                     "bool": {
        #                             "should": [
        #                                 {"term": {"rule.id": 60122}},
        #                                 {"term": {"rule.id": 60106 }},
        #                             ]
        #                         }
        #                 }
        #             ],
        #             "filter": [
        #                 {
        #                     "range": {
        #                         "timestamp": {
        #                             "gte": "2022-09-21T10:20:31", 
        #                             "lte": "2022-10-21T23:20:31"
        #                         }
        #                     }           
        #                 }
        #             ],
        #         },
        #     }
        # }

        query_body = {
            #  "from" : 0, 
             "size" : 10000,
            
            "query": {
                "bool": {
                    "filter" : {
                        "bool": {    
                            "must":[
                                {"term": {"agent.name": "CCTVM01"}},
                                {
                                    "bool": {
                                            "should": [
                                                {"term": {"rule.id": 60122}},
                                                {"term": {"rule.id": 60106 }},
                                            ]
                                        }
                                }
                            ],
                            "filter": [
                                {
                                    "range": {
                                        "timestamp": {
                                            "gte": "2022-10-21T10:20:31", 
                                            "lte": "2022-10-21T10:25:31"
                                        }
                                    }           
                                }
                            ],
                        },
                    }
                }
            }
        }

        resp = client.search(index="wazuh-alerts-4.x-2022.10.21", body=query_body)

        # print(json.dumps(resp, indent=4))
        print("Connection to ES Server successful")
        return resp
    except:
        print("Unable to connect to server")
        exit(1)

   