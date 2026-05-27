
def print_results(domain, record_type, results):

    print("\n==============================")
    print(f"{record_type} Records for {domain}")
    print("==============================\n")

    for index, data in enumerate(results, start=1):
        print(f"{index}. {data}")