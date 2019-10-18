$(function () {
//1.列表页加入购物车  数量为 1
    $('.btn_style .Join_btn').click(function () {
        var product = $(this).parent().prev().prev().prev().text();
        var nickName = $('#islogin_1').text();

        if ($('#islogin_1').text()=='登录'){
            alert('请先登录！');
            return;
        }
        $.ajax({
            url:'/addToCart/',
            data:{
                product:product,
                nickName:nickName,
            },
            type:'get',
            dataType:'text',
            success:function (msg) {
                if (msg=='1'){
                    alert('添加成功')
                }
            },
            error:function (msg) {
                alert('n')
            },
        });
        $.get('/head_getCartsNumber/',function (data) {

              $('#user_cart').text('购物车（'+data.number+'）')
        });
    });

//2.商品详情页加入购物车 数量可由用户输入 默认为1
    $('.operating .Join_btn').click(function () {
        var product = $(this).parent().prev().prev().prev().prev().find('h2').text();
        var nickName = $('#islogin_1').text();
        var number = $('.number_text').val();
        if ($('#islogin_1').text()=='登录'){
            alert('请先登录！');
            return;
        }
        $.ajax({
            url:'/addToCart/',
            data:{
                product:product,
                nickName:nickName,
                number:number
            },
            type:'get',
            dataType:'text',
            success:function (msg) {
                if (msg=='1'){
                    alert('添加成功')
                }
            },
        });

        $.get('/head_getCartsNumber/',function (data) {
              $('#user_cart').text('购物车（'+data.number+'）')
        });
    });

//3.列表页点击 立即购买 将商品加入购物车 并跳转到购物车
    $('.btn_style .buy_btn').click(function () {
        var product = $(this).parent().prev().prev().prev().text();
        var nickName = $('#islogin_1').text();

        if ($('#islogin_1').text()=='登录'){
            alert('请先登录！');
            return;
        }
        $.ajax({
            url:'/addToCart/',
            data:{
                product:product,
                nickName:nickName,
            },
            type:'get',
            dataType:'text',
            success:function (msg) {
                if (msg=='1'){
                    // alert('添加成功')
                }
            },
            error:function (msg) {
                alert('n')
            },
        });
        $.get('/head_getCartsNumber/',function (data) {

              $('#user_cart').text('购物车（'+data.number+'）')
        });
    });

//4.商品详情页点击 立即购买 将商品加入购物车 并跳转到购物车
    $('.operating .buy_btn').click(function () {
        var product = $(this).parent().prev().prev().prev().prev().find('h2').text();
        var nickName = $('#islogin_1').text();
        var number = $('.number_text').val();
        if ($('#islogin_1').text()=='登录'){
            alert('请先登录！');
            return;
        }
        $.ajax({
            url:'/addToCart/',
            data:{
                product:product,
                nickName:nickName,
                number:number
            },
            type:'get',
            dataType:'text',
            success:function (msg) {
                if (msg=='1'){
                    // alert('添加成功')
                }
            },
        });

        $.get('/head_getCartsNumber/',function (data) {
              $('#user_cart').text('购物车（'+data.number+'）')
        });
    });

});



