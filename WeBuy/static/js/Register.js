function changeImage(){
    $('#img').attr('src','/verifyCode/'+'?'+'/'+Math.random())
}
$(function(){
    //核对验证码
    $('#txtCode').blur(function () {
        var code = $('#txtCode').val();
        $.ajax({
            url:'/checkVerifyCode/',
            data:{
                code:code,
                csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val(),
            },
            dataType:'text',
            type:'post',
            success:function (msg) {
                if(msg=='2'){
                    alert('验证码有误');
                    $('#txtCode').val('');
                    changeImage()

                }
            },
            error:function (msg) {

            }
        })
    });
    $('.btn_register').click(function(){
        var mobile = $('#txtMobile').val();
        var userName = $('#txtUserName').val();
        var pwd = $('#txtPwd').val();
        var confirmPwd = $('#txtConfirmPwd').val();
        var code = $('#txtCode').val();
        var Agreement = $('#rememberMe').is(':checked');
        // 校验
        if(mobile == ''){
            alert('手机号不能为空');
            return;
        }
        if(userName == ''){
            alert('用户名不能为空');
            return;
        }
        if(pwd == ''){
            alert('密码不能为空');
            return;
        }
        if(pwd != confirmPwd){
            alert('两次密码不一致');
            return;
        }
        if(code == ''){
            alert('验证码不能为空');
            return;
        }
        if(Agreement == ''){
            alert('请看协议');
            return;
        }

        // 发送注册请求
        $.ajax({
            url:'/registerPost/',
            data:{
                mobile:mobile,
                userName:userName,
                pwd:pwd,
                confirmPwd:confirmPwd,
                code:code,
                csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val()
            },
            dataType:'text',
            type:'post',
            success:function (msg) {
                if(msg == '0'){
                    alert('验证码错误！');
                    changeImage()
                }
                if(msg == '1'){
                    alert('注册成功！');
                    window.location = '/Login/'
                }
                if(msg == '2'){
                    alert('用户名已存在！');
                }
                if(msg == '3'){
                    alert('手机号已经注册过！');
                }
            },
            error:function (msg) {
                alert('出错了');
            }
        });

    });

});