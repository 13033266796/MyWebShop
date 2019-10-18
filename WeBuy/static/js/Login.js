$(function () {
    $('.btn_login').click(function () {
        var nickName = $('#nickName').val();
        var Pwd = $('#Pwd').val();
        //校验
        if(nickName==''){
            alert('用户名不能为空！');
            return;
        }
        if(Pwd==''){
            alert('密码不能为空！');
            return;
        }

        //发送登录请求
        $.ajax({
            url:'/LoginPost/',
            data:{
                nickName:nickName,
                Pwd:Pwd,
                csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val(),
            },
            type:'post',
            dataType:'text',
            success:function (msg) {
                if(msg=='0'){
                    alert('此用户不存在！')
                    return;
                }
                if(msg=='1'){
                    alert('密码错误，请重试。');
                    return;
                }
                else{
                    alert('登录成功！');
                    window.location = msg
                }
            },
            error:function (msg) {
                alert('出错了')
            },
        });
    });
});