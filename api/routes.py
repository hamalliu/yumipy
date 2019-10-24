from controllor.route import RouteGroup
from . import middlewares
from . import admin


def router():
    rg = RouteGroup('api', __name__, url_prefix='/api', middlewares=[middlewares.parse_params])
    rg.add_group(admin.router())
    return rg
