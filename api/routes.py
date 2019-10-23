from controllor.route import RouteGroup
from . import middlewares

rg = RouteGroup('api', __name__, url_prefix='/api', middlewares=[middlewares.ParseParams])
