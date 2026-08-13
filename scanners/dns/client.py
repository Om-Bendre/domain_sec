import dns.resolver
import dns.reversename


class DNSClient:

    def query(
        self,
        domain: str,
        configuration,
    ) -> dict:

        resolver = dns.resolver.Resolver()

        resolver.nameservers = [
            configuration.resolver,
        ]

        record_types = [
            "A",
            "AAAA",
            "MX",
            "NS",
            "TXT",
            "CAA",
            "CNAME",
        ]

        raw = {}

        #
        # DNS Records
        #

        for record_type in record_types:

            try:

                answer = resolver.resolve(
                    domain,
                    record_type,
                )

                raw[record_type] = [
                    self._decode_record(record, record_type)
                    for record in answer
                ]

            except Exception:

                raw[record_type] = []

        #
        # DNSSEC - DNSKEY
        #

        try:

            dnskeys = resolver.resolve(
                domain,
                "DNSKEY",
            )

            raw["dnssec_enabled"] = True

            raw["dnskeys"] = [
                str(key)
                for key in dnskeys
            ]

        except Exception:

            raw["dnssec_enabled"] = False
            raw["dnskeys"] = []

        #
        # DNSSEC - DS
        #

        try:

            ds = resolver.resolve(
                domain,
                "DS",
            )

            raw["ds_records"] = [
                str(record)
                for record in ds
            ]

        except Exception:

            raw["ds_records"] = []

        #
        # DMARC
        #

        try:

            dmarc_answer = resolver.resolve(
                f"_dmarc.{domain}",
                "TXT",
            )

            raw["DMARC"] = [
                self._decode_record(record, "TXT")
                for record in dmarc_answer
            ]

        except Exception:

            raw["DMARC"] = []

        #
        # PTR
        #

        raw["PTR"] = []

        for ip in raw.get(
            "A",
            [],
        ):

            try:

                reverse = (
                    dns.reversename.from_address(
                        ip,
                    )
                )

                answer = resolver.resolve(
                    reverse,
                    "PTR",
                )

                raw["PTR"].extend(
                    [
                        str(record)
                        for record in answer
                    ]
                )

            except Exception:

                pass

        return raw

    @staticmethod
    def _decode_record(record, record_type: str) -> str:
        

        if record_type == "TXT":

            try:

                return b"".join(record.strings).decode("utf-8")

            except Exception:

                return str(record).strip('"')

        return str(record)