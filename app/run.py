#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, request
import service.account


app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return 'up'


@app.route('/user/account/register', methods=['POST'])
def user_account_register():
    return service.account.register(request.form)


#if __name__ == '__main__':
#    app.run(debug=True)

r= service.account.register({'account':'1','password':'22'})
print r
