var china_map = echarts.init(document.getElementById('map'), 'white', {renderer: 'canvas'});
var option_map = {
    "series": [
        {
            "type": "map",
            "name": "累计确诊",
            "label": {
                "show": true,
                "position": "top",
                "margin": 5
            },
            "mapType": "china",
            "data": [],
            "roam": false,
            "zoom": 1,
            "showLegendSymbol": false,
            "emphasis": {}
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "title": [
        {
            "text": "全国累计确诊人数分布图",
            "left": "center",
            "padding": 5,
            "itemGap": 10
        }
    ],
    "visualMap": {
        "show": true,
        "type": "piecewise",
        "min": 0,
        "max": 100,
        "inRange": {
            "color": [
                "#50a3ba",
                "#eac763",
                "#d94e5d"
            ]
        },
        "calculable": true,
        "inverse": false,
        "splitNumber": 5,
        "orient": "vertical",
        "showLabel": true,
        "itemWidth": 20,
        "itemHeight": 14,
        "borderWidth": 0,
        "pieces": [
            {
                "min": 1000,
                "label": ">1000\u4eba",
                "color": "#FF3030"
            },
            {
                "min": 500,
                "max": 1000,
                "label": "500-1000\u4eba",
                "color": "#FF4500"
            },
            {
                "min": 100,
                "max": 499,
                "label": "100-499\u4eba",
                "color": "#FF7F50"
            },
            {
                "min": 10,
                "max": 99,
                "label": "10-99\u4eba",
                "color": "#FFA500"
            },
            {
                "min": 1,
                "max": 9,
                "label": "1-9\u4eba",
                "color": "#FFDEAD"
            }
        ]
    }
};


var pie = echarts.init(document.getElementById('pie'),'white',{renderer: 'canvas'});
var option_pie = {
    title: {
        text: '现有确诊',
        subtext: '前十',
        left: 'center'
    },
    tooltip: {
        trigger: 'item',
        formatter: '{b} : {c}'
    },
    legend: {
        left: 'center',
        top: 'bottom',
        data: []
    },
    series: [
        {
            name: '',
            type: 'pie',
            radius: [50, 150],
            center: ['50%', '50%'],
            roseType: 'radius',
            label: {
                show: true
            },
            emphasis: {
                label: {
                    show: true
                }
            },
            data: []
        },
    ]
};