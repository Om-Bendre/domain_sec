import dns.resolver
from utils.resolver import lookup
from utils.formatter import print_results, print_reverse_results, print_ptr_intelligence, print_dnssec_info
from utils.validator import is_valid_record, is_valid_ip
from utils.timer import start_timer, stop_timer
from utils.dns_servers import dns_cust_servers
from utils.reverse_lookup import reverse_lookup
from utils.ip_extractor import extract_ips
from intelligence.ptr_intel import analyze_ptr
from utils.dnssec import check_dnssec
from utils.whois_lookup import lookup_whois
from utils.formatter import print_whois_info, print_asn_info, print_geoip_info, print_ipv6_info
from utils.asn_lookup import lookup_asn
from utils.geoip_lookup import lookup_geoip
from utils.ipv6_analysis import analyze_ipv6



def run_infrastructure_analysis(ips, selected_name, selected_ip):
    """
    Shared infrastructure analysis block.
    Accepts a list of IPs and runs PTR intelligence on each.
    """
    print("\nInfrastructure analysis available for the followin  IPs:")
    for i, ip in enumerate(ips, start=1):
        print(f"  {i}. {ip}")

    choice = input("\nView infrastructure analysis? (y/n): ").strip().lower()

    if choice != 'y':
        return

    for ip in ips:
        print(f"\n[ Analyzing {ip} ]")

        try:
            start = start_timer()
            ptr_results = reverse_lookup(ip, selected_ip)
            elapsed = stop_timer(start)

            print_reverse_results(ip, ptr_results)
            print(f"  Lookup Time : {elapsed * 1000:.2f} ms")

            for record in ptr_results:
                intel = analyze_ptr(str(record))
                print_ptr_intelligence(intel)
                geo = lookup_geoip(ip)
                print_geoip_info(ip, geo)
                asn_info = lookup_asn(ip)
                print_asn_info(ip, asn_info)


        except dns.resolver.NXDOMAIN:
            print(f"  No PTR record found for {ip}")
        except dns.resolver.Timeout:
            print(f"  Request timed out for {ip}")
        except Exception as e:
            print(f"  Error analyzing {ip}: {e}")


def main():
    print("\nChoose Operation:\n")
    print("1. Forward Lookup")
    print("2. Reverse Lookup")
    print("3. DNSSEC check")
    print("4. WHOIS lookup")
    operation = input("\nEnter choice: ")

    print("\nChoose DNS Resolver:\n")
    for key, value in dns_cust_servers.items():
        print(f"{key}. {value[0]}")
    choice = input("\nEnter choice: ")

    if choice not in dns_cust_servers:
        print("Invalid choice")
        return

    selected_name, selected_ip = dns_cust_servers[choice]

    # This list is populated by whichever branch runs
    # The shared analysis block reads from it afterward
    ips_for_analysis = []

    if operation == "1":
        domain = input("Enter domain: ")
        record_type = input("Enter record type: ").upper()

        if not is_valid_record(record_type):
            print("Invalid record type")
            return

        try:
            start = start_timer()
            results, ttl = lookup(domain, record_type, selected_ip)
            elapsed = stop_timer(start)

            print_results(domain, record_type, results, ttl)

            if record_type == "AAAA":
             for ipv6 in results:
              info = analyze_ipv6(str(ipv6))
              print_ipv6_info(info)
              
            print(f"\nResolver Used : {selected_name} ({selected_ip})")
            print(f"Lookup Time   : {elapsed * 1000:.2f} ms")

            # Extract IPs if record type contains them directly
            ips_for_analysis = extract_ips(results, record_type)

        except dns.resolver.NXDOMAIN:
            print("Domain does not exist")
            return
        except dns.resolver.NoAnswer:
            print("No record found")
            return
        except dns.resolver.Timeout:
            print("Request timed out")
            return
        except Exception as e:
            print(f"Error: {e}")
            return

    elif operation == "2":
        ip_address = input("Enter IP Address: ")

        if not is_valid_ip(ip_address):
            print("Invalid IP Address")
            return

        try:
            start = start_timer()
            ptr_results = reverse_lookup(ip_address, selected_ip)
            elapsed = stop_timer(start)

            print_reverse_results(ip_address, ptr_results)
            print(f"\nResolver Used : {selected_name} ({selected_ip})")
            print(f"Lookup Time   : {elapsed * 1000:.2f} ms")

            # The input IP is directly available for analysis
            ips_for_analysis = [ip_address]

        except dns.resolver.NXDOMAIN:
            print("No PTR record found")
            return
        except dns.resolver.Timeout:
            print("Request timed out")
            return
        except Exception as e:
            print(f"Error: {e}")
            return
        
    elif operation == "3":
        domain = input("Enter domain: ")

        try:

            start = start_timer()

            enabled, dnskeys = check_dnssec(
                domain,
                selected_ip
            )

            elapsed = stop_timer(start)

            print_dnssec_info(
                domain,
                enabled,
                dnskeys
            )

            print(f"\nResolver Used : {selected_name} ({selected_ip})")
            print(f"Lookup Time   : {elapsed * 1000:.2f} ms")

        except dns.resolver.NXDOMAIN:
            print("Domain does not exist")

        except dns.resolver.Timeout:
            print("Request timed out")

        except Exception as e:
         print(f"Error : {e}")

    elif operation == "4":

     domain = input("Enter domain: ")

     try:

        start = start_timer()

        info = lookup_whois(domain)

        elapsed = stop_timer(start)

        print_whois_info(info)

        print(f"\nLookup Time   : {elapsed * 1000:.2f} ms")

     except Exception as e:
        print(f"Error: {e}")

    else:
        print("Invalid operation")
        return

    # Shared infrastructure analysis block
    # Runs after either branch if IPs are available
    if ips_for_analysis:
        run_infrastructure_analysis(ips_for_analysis, selected_name, selected_ip)
    else:
        print("\n(Infrastructure analysis not available for this record type)")


if __name__ == "__main__":
    main()