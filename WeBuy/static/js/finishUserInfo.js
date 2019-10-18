$(function () {
    $('#btn').click(function () {
        var nickName = $('#nickName').text();
        var realName = $('#realName').val();
        var gender = $('[name="RadioGroup1"]:checked').val();
        var number = $('#number').val();
        var mail = $('#mail').val();

        //校验
        if(realName==''){
            alert('真实姓名不能为空')
        }
        if(gender==''){
            alert('性别不能为空')
        }
        if(mail==''){
            alert('邮箱不能为空')
        }

        //异步发送数据
        $.ajax({
            url:'/user_infoPost/',
            data:{
                nickName:nickName,
                realName:realName,
                gender:gender,
                number:number,
                mail:mail,
                csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val(),
            },
            type:'post',
            dataType:'text',
            success:function (msg) {
                if(msg=='1'){
                    alert('认证成功')
                }
            },
            error:function (msg) {
                alert('出错了')
            }
        });
    });


    $('#userHead').click(function () {
        $('#uploadHead').click()
    });

    $('#uploadHead').change(function () {
        $('#comfirm').click();
    });


    var img = '/static/media/'+$('#nickname').text()+'.jpg'
    $.ajax({
        url:'/checkHead/',
        data:{
            img:img
        },
        type:'get',
        dataType:'text',
        success:function (msg) {
            if(msg=='1'){
                $('#Head').attr('src','/static/media/'+$('#nickname').text()+'.jpg')
            }

        }

    })
});
