from flask import Flask, render_template, session, redirect, url_for, request, Blueprint


from functools import wraps

def member_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if session.get('memberid',None) is None:
            return redirect(url_for('auth.viewLogin', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def user_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if session.get('userid',None) is None:
            resp = {}
            resp['result'] = False
            resp['code'] = 10001
            resp['message'] = "인증이 필요합니다"
            return resp
        return f(*args, **kwargs)
    return decorated_function