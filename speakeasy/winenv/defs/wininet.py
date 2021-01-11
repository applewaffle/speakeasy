# Copyright (C) 2020 FireEye, Inc. All Rights Reserved.

import ctypes as ct
from speakeasy.struct import EmuStruct, Ptr


INTERNET_FLAG_ASYNC = 0x10000000
INTERNET_FLAG_CACHE_ASYNC = 0x00000080
INTERNET_FLAG_CACHE_IF_NET_FAIL = 0x00010000
INTERNET_FLAG_DONT_CACHE = 0x04000000
INTERNET_FLAG_EXISTING_CONNECT = 0x20000000
INTERNET_FLAG_FORMS_SUBMIT = 0x00000040
INTERNET_FLAG_FROM_CACHE = 0x01000000
INTERNET_FLAG_FWD_BACK = 0x00000020
INTERNET_FLAG_HYPERLINK = 0x00000400
INTERNET_FLAG_IGNORE_CERT_CN_INVALID = 0x00001000
INTERNET_FLAG_IGNORE_CERT_DATE_INVALID = 0x00002000
INTERNET_FLAG_IGNORE_REDIRECT_TO_HTTP = 0x00008000
INTERNET_FLAG_IGNORE_REDIRECT_TO_HTTPS = 0x00004000
INTERNET_FLAG_KEEP_CONNECTION = 0x00400000
INTERNET_FLAG_MAKE_PERSISTENT = 0x02000000
INTERNET_FLAG_MUST_CACHE_REQUEST = 0x00000010
INTERNET_FLAG_NEED_FILE = 0x00000010
INTERNET_FLAG_NO_AUTH = 0x00040000
INTERNET_FLAG_NO_AUTO_REDIRECT = 0x00200000
INTERNET_FLAG_NO_COOKIES = 0x00080000
INTERNET_FLAG_NO_UI = 0x00000200
INTERNET_FLAG_OFFLINE = 0x01000000
INTERNET_FLAG_PASSIVE = 0x08000000
INTERNET_FLAG_PRAGMA_NOCACHE = 0x00000100
INTERNET_FLAG_RAW_DATA = 0x40000000
INTERNET_FLAG_READ_PREFETCH = 0x00100000
INTERNET_FLAG_RELOAD = 0x80000000
INTERNET_FLAG_RESTRICTED_ZONE = 0x00020000
INTERNET_FLAG_RESYNCHRONIZE = 0x00000800
INTERNET_FLAG_SECURE = 0x00800000
INTERNET_FLAG_TRANSFER_ASCII = 0x00000001
INTERNET_FLAG_TRANSFER_BINARY = 0x00000002
INTERNET_NO_CALLBACK = 0x00000000
INTERNET_OPTION_SUPPRESS_SERVER_AUTH = 104
WININET_API_FLAG_ASYNC = 0x00000001
WININET_API_FLAG_SYNC = 0x00000004
WININET_API_FLAG_USE_CONTEXT = 0x00000008

INTERNET_SCHEME_PARTIAL = -2
INTERNET_SCHEME_UNKNOWN = -1
INTERNET_SCHEME_DEFAULT = 0
INTERNET_SCHEME_FTP = 1
INTERNET_SCHEME_GOPHER = 2
INTERNET_SCHEME_HTTP = 3
INTERNET_SCHEME_HTTPS = 4

HTTP_QUERY_STATUS_CODE = 19
HTTP_STATUS_OK = "200"

WINHTTP_ADDREQ_INDEX_MASK = 0x0000FFFF
WINHTTP_ADDREQ_FLAGS_MASK = 0xFFFF0000
WINHTTP_ADDREQ_FLAG_ADD_IF_NEW = 0x10000000
WINHTTP_ADDREQ_FLAG_ADD = 0x20000000
WINHTTP_ADDREQ_FLAG_COALESCE_WITH_COMMA = 0x40000000
WINHTTP_ADDREQ_FLAG_COALESCE_WITH_SEMICOLON = 0x01000000

WINHTTP_QUERY_MIME_VERSION = 0
WINHTTP_QUERY_CONTENT_TYPE = 1
WINHTTP_QUERY_CONTENT_TRANSFER_ENCODING = 2
WINHTTP_QUERY_CONTENT_ID = 3
WINHTTP_QUERY_CONTENT_DESCRIPTION = 4
WINHTTP_QUERY_CONTENT_LENGTH = 5
WINHTTP_QUERY_CONTENT_LANGUAGE = 6
WINHTTP_QUERY_ALLOW = 7
WINHTTP_QUERY_PUBLIC = 8
WINHTTP_QUERY_DATE = 9
WINHTTP_QUERY_EXPIRES = 10
WINHTTP_QUERY_LAST_MODIFIED = 11
WINHTTP_QUERY_MESSAGE_ID = 12
WINHTTP_QUERY_URI = 13
WINHTTP_QUERY_DERIVED_FROM = 14
WINHTTP_QUERY_COST = 15
WINHTTP_QUERY_LINK = 16
WINHTTP_QUERY_PRAGMA = 17
WINHTTP_QUERY_VERSION = 18
WINHTTP_QUERY_STATUS_CODE = 19
WINHTTP_QUERY_STATUS_TEXT = 20
WINHTTP_QUERY_RAW_HEADERS = 21
WINHTTP_QUERY_RAW_HEADERS_CRLF = 22
WINHTTP_QUERY_CONNECTION = 23
WINHTTP_QUERY_ACCEPT = 24
WINHTTP_QUERY_ACCEPT_CHARSET = 25
WINHTTP_QUERY_ACCEPT_ENCODING = 26
WINHTTP_QUERY_ACCEPT_LANGUAGE = 27
WINHTTP_QUERY_AUTHORIZATION = 28
WINHTTP_QUERY_CONTENT_ENCODING = 29
WINHTTP_QUERY_FORWARDED = 30
WINHTTP_QUERY_FROM = 31
WINHTTP_QUERY_IF_MODIFIED_SINCE = 32
WINHTTP_QUERY_LOCATION = 33
WINHTTP_QUERY_ORIG_URI = 34
WINHTTP_QUERY_REFERER = 35
WINHTTP_QUERY_RETRY_AFTER = 36
WINHTTP_QUERY_SERVER = 37
WINHTTP_QUERY_TITLE = 38
WINHTTP_QUERY_USER_AGENT = 39
WINHTTP_QUERY_WWW_AUTHENTICATE = 40
WINHTTP_QUERY_PROXY_AUTHENTICATE = 41
WINHTTP_QUERY_ACCEPT_RANGES = 42
WINHTTP_QUERY_SET_COOKIE = 43
WINHTTP_QUERY_COOKIE = 44
WINHTTP_QUERY_REQUEST_METHOD = 45
WINHTTP_QUERY_REFRESH = 46
WINHTTP_QUERY_CONTENT_DISPOSITION = 47
WINHTTP_QUERY_AGE = 48
WINHTTP_QUERY_CACHE_CONTROL = 49
WINHTTP_QUERY_CONTENT_BASE = 50
WINHTTP_QUERY_CONTENT_LOCATION = 51
WINHTTP_QUERY_CONTENT_MD5 = 52
WINHTTP_QUERY_CONTENT_RANGE = 53
WINHTTP_QUERY_ETAG = 54
WINHTTP_QUERY_HOST = 55
WINHTTP_QUERY_IF_MATCH = 56
WINHTTP_QUERY_IF_NONE_MATCH = 57
WINHTTP_QUERY_IF_RANGE = 58
WINHTTP_QUERY_IF_UNMODIFIED_SINCE = 59
WINHTTP_QUERY_MAX_FORWARDS = 60
WINHTTP_QUERY_PROXY_AUTHORIZATION = 61
WINHTTP_QUERY_RANGE = 62
WINHTTP_QUERY_TRANSFER_ENCODING = 63
WINHTTP_QUERY_UPGRADE = 64
WINHTTP_QUERY_VARY = 65
WINHTTP_QUERY_VIA = 66
WINHTTP_QUERY_WARNING = 67
WINHTTP_QUERY_EXPECT = 68
WINHTTP_QUERY_PROXY_CONNECTION = 69
WINHTTP_QUERY_UNLESS_MODIFIED_SINCE = 70
WINHTTP_QUERY_PROXY_SUPPORT = 75
WINHTTP_QUERY_AUTHENTICATION_INFO = 76
WINHTTP_QUERY_PASSPORT_URLS = 77
WINHTTP_QUERY_PASSPORT_CONFIG = 78
WINHTTP_QUERY_MAX = 78


INTERNET_OPTION_SECURITY_FLAGS = 31

SECURITY_FLAG_SECURE = 1

ERROR_INSUFFICIENT_BUFFER = 122


class URL_COMPONENTS(EmuStruct):
    def __init__(self, ptr_size):
        super().__init__(ptr_size)
        self.dwStructSize = ct.c_uint32
        self.lpszScheme = Ptr
        self.dwSchemeLength = ct.c_uint32
        self.nScheme = ct.c_uint32
        self.lpszHostName = Ptr
        self.dwHostNameLength = ct.c_uint32
        self.nPort = ct.c_uint16
        self.lpszUserName = Ptr
        self.dwUserNameLength = ct.c_uint32
        self.lpszPassword = Ptr
        self.dwPasswordLength = ct.c_uint32
        self.lpszUrlPath = Ptr
        self.dwUrlPathLength = ct.c_uint32
        self.lpszExtraInfo = Ptr
        self.dwExtraInfoLength = ct.c_uint32


def get_const_defines(flags, prefix=''):
    defs = []
    for k, v in globals().items():
        if isinstance(v, int):
            if v & flags:
                if prefix:
                    if k.startswith(prefix):
                        defs.append(k)
                else:
                    defs.append(k)
    return defs


def get_flag_defines(flags):
    return get_const_defines(flags, prefix='INTERNET_FLAG')


def get_header_info(info):
    for k, v in globals().items():
        if k.startswith('HTTP_QUERY') and v == info:
            return k


def get_option_define(opt):
    for k, v in globals().items():
        if k.startswith('INTERNET_OPTION_') and v == opt:
            return k


def get_header_info_winhttp(flags):
    return get_const_defines(flags, prefix='WINHTTP_ADDREQ_')


def get_header_query(opt):
    for k, v in globals().items():
        if k.startswith('WINHTTP_QUERY_') and v == opt:
            return k
