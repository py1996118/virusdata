from django.views.decorators.csrf import csrf_exempt

from yqshows.models import Details, TotalAdd, Province
from django.http import JsonResponse
from django.shortcuts import HttpResponse


def TotalAdd_api(req):
    context = {'status': 200}
    ta_data = TotalAdd.objects.all()
    #数据为空返回错误
    if ta_data == None:
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    data = []
    if ta_data:
        for i in ta_data:
            datas = {}
            datas['confirm'] = i.confirm
            datas['nowconfirm'] = i.nowconfirm
            datas['importcase'] = i.importcase
            datas['noinfect'] = i.noinfect
            datas['heal'] = i.heal
            datas['dead'] = i.dead
            data.append(datas)
        # 就data存入context
        context.update({'data': data})
        return JsonResponse(context)
    else:
        return JsonResponse({'status': 10022, 'message': 'query isempty'})


def Province_api(req):
    context = {'status': 200}
    p_data = Province.objects.all()
    #数据为空返回错误
    if p_data == None:
        return JsonResponse({'status': 10021, 'message': 'parameter error'})
    data1 = []
    data2 = []
    datap = []
    if p_data:
        for i in p_data:
            data3 = {}
            data4 = {}
            data3['name'] = i.province
            data4['name'] = i.province
            data3['value'] = i.confirm
            data4['value'] = i.confirm_now
            data1.append(data3)
            data2.append(data4)
            datap.append(i.province)
        # 就data存入context
        context.update({'data1': data1})
        context.update({'data2': data2})
        context.update({'datap': datap})
        return JsonResponse(context, json_dumps_params={'ensure_ascii' : False})
    else:
        return JsonResponse({'status': 10022, 'message': 'query isempty'})


def Details_api(req):
    context = {'status': 200,'msg': 'success'}
    details_data = Details.objects.all()
    #数据为空返回错误
    if details_data == None:
        return JsonResponse({'status': 10021, 'message': 'parameter error'})
    data = []
    if details_data:
        for i in details_data:
            datas = {}
            datas['省市'] = i.province
            datas['城市'] = i.city
            datas['累计确诊']= i.confirm
            datas['现有确诊']= i.confirm
            datas['新增确诊']= i.confirm_add
            datas['治愈人数']= i.heal
            datas['死亡人数']= i.dead
            datas['更新时间']= i.tme
            data.append(datas)
        #就data存入context
        context.update({'data': data})
        return JsonResponse(context, json_dumps_params={'ensure_ascii' : False})
    else:
        return JsonResponse({'status': 10022, 'message': 'query isempty'})


def pie_api(req):
    pr_data = Province.objects.all().order_by('-confirm_now')
    data = []
    for i in pr_data:
        datas = {}
        datas['name'] = i.province
        datas['value'] = i.confirm_now
        data.append(datas)
    context = {'data':data}
    return JsonResponse(context, json_dumps_params={'ensure_ascii' : False})

@csrf_exempt
def bar_api(request):
    if request.method =='POST':
        pro = request.POST.get('pro')
        citys = Details.objects.filter(province=pro)
        city = []
        confirm = []
        for i in citys:
            city.append(i.city)
            confirm.append(i.confirm)
        context = {'data1':city}
        context.update({'data2': confirm})
        return JsonResponse(context, json_dumps_params={'ensure_ascii' : False})
