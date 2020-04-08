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
            datas['province'] = i.province
            datas['confirm'] = i.confirm
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
    datas = Province.objects.all()
    data = []
    for i in datas:
        data.append([i.province, i.confirm_now])
    sorted(data,key=lambda data:data[0][1])
    pie = Pie(init_opts=opts.InitOpts(width='auto', height='600px', ))
    pie.add("现有确诊", data[:10], radius=[20, 100], rosetype='radius')
    return HttpResponse(pie.render_embed())


def map_api(req):
    datas = Province.objects.all()
    data = []
    for i in datas:
        data.append([i.province, i.confirm_now])
    # maptype='china' 只显示全国直辖市和省级
    # 数据只能是省名和直辖市的名称
    map = Map(init_opts=opts.InitOpts(width='auto',height='600px',bg_color="grey", theme=ThemeType.DARK))
    map.add("现有确诊", data, 'china', is_map_symbol_show=False)
    map.set_global_opts(
        # 标题配置项，pos_left可取值center、left、right、5%等等
        title_opts=opts.TitleOpts(title="全国疫情确诊人数分布图", pos_left="left"),
        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True,  # 设置是否为分段显示
            # 自定义的每一段的范围，以及每一段的文字，以及每一段的特别的样式。例如：
            pieces=[
                {"min": 1000, "label": '>1000人', "color": "#FF3030"},  # 不指定 max，表示 max 为无限大（Infinity）。
                {"min": 500, "max": 1000, "label": '500-1000人', "color": "#FF4500"},
                {"min": 100, "max": 499, "label": '100-499人', "color": "#FF7F50"},
                {"min": 10, "max": 99, "label": '10-99人', "color": "#FFA500"},
                {"min": 1, "max": 9, "label": '1-9人', "color": "#FFDEAD"},
            ]))
    return HttpResponse(map.render_embed())

