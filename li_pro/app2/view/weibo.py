from django.views.generic import View
from django.http import HttpResponse
import pymongo

client = pymongo.MongoClient(host='mongodb://123.206.31.62', port=27017)
db = client.weibo
table = db['joke']


class SearchInfo(View):

    def get(self, request):
        type = int(request.GET.get('type', 1))
        page = int(request.GET.get('page', 0))
        data = table.find({"type": {"$in": [type]}}).sort('-create_time').limit(10).skip(page*10)
        result = {
            'data': list(data)
        }
        return HttpResponse(content=result)


class Login(View):

    def post(self, request):
        user_name = request.POST.get('user', '')
        password = request.POST.get('password', '')
        if user_name == '111' and password == '111':
            return
        else:
            return