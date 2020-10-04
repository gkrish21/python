import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"name":"Gopal", "views":10000, "likes": 440},
#         {"name":"Tim", "views":2000, "likes": 55},
#         {"name":"How to make Rest Api", "views":80000, "likes": 550}]

# for i in range(len(data)):
#     response = requests.put(BASE + 'video/'+str(i), data[i])
#     print(response.json())

# input()
# response = requests.get(BASE + 'video/20')
# print(response.json())

response = requests.patch(BASE + 'video/2', {'likes': 101})
print(response.json())

