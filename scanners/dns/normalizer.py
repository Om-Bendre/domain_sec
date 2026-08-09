class DNSNormalizer:

    def normalize(
        self,
        raw_data: dict,
    ) -> dict:

        return {

            "records": {

                "A": raw_data.get("A", []),

                "AAAA": raw_data.get("AAAA", []),

                "MX": raw_data.get("MX", []),

                "TXT": raw_data.get("TXT", []),

                "CAA": raw_data.get("CAA", []),

                "CNAME": raw_data.get("CNAME", []),

                "PTR": raw_data.get("PTR", []),

            },

            "dnssec": {

                "enabled": raw_data.get(
                    "dnssec_enabled",
                    False,
                ),

                "dnskeys": raw_data.get(
                    "dnskeys",
                    [],
                ),

                "ds": raw_data.get(
                    "ds_records",
                    [],
                ),

            },

            "mail": {

                "mx": raw_data.get(
                    "MX",
                    [],
                ),

                "txt": raw_data.get(
                    "TXT",
                    [],
                ),

            },

            "nameservers": raw_data.get(
                "NS",
                [],
            ),

            "ptr": raw_data.get(
                "PTR",
                [],
            ),

        }