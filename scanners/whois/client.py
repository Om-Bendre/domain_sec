import whois


class WHOISClient:

    def query(
        self,
        domain: str,
    ) -> dict:

        result = whois.whois(
            domain,
        )

        return {

            "domain_name":
                result.get(
                    "domain_name",
                ),

            "registrar":
                result.get(
                    "registrar",
                ),

            "registrar_url":
                result.get(
                    "registrar_url",
                ),

            "registrar_iana_id":
                result.get(
                    "registrar_iana_id",
                ),

            "creation_date":
                result.get(
                    "creation_date",
                ),

            "updated_date":
                result.get(
                    "updated_date",
                ),

            "expiration_date":
                result.get(
                    "expiration_date",
                ),

            "status":
                result.get(
                    "status",
                    [],
                ),

            "name_servers":
                result.get(
                    "name_servers",
                    [],
                ),

            "dnssec":
                result.get(
                    "dnssec",
                ),

            "registrant_name":
                result.get(
                    "name",
                ),

            "registrant_organization":
                result.get(
                    "org",
                ),

            "registrant_email":
                result.get(
                    "email",
                ),

            "registrant_country":
                result.get(
                    "country",
                ),

            "registrant_city":
                result.get(
                    "city",
                ),

            "registrant_state":
                result.get(
                    "state",
                ),

            "registrant_postal_code":
                result.get(
                    "zipcode",
                ),

            "registrant_address":
                result.get(
                    "address",
                ),

            "abuse_email":
                result.get(
                    "abuse_contact_email",
                ),

            "abuse_phone":
                result.get(
                    "abuse_contact_phone",
                ),

        }