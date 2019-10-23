class Controllor:
    __routesConf = dict

    def __init__(self):
        return

    def add_routes_conf(self, blueprint="", conf=None):
        if conf is None:
            return
        self.__routesConf[blueprint] = conf

    def get_route_conf(self, blueprint=''):
        if blueprint is '':
            return
        return self.__routesConf.get(blueprint, default=None)


__ctl = Controllor


def get_ctl():
    return __ctl
