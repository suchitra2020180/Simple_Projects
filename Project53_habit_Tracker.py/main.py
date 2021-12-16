#https://pixe.la/
import requests
USER_NAME= "suchitra2021"
TOKEN="dhtac5yts47djhgs"
ID ="test-graph"
pixela_endpoint="https://pixe.la/v1/users"

# step1:Creating user
user_paramas={"token": TOKEN,
                "username":USER_NAME,
                "agreeTermsOfService": "yes",
                "notMinor": "yes"}
# response = requests.post(url=pixela_endpoint, json=user_paramas)
# print(response.text)

# Once the user is created the response will give alreaddy exists. So comment the step
# step2: Creating graph definition
# format:  https://pixe.la/v1/users/a-know/graphs/test-graph
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config={"id":ID,
                "name":"Coding Time",
                "unit":"minutes",
                "type":"float",
                "color":"ajisai"
}
GRAPH_header={"X-USER-TOKEN":TOKEN}

# graph_response =requests.post(url=graph_endpoint, json=graph_config, headers=GRAPH_header)
# print(graph_response.text)

# https://pixe.la/v1/users/suchitra2021/graphs/test-graph
#https://pixe.la/v1/users/suchitra2021/graphs/test-graph.html

# step3: Posting a value(pixel) to the graph==> pixel creation
import datetime as dt
today=dt.datetime.now().date()
print(today)
#Yesterday record not updated then
#today=dt.datetime(year=2021, month=12, day=9)
#TODAY DATE
DATE=today.strftime("%Y%m%d")
print(DATE)
entry_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{ID}"
pixel_params={"date":DATE,
        "quantity":"60"}

entry_response= requests.post(url=entry_endpoint, json=pixel_params, headers=GRAPH_header)
print(entry_response.text)

# We can update and delete the pixels too
#PUT - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{ID}/{DATE}"
update_param = {"quantity": "100"}
# update_response = requests.put(url=update_endpoint, json=update_param, headers=GRAPH_header)
# print(update_response.text)

##Delete a pixel
##DELETE - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
del_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{ID}/{DATE}"
# del_response=requests.delete(url=del_endpoint, headers=GRAPH_header)
# print(del_response.text)