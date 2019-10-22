from flask import Blueprint


class RouteGroup(Blueprint):
    middlewares = []
    parent = {}

    def __init__(self, name, import_name, url_prefix=None, parent=None, middlewares=None):
        self.parent = parent
        self.middlewares.append(middlewares)
        if parent is not None:
            self.middlewares.append(parent.middlewares)
            url_prefix = parent.url_prefix + url_prefix
            name = parent.name + "/" + name

        Blueprint.__init__(self, name, import_name, url_prefix)

    def register(self, app, options, first_registration=False):
        for middleware in self.middlewares:
            self.before_app_request(middleware)
        Blueprint.register(app, options, first_registration)
