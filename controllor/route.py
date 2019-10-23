from flask import Blueprint

from controllor.controllor import get_ctl


class RouteGroup(Blueprint):
    __middlewares = []
    __parent = {}

    def __init__(self, name, import_name, url_prefix=None, parent=None, middlewares=None):
        self.__parent = parent
        self.__middlewares.append(middlewares)
        if parent is not None:
            self.__middlewares.append(parent.middlewares)
            url_prefix = parent.url_prefix + url_prefix
            name = parent.name + "/" + name

        Blueprint.__init__(self, name, import_name, url_prefix)

    def register(self, app, options, first_registration=False):
        for middleware in self.__middlewares:
            self.before_app_request(middleware)
        options = self.name
        Blueprint.register(app, options, first_registration)

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        get_ctl().add_routes_conf(self.name, options.pop("conf"))
        Blueprint.add_url_rule(self, rule, endpoint, view_func, **options)


class RouteConf:
    __parse = False
    __decrypt = False

    def __init__(self, parse=False, decrypt=False):
        self.__parse = parse
        self.__decrypt = decrypt
