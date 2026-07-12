import socket
import ipaddress

import dns.resolver
import dns.reversename

import ipwhois
import geoip2.database


class InfrastructureClient:

    def __init__(self):

        self.geo_reader = geoip2.database.Reader(
            "data/GeoLite2-City.mmdb"
        )

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

        geo = self.geo_reader.city(ip)

        return {

            "ip": ip,

            "ip_version": ip_version,

            "ptr": ptr,

            "asn": asn,

            "geo": geo,

        }