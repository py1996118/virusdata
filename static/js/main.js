$(document).ready(function(){
    $.ajax({
        url: "/total_api",
        type: "GET",
        data: '',
        success: function (response) {
            total = response.data[0];
            add = response.data[1];
            $(".icbar_Confirm .number").text(total.confirm);
            $(".icbar_Confirm .add .number").text(add.confirm);
            $(".icbar_nowConfirm .number").text(total.nowconfirm);
            $(".icbar_nowConfirm .add .number").text(add.nowconfirm);
            $(".icbar_heal .number").text(total.heal);
            $(".icbar_heal .add .number").text(add.heal);
            $(".icbar_dead .number").text(total.dead);
            $(".icbar_dead .add .number").text(add.dead);
            $(".icbar_import .number").text(total.importcase);
            $(".icbar_import .add .number").text(add.importcase);
            $(".icbar_nowSevere .number").text(total.noinfect);
            $(".icbar_nowSevere .add .number").text(add.noinfect);
            },
     });
});


function get_list() {
    $.ajax({
        url: "/detials_api",
        type: "GET",
        data: "",
        success: function (response) {
            provin = response.data;
            var html = '';
            for (i = 0; i < 10; i++) {
                for (key in provin[i]) {
                    html += "<li>" + key + ':' + provin[i][key] + "</li>";
                }
            }
            $(".list").html(html)
        },
    });
}
get_list();


function get_map_data() {
    $.ajax({
        url:'/province_api',
        timeout:10000,
        success:function (data) {
            option_map.series[0].data=data.data;
            china_map.setOption(option_map);
        },
        error:function () {
        }
    })
}
get_map_data();


function get_pie_data() {
    $.ajax({
        url:'/pie_api',
        timeout:10000,
        success:function (data) {
            console.log(data);
            option_pie.series[0].data=data.data;
            option_pie.legend.data = data.data.name;
            pie.setOption(option_pie);
        },
        error:function () {
        }
    })
}
get_pie_data();