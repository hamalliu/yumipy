from .service import login, logout, resetpwd
from controllor.route import RouteGroup, RouteConf
from . import middlewares


def router():
    rg = RouteGroup('admin', __name__, url_prefix='/admin', middlewares=[middlewares.Auth])
    rg.add_route(RouteConf('/login', 'login', view_func=login, methods=['POST']))
    rg.add_route(RouteConf('/logout', 'logout', view_func=logout, methods=['POST']))
    rg.add_route(RouteConf('/resetpwd', 'resetpwd', view_func=resetpwd, methods=['POST']))
    return rg
