from api import routes
from api.admin.service import login, logout, resetpwd
from controllor.route import RouteGroup, RouteConf
from . import middlewares

rg = RouteGroup('admin', __name__, url_prefix='/admin', parent=routes.rg, middlewares=[middlewares.Auth])
rg.register()
rg.add_url_rule('/login', __name__, login, methods='POST', conf=RouteConf(False, False))
rg.add_url_rule('/logout', __name__, logout, methods='POST', conf=RouteConf(False, False))
rg.add_url_rule('/resetpwd', __name__, resetpwd, methods='POST', conf=RouteConf(False, False))

