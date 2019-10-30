from django.shortcuts import render, render_to_response
import pip
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

plt.style.use('ggplot')
plt.ion()
df = pd.read_csv('kkkk.csv', delimiter=',',
                     usecols=['ID', 'Device ID', 'RMS_V', 'RMS_V1', 'RMS_V2', 'RMS_V3', 'RMS_A', 'RMS_A1', 'RMS_A2',
                              'RMS_A3',
                              'RMS_PF', 'RMS_PF1', 'RMS_PF2', 'RMS_PF3', 'RMS_W', 'RMS_W1', 'RMS_W2', 'RMS_W3',
                              'RMS_F', 'RMS_KWH', 'RMS_VLL', 'RMS_VAB', 'RMS_VBC', 'RMS_VCA', 'RMS_AW', 'RMS_AW1',
                              'RMS_AW2', 'RMS_AW3', 'TIME_STAMP'])

@csrf_exempt



def app_pow():
    df['app_pow']= df['RMS_V'] * df['RMS_A']
    app_pow= df['app_pow']
    return app_pow



def tr_pow():
    df['app_pow'] = df['RMS_V'] * df['RMS_A']
    df['tr_pow']=df['RMS_PF'] * df['app_pow']
    tr_pow= df['tr_pow']
    return tr_pow





#def show():
   # df['APP_POW'] = df.apply(calculate_app, axis=1)
    #tr_pow = "TRUE POWER" + df['TR_POW']
    #eturn tr_pow



def graph1():
  plt.rcParams["figure.figsize"]=(5,5)
  plt.rcParams["keymap.quit"] = "ctrl+w",  "q"
  plt.plot(df[0:10]['TIME_STAMP'],df[0:10]['RMS_V'])
  plt.ylabel('voltage')
  plt.title('T-V GRAPH')
  plt.legend('Hello')
  plt.show()

def last1():
      df['APP_POW'] = df['RMS_V'] * df['RMS_A']
      df['TR_POW'] = df['RMS_PF'] * df['APP_POW']
      cnt = df.shape[0]
      N = cnt - 25;
      res = df['TR_POW'][N:]
      res = [num for num in res if num != 0]
      TR_sum = 0
      for i in range(15):
          TR_sum = TR_sum + res[i]
          avg = TR_sum / 15
      print(avg)
      res.reverse()
      last1 = str(res[0])
      return last1


def travg():
    df['APP_POW'] = df['RMS_V'] * df['RMS_A']
    df['TR_POW'] = df['RMS_PF'] * df['APP_POW']
    cnt = df.shape[0]
    N = cnt - 25;
    res = df['TR_POW'][N:]
    res = [num for num in res if num != 0]
    TR_sum = 0
    for i in range(15):
        TR_sum = TR_sum + res[i]
        travg = TR_sum / 15
    return travg



def last2():
    df['APP_POW'] = df['RMS_V'] * df['RMS_A']
    df['TR_POW'] = df['RMS_PF'] * df['APP_POW']
    cntt = df.shape[0]
    Nn = cntt - 25;
    resu = df['APP_POW'][Nn:]
    resu = [num for num in resu if num != 0]
    TR_summ = 0
    for i in range(15):
        TR_summ = TR_summ + resu[i]
        avgg = TR_summ / 15
    print(avgg)
    resu.reverse()
    last2 = str(resu[0])
    return last2

def avgg():
    df['APP_POW'] = df['RMS_V'] * df['RMS_A']
    df['TR_POW'] = df['RMS_PF'] * df['APP_POW']
    cntt = df.shape[0]
    Nn = cntt - 25;
    resu = df['APP_POW'][Nn:]
    resu = [num for num in resu if num != 0]
    TR_summ = 0
    for i in range(15):
        TR_summ = TR_summ + resu[i]
        avgg = TR_summ / 15

    return avgg



def getpage(request):
    if request.method == 'GET':
        return render(request,'kkk.html')

def output(request):
    return render(request, 'kkk.html', {'last1':last1})

def outputa(request):
    return render(request, 'kkk.html', {'avgg':avgg})

def outputtr(request):
    return render(request, 'kkk.html', {'travg':travg})


def output1(request):
    return render(request, 'kkk.html', {'last2':last2})




def modu():
    df['APP_POW'] = df['RMS_V'] * df['RMS_A']
    df['TR_POW'] = df['RMS_PF'] * df['APP_POW']
    cnt = df.shape[0]
    N = cnt - 25;
    res = df['TR_POW'][N:]
    res = [num for num in res if num != 0]
    TR_sum = 0
    for i in range(15):
        TR_sum = TR_sum + res[i]
        avg = TR_sum / 15
    print(avg)
    res.reverse()
    last = str(res[0])
    print(last)
    a = 0.15 * float(last)
    print(a)
    b = float(last) + float(a)
    c = float(last) - float(a)
    print(b)
    print(c)
    if ((avg >= b) | (avg <= c)):
        #print("Value has been varied")
        modu= "Value has been varied"
    else:

        modu="value has not been modified as there is no rise in current power"

    return modu

def amodu():
    df['APP_POW'] = df['RMS_V'] * df['RMS_A']
    df['TR_POW'] = df['RMS_PF'] * df['APP_POW']
    cntt = df.shape[0]
    Nn = cntt - 25;
    resu = df['APP_POW'][Nn:]
    resu = [num for num in resu if num != 0]
    ap_sum = 0
    for i in range(15):
        ap_sum = ap_sum + resu[i]
        avg = ap_sum / 15
    print(avg)
    resu.reverse()
    last = str(resu[0])
    print(last)
    a = 0.15 * float(last)
    print(a)
    b = float(last) + float(a)
    c = float(last) - float(a)
    print(b)
    print(c)
    if ((avg >= b) | (avg <= c)):
        #print("Value has been varied")
        amodu= "Value has been varied"
    else:
        amodu= "value has not been modified as there is no rise in current power"

    return amodu

def outputv(request):
    return render(request, 'kkk.html', {'amodu':amodu})




def output2(request):
    return render(request, 'kkk.html', {'modu':modu})







