import elastic

def main():

    data = {}

    resp = elastic.connectElastic()
    logs = resp["hits"]["hits"]
    print(len(logs))
    for log in logs:
        event = log["_source"]["data"]["win"]["eventdata"]
        target_user = event["targetUserName"]
        ruleId = int(log["_source"]["rule"]["id"])
        if target_user not in data.keys():
            data[target_user] = {}
            if ruleId == 60122:
                data[target_user]["failure"]=1
            elif ruleId == 60106:
                data[target_user]["sucsess"]=1
        else:
            if ruleId == 60122:
                data[target_user]["failure"] +=1
            elif ruleId == 60106:
                data[target_user]["sucsess"] +=1
    print(data)

main()