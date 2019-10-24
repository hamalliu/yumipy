dbconf = {
    "name": "test_db",
    "dsn": "sqlite://:memory:",
    "read_timeout": 30,  # second
    "write_timeout": 30,  # second
}

ctlconf = {
    ""
}


class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URL = "sqlite://:memory:"
