from flask import Flask, render_template, session, redirect, url_for, request, Blueprint
from flask_sqlalchemy import Pagination
from app.mod_bollard.models import BollardType,Beacon,Bollard, Region

from functools import wraps

import json
import bcrypt

from app import app

from app.decoraters import member_required, user_required
from app.utils import PagingMap


mod_bollard = Blueprint('bollard', __name__, url_prefix='/bollard')



@mod_bollard.route('/')
@member_required
def viewMain():
    return render_template('/bollard/main.html')

@mod_bollard.route('/add')
@member_required
def viewAdd():
    return render_template('/bollard/add.html')

@mod_bollard.route('/list')
@member_required
def viewList():

    bollard = Bollard.query.paginate(4,2)
    print(bollard)
    paging = PagingMap()
    paging.totalCount = 10
    paging.totalPage = 1
    paging.curPage = 1
    paging.countPerPage = 10
    paging.data = bollard.items

    return render_template('/bollard/bollardlist.html',
                           paging = paging
    )


@mod_bollard.route('/beacon')
@member_required
def viewBeacon():
    beacons = Beacon.query.all()
    app.logger.debug(beacons)
    return render_template('/bollard/beacon.html',
                           beacons = beacons
                           )

@mod_bollard.route('/region')
@member_required
def viewRegion():
    regions = Region.query.all()
    return render_template('/bollard/region.html',
                           regions = regions
                           )


@mod_bollard.route('/add.json', methods=['POST','GET'])
def api_bollard_add():
    #볼라드 신규 생성
    #비콘정보 입력( uuid, major, minor )
    #생성시 동일 비콘이 존재하면 에러
    #비콘 정보 대신 비콘 id
    pass

