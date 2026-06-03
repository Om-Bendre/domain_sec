import dns.resolver
from utils.resolver import lookup
from utils.formatter import print_results
from utils.validator import is_valid_record
from utils.timer import start_timer, stop_timer
from utils.cust_resolver import dns_cust_servers
from utils.reverse_lookup import reverse_lookup

print("\n1.Forward lookup\n2.reverse lookup")
lookup_choice = input("\nEnter your choice")

if lookup_choice == 1:
    print("\nChoose DNS Resolver:\n")
    for key, value in dns_cust_servers.items():
        print(f"{key}. {value[0]}")

    choice = input("\nEnter choice: ")

    if choice not in dns_cust_servers:
        print("Invalid choice")
        exit()

    selected_name, selected_ip = dns_cust_servers[choice]

    domain = input("Enter domain: ")
    record_type = input("Enter record type: ").upper()

    if not is_valid_record(record_type):
        print("Invalid record type")

    else:
        try:
            start = start_timer()
            results = lookup(domain, record_type, selected_ip)
            end = stop_timer(start)

            print_results(domain, record_type, results)
            print(f"\nResolver Used: {selected_name} ({selected_ip})")
            print(f"\nLookup time: {end * 1000:.2f}ms\n")

        except dns.resolver.NXDOMAIN:
            print("Domain does not exist")

        except dns.resolver.NoAnswer:
            print("No record found")

        except dns.resolver.Timeout:
            print("[Request timed out")

        except Exception as e:
            print(f"Error: {e}")
