from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.template import Context, loader
import json
from django.views.decorators.csrf import ensure_csrf_cookie
import requests

def index(request):
    baseURL = 'https://backend.sigfox.com/api/v2/'
    data = '739A8C'
    messageURL = baseURL + 'devices/' + data + '/messages'
    user = '5c500fe6e833d917afc9ccb4'
    password = '5db0745e784d738e0690490aa21c2da6'
    headers = {'content-type' : 'application/json'}
    r = requests.get(messageURL, auth=(user, password), headers=headers)
    if r.status_code == 200:
        data = r.json()
        app_data = data['data']
    targetData = app_data[-1]
    messageData = targetData['data']
    values = []
    for i in range(1,18,4):
        target = messageData[i:(i+3)]
        value = int(target, 16)
        values.append(value)
    print(values)
    return render(request, 'mapping/index.html', {'data' : values})

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
        app_data = data['data']
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
        return render(request, 'mapping/message.html', {'list' : app_data})
    return HttpResponse('Sorry U Failed')

