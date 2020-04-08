$(document).ready(function(){
    $.ajax({
        url:"/detials_api",
        type:"GET",
        data:"",
        success:function(response){
            provin = response.data;
            var html='';
            html+="<h1>"+'数据列表'+"</h1>";
            for(i=0;i<10;i++){
                for (key in provin[i]){
                    html+="<li>"+key+':'+provin[i][key]+ "</li>";
                }
            }
            $(".list").html(html)
        },
    });
});