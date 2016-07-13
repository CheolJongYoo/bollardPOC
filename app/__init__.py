from flask import Flask, render_template, session, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy

from functools import wraps
from datetime import datetime, timedelta
import bcrypt
import json
import random
import logging



app = Flask(__name__)

app.config.from_object('config')


logger = app.logger

db = SQLAlchemy(app)

title = u'볼라드 CMS'



from app.mod_auth.models import Member, User, UserAuth, UserDevice
from app.decoraters import member_required, user_required
from app.mod_bollard.models import Beacon, Bollard, BollardType, Region

from app.mod_auth.controllers import mod_auth
from app.mod_bollard.views import mod_bollard
from app.mod_statistic.controllers import mod_statistics
from app.mod_voc.controllers import mod_voc



def init_database():
    print(app.config['SECRET_KEY'])
    db.metadata.create_all(db.engine)
    if Member.query.count() <= 0:
        cryptPassword = bcrypt.hashpw('orange18'.encode('utf-8'),app.config['SECRET_KEY'].encode('utf-8'))
        member = Member(memberId='player3e',password=cryptPassword,displayName=u'유철종')
        db.session.add(member)
        db.session.commit()

    if Region.query.count() <= 0:
        typeA = BollardType('볼라드A','','볼라드A 형')
        db.session.add(typeA)
        db.session.commit()

        typeB = BollardType('볼라드B','','볼라드B 형')
        db.session.add(typeB)
        db.session.commit()

        region = Region()
        region.displayName = '은평구'
        region.centerX = '37.1234'
        region.centerY = '128.1234'
        region.polygon = '10.0'
        region.unitType = 'C'
        region.color = 'FFEEEEEE'
        db.session.add(region)
        db.session.commit()
        app.logger.debug(region.id)

        child = Region()
        child.parentId = region.id
        child.displayName = '녹번동'
        child.centerX = '37.1234'
        child.centerY = '128.1234'
        child.polygon = '10.0'
        child.unitType = 'C'
        child.color = 'FFEEEEEE'
        db.session.add(child)
        db.session.commit()
        app.logger.debug(child.id)

        child = Region()
        child.parentId = region.id
        child.displayName = '불광제1동'
        child.centerX = '37.1234'
        child.centerY = '128.1234'
        child.polygon = '10.0'
        child.unitType = 'C'
        child.color = 'FFEEEEEE'
        db.session.add(child)
        db.session.commit()
        app.logger.debug(child.id)

        child = Region()
        child.parentId = region.id
        child.displayName = '불광제2동'
        child.centerX = '37.1234'
        child.centerY = '128.1234'
        child.polygon = '10.0'
        child.unitType = 'C'
        child.color = 'FFEEEEEE'
        db.session.add(child)
        db.session.commit()
        app.logger.debug(child.id)

        beacon = Beacon()
        beacon.uuid = '24DDF411-8CF1-440C-87CD-E368DAF9C93E'
        beacon.major = 18503
        beacon.minor = 17735
        beacon.description = 'test1'

        db.session.add(beacon)
        db.session.commit()

        beacon = Beacon()
        beacon.uuid = '24DDF411-8CF1-440C-87CD-E368DAF9C93E'
        beacon.major = 18503
        beacon.minor = 17735
        beacon.description = 'test1'

        db.session.add(beacon)
        db.session.commit()

        beacon = Beacon()
        beacon.uuid = '24DDF411-8CF1-440C-87CD-E368DAF9C93E'
        beacon.major = 18503
        beacon.minor = 17736
        beacon.description = 'test2'

        db.session.add(beacon)
        db.session.commit()

        beacon = Beacon()
        beacon.uuid = '24DDF411-8CF1-440C-87CD-E368DAF9C93E'
        beacon.major = 18503
        beacon.minor = 17737
        beacon.description = 'test3'

        db.session.add(beacon)
        db.session.commit()

        beacon = Beacon()
        beacon.uuid = '24DDF411-8CF1-440C-87CD-E368DAF9C93E'
        beacon.major = 18503
        beacon.minor = 17738
        beacon.description = 'test4'

        db.session.add(beacon)
        db.session.commit()

        bollard = Bollard()
        bollard.displayName = '테스트 볼라드 1번째'
        bollard.beaconId = beacon.id
        bollard.typeId = typeA.id

        db.session.add(bollard)
        db.session.commit()

        bollard = Bollard()
        bollard.displayName = '테스트 볼라드 2번째'
        bollard.beaconId = None
        bollard.typeId = typeA.id

        db.session.add(bollard)
        db.session.commit()

        bollard = Bollard()
        bollard.displayName = '테스트 볼라드 3번째'
        bollard.beaconId = None
        bollard.typeId = typeA.id

        db.session.add(bollard)
        db.session.commit()

        bollard = Bollard()
        bollard.displayName = '테스트 볼라드 4번째'
        bollard.beaconId = None
        bollard.typeId = typeB.id

        db.session.add(bollard)
        db.session.commit()

        bollard = Bollard()
        bollard.displayName = '테스트 볼라드 5번째'
        bollard.beaconId = None
        bollard.typeId = typeB.id

        db.session.add(bollard)
        db.session.commit()

        app.logger.debug(beacon.id)

#@app.before_first_request
#def create_db():
#    init_database()

@app.errorhandler(404)
def errorNotFound(e):
    return render_template('/error/404.html'), 404

@app.route('/')
@member_required
def viewMain():
    regions = Region.query.all()
    app.logger.debug(regions)
    return render_template('index.html')

init_database()

app.register_blueprint(mod_auth)
app.register_blueprint(mod_bollard)
app.register_blueprint(mod_statistics)
app.register_blueprint(mod_voc)
















