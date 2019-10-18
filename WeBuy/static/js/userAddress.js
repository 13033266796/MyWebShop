$(function () {
    //打开收货地址页面获取地址


    //获取省信息
    $.get('/pro/',function (list) {
        pro = $('#pro');
        //[410000,'河南']
        $.each(list.data,function (index,item) {
            pro.append('<option value="'+item[0]+'">'+item[1]+'</option>')
        })

    });
    //获取市信息
    $('#pro').change(function () {
        $('#city').empty().append('<option value="">请选择市</option>');
        $('#dis').empty().append('<option value="">请选择区/县</option>');
        $.get('/cityAndDis'+$(this).val()+'/',function (list) {
            city =$('#city');
            $.each(list.data,function (index, item) {
                city.append('<option value="'+item.id+'">'+item.name+'</option>')
            });
        });
    });
    //获取区、县信息
    $('#city').change(function () {
        $('#dis').empty().append('<option value="">请选择区/县</option>');
        $.get('/cityAndDis'+$(this).val()+'/',function (list) {
            dis = $('#dis');
            $.each(list.data,function (index, item) {
                dis.append('<option value="'+item.id+'">'+item.name+'</option>')
            })
        })
    });

    $('#address_btn').click(function () {
        var realName = $('#realName').val();
        var pro = $("#pro").find("option:selected").text();
        var city = $("#city").find("option:selected").text();
        var dis = $("#dis").find("option:selected").text();
        var detail_address = $('#detail_address').val();
        var youbian = $('#youbian').val();
        var number = $('#number').val();
        var telephone = $('#telephone').val();

        //校验
        if (realName=='')
            alert('真实姓名不能为空');
        if (pro=='')
            alert('省信息不能为空');
        if (city=='')
            alert('市信息不能为空');
        if (dis=='')
            alert('区、县信息不能为空');
        if (detail_address=='')
            alert('详细地址不能为空不能为空');
        if (number=='')
            alert('手机号不能为空');

        //发送数据
        $.ajax({
           url:'/addressPost/',
           data:{
               realName:realName,
               pro:pro,
               city:city,
               dis:dis,
               detail_address:detail_address,
               youbian:youbian,
               number:number,
               telephone:telephone,
               csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val(),
           },
           type:'post',
           dataType:'text',
           success:function (msg) {
               alert('成功')
           } ,
           error:function (msg) {
               alert('错误')
           } ,

        });

    });



});