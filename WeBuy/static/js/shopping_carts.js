$('.rememberMe').change(function () {
        var sum = 0;
        $('.rememberMe:checked:not(#checkall)').each(function () {
            var num = $(this).parent().next().next().next().find('.number_text').val();
            var price = $(this).parent().next().next().find('.price').text();
            sum = sum+num*price
        });
        $('.cart_price b').text('￥'+sum.toFixed(2));

    });

    //全选 全消
    $('#checkall').click(function () {
        state = $(this).prop('checked');
        $('.rememberMe:not(#checkall)').prop('checked',state)
    });

    $('.rememberMe:not(#checkall)').click(function () {
        if($(this).prop('checked')){
            if($(':checked').length+1 == $(':checkbox').length){
                $('#checkall').prop('checked',true)
            }
        }
        else {
            $('#checkall').prop('checked',false)
        }
    });

    $('.jian').click(function () {
        var sum = 0;
        $('.rememberMe:checked:not(#checkall)').each(function () {
            var num = $(this).parent().next().next().next().find('.number_text').val();
            var price = $(this).parent().next().next().find('.price').text();
            sum = sum+num*price
        });
        $('.cart_price b').text('￥'+sum.toFixed(2))
    });
    $('.jia').click(function () {
        var sum = 0;
        $('.rememberMe:checked:not(#checkall)').each(function () {
            var num = $(this).parent().next().next().next().find('.number_text').val();
            var price = $(this).parent().next().next().find('.price').text();
            sum = sum+num*price
        });
        $('.cart_price b').text('￥'+sum.toFixed(2))
    });
    $('.number_text').blur(function () {
        var sum = 0;
        $('.rememberMe:checked:not(#checkall)').each(function () {
            var num = $(this).parent().next().next().next().find('.number_text').val();
            var price = $(this).parent().next().next().find('.price').text();
            sum = sum+num*price
        });
        $('.cart_price b').text('￥'+sum.toFixed(2));
        $(this).parent().parent().next().text('￥'+(parseFloat($(this).parent().parent().prev().find('.price').text())*parseInt($(this).val())).toFixed(2))
        // $(this).parent().next().text();
        // $(this).parent().prev().find('.price').text();
        // $(this).val();
    });

//单个删除购物车内商品
$('.title_width5 a:not(#allDelete)').click(function () {
    var nickName = $('#islogin_1').text();
    var product = $(this).parent().prev().prev().prev().prev().find('.title_name').text();
    $.get('/deleteGoods/?nickName='+nickName+'&product='+product,function (msg) {
        if(msg=='删除成功'){
            window.location = '/shopping_cart/'
        }
    })
});

//购物车批量删除
$('#allDelete').click(function () {
    var product_list = '';
    //遍历所有勾选商品
    $('.rememberMe:checked:not(#checkall)').each(function () {
        var product = $(this).parent().next().find('.title_name').text();
        product_list = product_list+product+','
    });
    var nickName = $('#islogin_1').text();

    $.ajax({
        url:"/deleteAllGoods/",
        data:{
            nickName:nickName,
            product_list:product_list,
        },
        type:'get',
        dataType:'text',
        success:function (msg) {
            alert('删除成功');
            window.location = '/shopping_cart/'
        },
    })

});