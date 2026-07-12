class InfrastructureNormalizer:

    def normalize(
        self,
        raw_data,
    ):

        asn = raw_data["asn"]
        geo = raw_data["geo"]

        network = asn.get("network")

        return {

            "ip": raw_data["ip"],

            "ip_version": raw_data["ip_version"],

            "ptr": raw_data["ptr"],

            "asn": asn.get("asn"),

            "asn_registry": asn.get("asn_registry"),

            "asn_country": asn.get("asn_country_code"),

            "asn_description": asn.get("asn_description"),

            "network_name": (
                network.get("name")
                if network
                else None
            ),

            "network_handle": (
                network.get("handle")
                if network
                else None
            ),

            "cidr": (
                network.get("cidr")
                if network
                else None
            ),

            "network_type": (
                network.get("type")
                if network
                else None
            ),

            "start_address": (
                network.get("start_address")
                if network
                else None
            ),

            "end_address": (
                network.get("end_address")
                if network
                else None
            ),

            "country": geo.country.name,

            "country_code": geo.country.iso_code,

            "region": geo.subdivisions.most_specific.name,

            "city": geo.city.name,

            "postal_code": geo.postal.code,

            "latitude": geo.location.latitude,

            "longitude": geo.location.longitude,

            "time_zone": geo.location.time_zone,

            "accuracy_radius": geo.location.accuracy_radius,

        }