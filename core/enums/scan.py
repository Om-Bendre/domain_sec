from enum import Enum


class ScanStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    PARTIAL = "partial"


class ScanType(str, Enum):
    PASSIVE = "passive"
    ACTIVE = "active"
    AUTHENTICATED = "authenticated"


class TargetType(str, Enum):
    DOMAIN = "domain"
    IP = "ip"
    URL = "url"
    INVALID = "invalid"

