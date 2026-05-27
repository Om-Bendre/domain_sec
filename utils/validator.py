from utils.records import allowed_records

def is_valid_record(record_type):
    return record_type in allowed_records