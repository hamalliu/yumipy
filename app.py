import os

from flask import Flask

from db import init_db
from controllor import init_ctl
from api import router


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object('config.Config')
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 初始化db
    # init_db(app)

    # 初始化controllor
    init_ctl(app.config.get("controllor"))

    # 注册路由
    router().register(app)

    return app


if __name__ == '__main__':
    create_app().run()
