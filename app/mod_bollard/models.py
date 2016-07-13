from app import db

class Beacon(db.Model):
    __tablename__ = 'tb_beacon'
    id = db.Column(db.Integer, primary_key=True)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    modifiedAt = db.Column(db.DateTime,default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())

    installDate = db.Column(db.DateTime(), nullable=True)
    updateDate = db.Column(db.DateTime(), nullable=True)
    uuid = db.Column(db.String(255),nullable=False)
    major = db.Column(db.Integer, nullable=False)
    minor = db.Column(db.Integer, nullable=False)
    power = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(255),nullable=True)

    bollard = db.relationship('Bollard', primaryjoin=('Beacon.id==Bollard.beaconId'))
    def __repr__(self):
        return '<uuid %r major %r minor %r bollard %r>' % (self.uuid,self.major,self.minor, self.bollard)


class BollardType(db.Model):
    __tablename__ = 'tb_bollardtype'
    id = db.Column(db.Integer, primary_key=True)

    displayName = db.Column(db.String(100),nullable=False)
    displayImage = db.Column(db.String(255),nullable=True)
    description = db.Column(db.String(255),nullable=True)

    def __init__(self, name, image, description):
        self.displayName = name
        self.displayImage = image
        self.description = description

    def __repr__(self):
        return '<displayName : %r, image : %r, desc : %r>' % (self.displayName, self.displayImage, self.description)

class Bollard(db.Model):
    __tablename__ = 'tb_bollard'
    id = db.Column(db.Integer, primary_key=True)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    modifiedAt = db.Column(db.DateTime,default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
    typeId = db.Column(db.Integer, db.ForeignKey('tb_bollardtype.id'), nullable=False)
    type = db.relationship('BollardType', primaryjoin=('Bollard.typeId==BollardType.id'))
    displayName = db.Column(db.String(100),nullable=False)
    displayImage = db.Column(db.String(255),nullable=True)
    beaconId = db.Column(db.Integer, db.ForeignKey('tb_beacon.id'), nullable=True)
    status = db.Column(db.String(1),default='S')

    beacon = db.relationship('Beacon', primaryjoin=('Bollard.beaconId==Beacon.id'))
    def __repr__(self):
        return '<displayName : %r, beaconCode : %r, status : %r beacon : %r>' % (self.displayName, self.beaconId, self.status, self.beaconId)


class Region(db.Model):
    __tablename__ = 'tb_region'
    id = db.Column(db.Integer, primary_key=True)

    parentId = db.Column(db.Integer, db.ForeignKey('tb_region.id'), nullable=True)
    parent = db.relationship('Region', remote_side=id)#, backref='sub_regions')
    displayName = db.Column(db.String(100), nullable=False)
    displayImageFile = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    centerX = db.Column(db.Float(Precision=64), nullable=False)
    centerY = db.Column(db.Float(Precision=64), nullable=False)
    polygon = db.Column(db.String(1000),nullable=True)
    unitType = db.Column(db.String(1),default='C')
    color = db.Column(db.String(8),default='FF000000')

    def __init__(self):
        pass

    def __repr__(self):
        return '<Region : %r, name : %r, parent : %r>' % (self.id, self.displayName, self.parent)