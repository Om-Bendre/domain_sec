class InfrastructureNormalizer:

    def normalize(
        self,
        raw_data: dict,
    ) -> dict:

        asn = raw_data["asn"]

        network = asn.get(
            "network",
        )

        return {

            "ip": {

                "address": raw_data["ip"],

                "version": raw_data["ip_version"],

                "ptr": raw_data["ptr"],

            },

            "asn": {

                "number": asn.get("asn"),

                "registry": asn.get("asn_registry"),

                "country": asn.get("asn_country_code"),

                "description": asn.get("asn_description"),

            },

            "network": {

                "name":

                    network.get("name")

                    if network

                    else None,

                "handle":

                    network.get("handle")

                    if network

                    else None,

                "cidr":

                    network.get("cidr")

                    if network

                    else None,

                "type":

                    network.get("type")

                    if network

                    else None,

                "start_address":

                    network.get("start_address")

                    if network

                    else None,

                "end_address":

                    network.get("end_address")

                    if network

                    else None,

            },

        }