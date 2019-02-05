from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.template import Context, loader
import json
from django.views.decorators.csrf import ensure_csrf_cookie
import requests

def index(request):
    # template = loader.get_template("mapping/index.html")
    # return HttpResponse(template.render())
    return render(request, 'mapping/index.html')

def sigfox(request):
    baseURL = 'https://backend.sigfox.com/api/v2/'
    data = '739A8C'
    messageURL = baseURL + 'devices/' + data + '/messages'
    user = '5c500fe6e833d917afc9ccb4'
    password = '5db0745e784d738e0690490aa21c2da6'
    headers = {'content-type' : 'application/json'}
    r = requests.get(messageURL, auth=(user, password), headers=headers)
    if r.status_code == 200:
        data = r.json()
        app_data = data['data'][0]
        # time = data['data'][0]
        # app_data = {}

        # for i in data :
        #     message_data = {
        #         'id' : data[i]['device'],
        #         'time' : data[i]['time'],
        #         'data' : data[i]['data'],
        #     }
        #     app_data.update(message_data)
        # return HttpResponse(data, content_type='application/javascript; charset=UTF-8', status=None)
        return render(request, 'mapping/message.html', app_data)
    return HttpResponse('Sorry U Failed')



# # Create your views here.
# conn = MySQLdb.connect(host = '',
#     user = 'root',
#     passwd = 'root',
#     db = 'myDB'   
# )

# cursor.execute('select <column> from <table>')
# rows = dictfetchall(cursor)


# conn.close()

# def dictfetchall(cursor):
#     "Return all rows from a cursor as a dictionary"
#     desc = cursor.description
#     return [
#         dict(zip([col[0] for col in desc], row))
#         for row in cursor.fetchall()
#     ]
