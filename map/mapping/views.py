from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.template import Context, loader
import json
from django.views.decorators.csrf import ensure_csrf_cookie
import requests
import math

def index(request):
    baseURL = 'https://backend.sigfox.com/api/v2/' # base url
    data = '739A8C' # Sigfox Unashield ID
    messageURL = baseURL + 'devices/' + data + '/messages'
    user = '5c500fe6e833d917afc9ccb4' # sigfox user ID
    password = '5db0745e784d738e0690490aa21c2da6' # sigfox password
    headers = {'content-type' : 'application/json'} # データをJSONで取得するための設定
    r = requests.get(messageURL, auth=(user, password), headers=headers)
    values = [] #センサ値配列の初期化
    if r.status_code == 200: # 取得成功時
        data = r.json()
        app_data = data['data']
    count = 0
    for targetData in app_data:
        messageData = targetData['data']
        count = count+1
        if count > 2:
            break
        for i in range(1,18,4):
            target = messageData[i:(i+3)]
            value = int(target, 16)
            value = culcMC(value)
            values.append(value)
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
        return render(request, 'mapping/message.html', {'list' : app_data})
    return HttpResponse('Sorry U Failed')

def culcMC(x): #含水比の計算
    exp = math.e
    ans = x + (6.54 * 1000)
    ans = ans / (2.28 * 1000)
    ans = ans * ans
    ans = pow(exp, (ans * (-1)))
    ans = 3.59 * 100000 * ans
    return round(ans,1)