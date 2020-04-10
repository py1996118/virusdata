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
    var value = $("option:selected").val();
    $.ajax({
        url:'/province_api',
        timeout:10000,
        success:function (data) {
            if(value==='累计确诊'){
                option_map.series[0].data=data.data1;
                china_map.setOption(option_map);
            }
            else {
                option_map.series[0].data=data.data2;
                china_map.setOption(option_map);
            }
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
            option_pie.series[0].data=data.data.slice(0,10);
            option_pie.legend.data = data.data.name;
            pie.setOption(option_pie);
        },
        error:function () {
        }
    })
}
get_pie_data();

function get_bar_first() {
    $.ajax({
        url : '/bar_api',
        type : 'POST',
        data:{ pro:'湖北' },
        success:function (data) {
            console.log(data);
            city = data.data1;
            con = data.data2;
            option_bar.xAxis.data = city;
            option_bar.series[0].data = con;
            bar.setOption(option_bar);
        }

    })
}
get_bar_first();


function get_option() {
    $.ajax({
        url:'/province_api',
        type:'GET',
        success:function (data) {
            provs = data.datap;
            for(var i=0; i<provs.length; i++) {
                var optionString = "";
                optionString += "<option>" + provs[i] + "</option>";
                $("#select2").append(optionString);
                }
            }
    })
}
get_option();

function get_bar_data() {
    var value = $("#select2").val();
    $.ajax({
        url : '/bar_api',
        type : 'POST',
        data:{ pro:value },
        success:function (data) {
            console.log(data);
            city = data.data1;
            con = data.data2;
            option_bar.xAxis.data = city;
            option_bar.series[0].data = con;
            bar.setOption(option_bar);
        }

    })
}