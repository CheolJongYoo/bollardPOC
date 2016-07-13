from app import db

class Member(db.Model):
    __tablename__ = 'tb_member'
    id = db.Column(db.Integer, primary_key=True)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    modifiedAt = db.Column(db.DateTime,default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
    memberId = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(256), nullable=False)
    displayName = db.Column(db.String(100), nullable=False)
    expireDate = db.Column(db.DateTime(), nullable=True)

    def __init__(self,memberId,password,displayName):
        self.memberId = memberId
        self.password = password
        self.displayName = displayName

    def __repr__(self):
        return '<Member : %r>' % (self.memberId)

class User(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    modifiedAt = db.Column(db.DateTime,default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
    userPhone = db.Column(db.String(20), unique=True)
    displayName = db.Column(db.String(20), nullable=True)
    displayImageFile = db.Column(db.String(255), nullable=True)
    userStatus = db.Column(db.String(1),default='A')

    def __init__(self):
        pass

    def __repr__(self):
        return '<User : %r>' % (self.userPhone)


class UserAuth(db.Model):
    __tablename__ = 'tb_userauth'
    id = db.Column(db.Integer, primary_key=True)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    authToken = db.Column(db.String(255), nullable=False)
    userCode = db.Column(db.Integer, db.ForeignKey('tb_user.id'), nullable=False)
    expireDate = db.Column(db.DateTime(), nullable=True)
    def __init__(self):
        pass

    def __repr__(self):
        return '<UserAuth : %r>' % (self.userCode)

class SmsAuth(db.Model):
    __tablename__ = 'tb_smsauth'
    id = db.Column(db.Integer, primary_key=True)
    createAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    modifiedAt = db.Column(db.DateTime,default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
    phoneNumber = db.Column(db.String(20), nullable=False)
    expireDate = db.Column(db.DateTime(), nullable=False)
    code = db.Column(db.String(6), nullable=False)
    use = db.Column(db.String(1),default='N')

    def __repr__(self):
        return '<phonenumber : %r, exp : %r, code : %r, use : %r>' % (self.phoneNumber, self.expireDate, self.code, self.use)



class UserDevice(db.Model):
    __tablename__ = 'tb_userdevice'
    id = db.Column(db.Integer, primary_key=True)
