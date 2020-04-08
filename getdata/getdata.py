import requests
import json
import pymysql
# sql = """
# create table details(
#     id int(11) not null auto_increment,
#     update_time datetime default null comment '数据最后更新时间',
#     province varchar(50) default null comment '省',
#     city varchar(50) default null comment '市',
#     confirm int(11) default null comment '累计确诊',
#     confirm_now int(11) default null comment '现有确诊',
#     confirm_add int(11) default null comment '新增确诊',
#     heal int(11) default null comment '累计治愈',
#     dead int(11) default null comment '累计死亡',
#     primary key(id)
#     )
# """

db = pymysql.connect(
    host='localhost',
    user='root',
    passwd='123456',
    db='yqdata',
    charset='utf8'
)
cursor = db.cursor()

def insert(table,values):
    sql = 'REPLACE INTO {} VALUES{}'.format(table,values)
    try:
        cursor.execute(sql)
        db.commit()
        print('数据插入/更新成功！')
    except:
        db.rollback()
        print('数据插入/更新失败！')

def showtalbe(table):
    cursor.execute('select * from {}'.format(table))
    print(cursor.fetchall())


headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery34106712238835589039_1585985046154&_=1585985046155'
res = requests.get(url, headers=headers)
res_data = json.loads(res.text.replace('jQuery34106712238835589039_1585985046154(','')[:-1])#去掉多余字符串以及结尾括号
response_data = json.loads(res_data['data'])

total = response_data['chinaTotal']
add = response_data['chinaAdd']
total_list = [0]+[total[k] for k in total if k not in ("suspect","nowSevere")]
add_list = [1]+[add[k] for k in add if k not in ("suspect","nowSevere")]

insert('total_add',tuple(total_list))
insert('total_add',tuple(add_list))

time = response_data['lastUpdateTime']
prov_datas = response_data['areaTree'][0]['children']
id = 0
count = 0
for prov_data in prov_datas:
    prov_name = prov_data['name']#省名
    confirm_add = prov_data['today']['confirm']#新增
    confirm_now = prov_data['total']['nowConfirm']#现有确诊
    confirm = prov_data['total']['confirm']#累计确诊
    dead = prov_data['total']['dead']#死亡人数
    heal = prov_data['total']['heal']#治愈人数
    count += 1
    insert('province', (count, prov_name, confirm, confirm_now, confirm_add, heal, dead, time))
    for city_data in prov_data['children']:#从省数据中获取城市列表遍历
        city_name = city_data['name']#城市名
        confirm_add = city_data['today']['confirm']#新增
        confirm_now = city_data['total']['nowConfirm']#现有确诊
        confirm = city_data['total']['confirm']#累计确诊
        dead = city_data['total']['dead']#死亡人数
        heal = city_data['total']['heal']#治愈人数
        id += 1
        insert('details',(id,prov_name,city_name,confirm,confirm_now,confirm_add,heal,dead,time))



showtalbe('total_add')
showtalbe('province')
showtalbe('details')

db.close()
