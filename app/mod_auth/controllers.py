from flask import Flask, render_template, session, redirect, url_for, request, Blueprint

from app.mod_auth.models import Member, User, UserDevice, UserAuth, SmsAuth

from functools import wraps
from datetime import datetime, timedelta
import bcrypt
import json
import random

from app import app, db

from app.decoraters import member_required, user_required

from app.utils import ResultMap, PagingMap

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/login.do')
def viewLogin():
    return render_template('/member/login.html')



@mod_auth.route('/member/login.json', methods=['POST','GET'])
def api_memberLogin():
    app.logger.debug(request.get_json())
    jsonData = request.get_json()
    memberId = jsonData['memberId']
    password = jsonData['password']

    cryptPassword = bcrypt.hashpw(password.encode('utf-8'),app.config['SECRET_KEY'].encode('utf-8'))

    member = Member.query.filter(Member.memberId == memberId).filter(Member.password == cryptPassword).first()
    app.logger.debug(member)
    resp = ResultMap()


    if member != None:
        session['islogin'] = True
        session['memberid'] = member.memberId
        session['id'] = member.id
        session['name'] = member.displayName
        resp.result = True
        #resp['data'] = json.dumps(member,ensure_ascii=False)
    else:
        resp.message = 'login fail'
        resp.code = 10000
    return resp.to_JSON()

@mod_auth.route('/member/logout.json', methods=['POST','GET'])
@member_required
def api_memberLogout():
    resp = ResultMap()

    if session.get('id',None) == None:
        app.logger.error('not login')
        resp.result = False
        resp.message = 'Not Login'
    else:
        session.clear()
        resp.result = True
    return resp.to_JSON()


@mod_auth.route('/user/signup.json', methods=['POST','GET'])
def api_auth_user_signup():
    pass


@mod_auth.route('/user/signin.json',methods=['POST','GET'])
def api_auth_user_signin():
    pass


def current_sms_token(phoneNumber):
    token = SmsAuth.query.filter(SmsAuth.phoneNumber == phoneNumber).filter(SmsAuth.use == 'N').filter(SmsAuth.expireDate > datetime.now()).first()
    return token

@mod_auth.route('/sms/new', methods=['POST','GET'])
def api_authSmsGetToken():
    #유효기간내의 사용가능한 토큰이 존재하면 해당 토큰 사용불가 처리후 토큰 신규 생성
    #존재하지 않을 경우 즉시 토큰 신규 생성
    #전화번호 없으면 에러
    resp = ResultMap()

    jsonData = request.get_json()
    phoneNumber = jsonData['phoneNumber']

    if phoneNumber == None:
        resp.result = False
        resp.message = '휴대전화 번호 오류'
        return json.dumps(resp,ensure_ascii=False)

    app.logger.info('phone : %r' %(phoneNumber))

    token = current_sms_token(phoneNumber)

    if token != None:
        app.logger.info(token)
        resp.result = False
        resp.message = '이미 발행된 토큰이 존재합니다(3분후 재시도 해주세요)'
        return json.dumps(resp,ensure_ascii=False)

    if token == None:
        token = SmsAuth()
        token.phoneNumber = phoneNumber
        token.expireDate = datetime.now() + timedelta(minutes = 3)
        token.code = random.randint(100000,999999)
        if app.config['DEBUG'] == True:
            token.code = 111111
    if token != None:
        db.session.add(token)
        db.session.commit()

    resp.result = True
    app.logger.info('token : ' + token.code)
    return resp.to_JSON()


@mod_auth.route('/sms/validate', methods=['POST','GET'])
def api_authSmsValidate():
    resp = ResultMap()

    jsonData = request.get_json()
    phoneNumber = jsonData['phoneNumber']
    code = jsonData['code']

    if phoneNumber == None:
        resp.result = False
        resp.message = '휴대전화 번호 오류'
        return json.dumps(resp,ensure_ascii=False)

    if code == None:
        resp.result = False
        resp.message = '인증번호 오류'
        return json.dumps(resp,ensure_ascii=False)

    token = current_sms_token(phoneNumber)
    if token != None:
        if token.code == code:
            resp.result = True
            token.use = 'Y'
            db.session.commit()
            return json.dumps(resp,ensure_ascii=False)
        else:
            resp.message = '인증번호 오류'
    resp.message = '인증 요청이력이 없습니다.'
    return resp.to_JSON()