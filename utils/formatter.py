def print_results(domain, record_type, results):

    print("\n==============================")
    print(f"{record_type} Records for {domain}")
    print("==============================\n")

    for index, data in enumerate(results, start=1):
        print(f"{index}. {data}")

def print_reverse_results(ip_address, results):

    print(f"\nPTR Records for {ip_address}\n")

    for index, data in enumerate(results, start=1):
        print(f"{index}. {data}")