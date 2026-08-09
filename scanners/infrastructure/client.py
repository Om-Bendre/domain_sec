import socket
import ipaddress

import dns.resolver
import dns.reversename

import ipwhois



class InfrastructureClient:

  
    def query(
        self,
        target: str,
    ):

        ip = socket.gethostbyname(target)

        ip_version = ipaddress.ip_address(ip).version

        reverse_name = dns.reversename.from_address(ip)

        resolver = dns.resolver.Resolver()

        try:
            ptr = str(
                resolver.resolve(
                    reverse_name,
                    "PTR",
                )[0]
            )

        except Exception:
            ptr = None

        asn = ipwhois.IPWhois(
            ip
        ).lookup_rdap()

        
        return {

            "ip": ip,

            "ip_version": ip_version,

            "ptr": ptr,

            "asn": asn,

        }