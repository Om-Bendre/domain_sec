import dns.resolver
from utils.resolver import lookup
from utils.formatter import print_results
from utils.validator import is_valid_record
from utils.timer import start_timer, stop_timer
from utils.dns_servers import dns_cust_servers
from utils.reverse_lookup import reverse_lookup
from utils.validator import is_valid_ip
from utils.formatter import print_reverse_results


def main():

    print("\nChoose Operation:\n")
    print("1. Forward Lookup")
    print("2. Reverse Lookup")

    operation = input("\nEnter choice: ")

    print("\nChoose DNS Resolver:\n")

    for key, value in dns_cust_servers.items():
        print(f"{key}. {value[0]}")

    choice = input("\nEnter choice: ")

    if choice not in dns_cust_servers:
        print("Invalid choice")
        return

    selected_name, selected_ip = dns_cust_servers[choice]

    if operation == "1":

     domain = input("Enter domain: ")
     record_type = input("Enter record type: ").upper()

     if not is_valid_record(record_type):
        print("Invalid record type")

     else:
        try:

            start = start_timer()

            results = lookup(
                domain,
                record_type,
                selected_ip
            )

            end = stop_timer(start)

            print_results(
                domain,
                record_type,
                results
            )

            print(
                f"\nResolver Used: "
                f"{selected_name} ({selected_ip})"
            )

            print(
                f"\nLookup time: "
                f"{end * 1000:.2f}ms\n"
            )

        except dns.resolver.NXDOMAIN:
            print("Domain does not exist")

        except dns.resolver.NoAnswer:
            print("No record found")

        except dns.resolver.Timeout:
            print("Request timed out")

        except Exception as e:
            print(f"Error: {e}")

    elif operation == "2":

     ip_address = input("Enter IP Address: ")

     if not is_valid_ip(ip_address):
        print("Invalid IP Address")
        return

     try:

        start = start_timer()

        results = reverse_lookup(
            ip_address,
            selected_ip
        )

        elapsed = stop_timer(start)

        print_reverse_results(
            ip_address,
            results
        )

        print(
            f"\nResolver Used: "
            f"{selected_name} ({selected_ip})"
        )

        print(
            f"\nLookup Time: "
            f"{elapsed * 1000:.2f} ms"
        )

     except dns.resolver.NXDOMAIN:
        print("No PTR record found")

     except dns.resolver.Timeout:
        print("Request timed out")

     except Exception as e:
        print(f"Error: {e}")      

    else:
     print("Invalid operation")     


if __name__ == "__main__":
    main()