# -*- coding: utf-8 -*-
# @Time     : 2018/4/27 7:02
# @Author   : ice
# @File     : __init__.py
# @Software : PyCharm
from __future__ import unicode_literals

from flask import Flask

# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'


@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


if __name__ == '__main__':
    # Start app
    app.run(debug=True)
