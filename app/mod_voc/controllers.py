from flask import Flask, render_template, session, redirect, url_for, request, Blueprint


from functools import wraps

import json
import bcrypt

from app import app

from app.decoraters import member_required, user_required



mod_voc = Blueprint('voc', __name__, url_prefix='/voc')


@mod_voc.route('/')
@member_required
def viewMain():
    return render_template('/voc/main.html')