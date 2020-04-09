from yqshows.models import Details, TotalAdd, Province
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from pyecharts.charts import Map, Geo, Pie, Page, Bar
from pyecharts.globals import ThemeType#主题
from pyecharts import options as opts


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
    data = []
    if p_data:
        for i in p_data:
            datas = {}
            datas['name'] = i.province
            datas['value'] = i.confirm
            data.append(datas)
        # 就data存入context
        context.update({'data': data})
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
            datas['province'] = i.province
            datas['city'] = i.city
            datas['confirm'] = i.confirm
            datas['confirm_add'] = i.confirm_add
            datas['confirm_now'] = i.confirm_now
            datas['heal'] = i.heal
            datas['dead'] = i.dead
            datas['time'] = i.tme
            data.append(datas)
        #就data存入context
        context.update({'data': data})
        return JsonResponse(context, json_dumps_params={'ensure_ascii' : False})
    else:
        return JsonResponse({'status': 10022, 'message': 'query isempty'})


def pie_api(req):
    pr_data = Province.objects.all().order_by('-confirm_now')[:10]
    data = []
    for i in pr_data:
        datas = {}
        datas['name'] = i.province
        datas['value'] = i.confirm_now
        data.append(datas)
    context = {'data':data}
    return JsonResponse(context, json_dumps_params={'ensure_ascii' : False})


def map_api(req):
    HttpResponse('hello')
