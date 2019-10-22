from controllor import routegroup
from . import middlewares

rg = routegroup.RouteGroup('api', __name__, url_prefix='/api', middlewares=[middlewares.ParseParams])
