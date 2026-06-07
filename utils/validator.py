from utils.records import allowed_records
import ipaddress

def is_valid_record(record_type):
    return record_type in allowed_records

def is_valid_ip(ip_addr):

    try:
        ipaddress.ip_address(ip_addr)
        return True

    except ValueError:
        return False