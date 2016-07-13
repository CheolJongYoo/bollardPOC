from flask import Flask, render_template, session, redirect, url_for, request, Blueprint


from functools import wraps

import json
import bcrypt

from app import app

from app.decoraters import member_required, user_required



mod_statistics = Blueprint('statistics', __name__, url_prefix='/statistics')


@mod_statistics.route('/')
@member_required
def viewMain():
    return render_template('/statistics/main.html')