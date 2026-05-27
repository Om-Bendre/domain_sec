import dns.resolver
from utils.resolver import lookup
from utils.formatter import print_results
from utils.validator import is_valid_record

domain = input("Enter domain: ")
record_type = input("Enter record type: ").upper()

if not is_valid_record(record_type):
    print("Invalid record type")

else:
    try:
        results = lookup(domain, record_type)

        print_results(domain, record_type, results)

    except dns.resolver.NXDOMAIN:
        print("Domain does not exist")

    except dns.resolver.NoAnswer:
        print("No record found")

    except dns.resolver.Timeout:
        print("[Request timed out")

    except Exception as e:
        print(f"Error: {e}")