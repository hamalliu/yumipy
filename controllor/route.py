from flask import Blueprint

from .controllor import get_ctl


def register_route_group(rg, app):
    if rg.children is not None and len(rg.children) != 0:
        for i in range(len(rg.children)):
            rg.children[i].name = rg.name + "/" + rg.children[i].name
            rg.children[i].url_prefix = rg.url_prefix + rg.children[i].url_prefix
            rg.children[i].middlewares.append(rg.middlewares)
            register_route_group(rg.children[i], app)

    if rg.routes is not None:
        bp = Blueprint(rg.name, rg.import_name, url_prefix=rg.url_prefix)
        for i in range(len(rg.routes)):
            get_ctl().add_routes_conf(rg.name, rg.routes[i])
            bp.add_url_rule(rg.routes[i].rule, rg.routes[i].endpoint, rg.routes[i].view_func,
                            methods=rg.routes[i].methods)
        bp.register(app, {'url_prefix': rg.url_prefix}, first_registration=True)
        return


class RouteGroup:
    def __init__(self, name, import_name, url_prefix=None, middlewares=None):
        self.name = ""
        self.import_name = ""
        self.url_prefix = ""
        self.middlewares = []
        self.routes = []
        self.children = []

        self.name = name
        self.import_name = import_name
        self.url_prefix = url_prefix
        self.middlewares.append(middlewares)

    def register(self, app):
        register_route_group(self, app)

    def add_route(self, route=None):
        if route is not None:
            self.routes.append(route)
        pass

    def add_group(self, group=None):
        if group is not None:
            self.children.append(group)
        pass


class RouteConf:
    def __init__(self, rule, endpoint, view_func, methods, parse=False, decrypt=False):
        self.rule = rule
        self.endpoint = endpoint
        self.view_func = view_func
        self.methods = methods
        self.parse = parse
        self.decrypt = decrypt
