from controllor import routegroup
from . import middlewares
from api import routegroup

rg = routegroup.RouteGroup('admin', __name__, url_prefix='/admin', parent=routegroup.rg, middlewares=[middlewares.Auth])
