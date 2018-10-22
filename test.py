import requests

# url_get_token = "https://api.weibo.com/oauth2/access_token"
#
# #构建POST参数
# playload = {
#             "client_id":"789316945",
#             "client_secret":"9a165120352192161037a961f63907f2",
#             "grant_type":"authorization_code",
#             "code":"1bf88b48bd7168e1bedb5e816545480b",
#             "redirect_uri":"http://123.206.31.62:8888"
#              }
# #POST请求
# r = requests.post(url_get_token, data=playload)
#
# #输出响应信息
# print(r.text)

url_post_a_text = "https://api.weibo.com/2/statuses/update.json"

#构建POST参数
playload = {
        "access_token": "2.00lsL13H0T5t6r0d74ba67e5ennhLB",
        "status": "This is a text test"
        }
#POST请求，发表文字微博
r = requests.post(url_post_a_text,data = playload)

print(r)