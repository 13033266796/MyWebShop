$(function () {
    $('#prePwd').blur(function () {
        if($('#prePwd').val()==''){
            $('#preTip').text('原密码不能为空')
        }
        else
            $('#preTip').text('*')
    });
    $('#newPwd').blur(function () {
        if($('#newPwd').val()==''){
            $('#newTip').text('新密码不能为空')
        }
        else
            $('#newTip').text('*')
    });
    $('#confirmPwd').blur(function () {
        if($('#confirmPwd').val()==''){
            $('#confirmTip').text('新密码不能为空');
        }
        else
            $('#confirmTip').text('*');
        if($('#confirmPwd').val()!=$('#newPwd').val()){
            $('#confirmTip').text('两次密码不一致');
            $('#confirmPwd').val('');
        }
        else
            $('#confirmTip').text('*');
    });

    $('#updatePwdBtn').click(function () {
        var prePwd = $('#prePwd').val();
        var newPwd = $('#newPwd').val();
        var confirmPwd = $('#confirmPwd').val();
        //校验
        if(prePwd==''){
            $('#preTip').text('原密码不能为空')
        }
        if(newPwd==''){
            $('#newTip').text('新密码不能为空')
        }
        if(confirmPwd==''){
            $('#confirmTip').text('新密码不能为空')
        }
        //异步发送数据
        $.ajax({
            url:'/updatePwdPost/',
            data:{
                prePwd:prePwd,
                newPwd:newPwd,
                csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val(),
            },
            type:'post',
            dataType:'text',
            success:function (msg) {
                if (msg=='yes'){
                    alert('修改成功')
                    //修改完重新登录
                }
                if (msg=='prePwd_error') {
                    $('#preTip').text('原密码错误')
                }
            },
            error:function (msg) {
                alert('错误')
            }
        })
    })
});