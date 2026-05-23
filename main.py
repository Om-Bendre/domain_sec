print("dns lookup tool")
import dns.resolver

domain = input("entr domain name: ")
# record = input("enter record type: ").upper()
allowed_records = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]
for rec in allowed_records:
 try:
        result = dns.resolver.resolve(domain,rec)

        
        print("\n========================================")
        print(f"{rec} records for {domain}")
        print("========================================\n")
       
        for index, data in enumerate(result, start=1):
            print(f"{index}. {data}")
        
 except dns.resolver.NXDOMAIN:
     print("domain name doest exist")
     break

 except dns.resolver.NoAnswer:
     print("no record found")

 except dns.resolver.Timeout:
     print("requested timeout")

 except Exception as e:
     print("error", e)