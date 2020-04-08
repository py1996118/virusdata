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