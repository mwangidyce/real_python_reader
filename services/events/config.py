import logging
import os
from ast import literal_eval


def parse_env_dict(env_value, default=None):
    if isinstance(env_value, dict):
        return env_value
    try:
        if env_value and isinstance(env_value, str) and "{" in env_value:
            return literal_eval(env_value)
        return default if default is not None else {}
    except:
        return default if default is not None else {}


NEVVON_CORE = parse_env_dict(
    os.environ.get("NEVVON_CORE"),
    {
        "HOST": "https://apitest.nevvon.com",
        "MAX_ATTEMPT": 3,
        "TIMEOUT": 30,
        "USER": "axiscare_integrations@nevvon.com",
        "PASSWORD": "axiscare2022#",
    },
)

SSO_CORE_URL = os.environ.get("SSO_CORE_URL", "generate-sso")


# Dictionary configurations
DB_CONFIG = parse_env_dict(
    os.environ.get("DB_CONFIG"),
    {
        "DBHOST": "service-sso-sand.cluster-cbsniiq2cl0b.us-east-2.rds.amazonaws.com",
        "DBUSER": "sso_main",
        "DBPASSWORD": "Sdfjj94sjzdj",
        "DBNAME": "sso_sandbox",
    },
)

REDIRECT_CONFIG = parse_env_dict(
    os.environ.get("REDIRECT_CONFIG"),
    {"HOST": "", "BASE_URI": "/sso/{}", "URI": "/redirect?s={}"},
)

REDIRECT_LOGGER_CONFIG = parse_env_dict(
    os.environ.get("REDIRECT_LOGGER_CONFIG"),
    {"LEVEL": logging.DEBUG, "FILE": "/var/log/nevvon/sso_sand/sso_sandbox.log"},
)

UPDATE_LOGGER_CONFIG = parse_env_dict(
    os.environ.get("UPDATE_LOGGER_CONFIG"),
    {"LEVEL": logging.DEBUG, "FILE": "/var/log/nevvon/sso_sand/sso_updates.log"},
)

API_CONFIG = parse_env_dict(
    os.environ.get("API_CONFIG"),
    {
        "MAX_ATTEMPT": 3,
        "TIMEOUT": 40,
        "TRAINING_TEXT": "Click here for your required training, powered by Nevvon",
    },
)

HHAX_CONFIG = parse_env_dict(
    os.environ.get("HHAX_CONFIG"),
    {
        "HOST": "https://sandbox.hhaexchange.com/integration/ENT/V1.8/CustomServices.svc",
        "TRAINING_TEXT": "Click here for your required training, powered by Nevvon",
        "UpdateCareGiverMobileLink": "UpdateCaregiverMobileLink",
    },
)

ACCOUNTS_SERVICE = parse_env_dict(
    os.environ.get("ACCOUNTS_SERVICE"),
    {
        "HOST": "http://localhost:8888",
        "BASE_URI": "api/v1/",
        "GET_ACCOUNTS_URI": "Accounts/{}",
        "MAX_ATTEMPT": 3,
        "TIMEOUT": 60,
    },
)

ID_MAPPING_CONFIG = parse_env_dict(
    os.environ.get("ID_MAPPING_CONFIG"),
    {
        "HOST": "http://localhost",
        "PORT": 3030,
        "MAX_ATTEMPT": 3,
        "TIMEOUT": 60,
        "USER": "",
        "PASSWORD": "",
    },
)

GUID_ORGID_MAP = parse_env_dict(os.environ.get("GUID_ORGID_MAP"), {"someguid": 568})

CARIBOU_CONFIG = parse_env_dict(
    os.environ.get("CARIBOU_CONFIG"),
    {
        "HOST": "https://app.caribou.care",
        "MAX_ATTEMPT": 3,
        "TIMEOUT": 60,
        "AUTH_TOKEN": "sample_auth",
    },
)

# Non-dictionary configurations
CARIBOU_TOKEN = os.environ.get("CARIBOU_TOKEN", "sample_token")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "abcdefghijklmnop123")
PORT = os.environ.get("PORT", 5000)
HOST = os.environ.get("HOST", "0.0.0.0")
DEBUG = os.environ.get("DEBUG", True)
TOKEN_EXPIRY_DAYS = int(os.environ.get("TOKEN_EXPIRY_DAYS", 365))
EXPIRATION_DATE = os.environ.get("APP_EXPIRATION_DATE", "1970-01-01")
BLINK_HARDCODED_ORG_ID = int(os.environ.get("BLINK_HARDCODED_ORG_ID", 64))
ERROR_PAGE_REDIRECT = os.environ.get("ERROR_PAGE_REDIRECT", "google.com")
TOKEN_TTL = int(os.environ.get("TOKEN_TTL", 31536000))

# Special case for WEBTRAINING_TARGET since it contains formatting
WEBTRAINING_TARGET = os.environ.get(
    "WEBTRAINING_TARGET", "https://webtraining.nevvon.com/#/{}"
)
