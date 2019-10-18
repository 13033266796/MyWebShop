from django.http import HttpResponse,HttpResponseRedirect

def isLogin(func):
    def isLogin_Set(request,*args):
        if request.session.get('nickName'):
            isLogin = 1
            return func(request,*args,isLogin)

        else:
            red = HttpResponseRedirect('/Login/')
            red.set_cookie('url',request.get_full_path())
            return red
    return isLogin_Set