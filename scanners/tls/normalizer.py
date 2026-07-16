class TLSNormalizer:

    def normalize(
        self,
        raw_data,
    ):

        certificate = raw_data["certificate"]

        subject = dict(

            x[0]

            for x in certificate.get(
                "subject",
                [],
            )

        )

        issuer = dict(

            x[0]

            for x in certificate.get(
                "issuer",
                [],
            )

        )

        sans = [
            value
            for key, value in certificate.get(
                "subjectAltName",
                []
            )
        ]

        return {

            "tls_version":

                raw_data["tls_version"],

            "cipher_suite":

                raw_data["cipher"][0],


            "cipher_bits":

                raw_data["cipher"][2],

            "subject_common_name":

                subject.get("commonName"),

            "issuer_common_name":

                issuer.get("commonName"),

            "valid_from":

                certificate.get("notBefore"),

            "valid_until":

                certificate.get("notAfter"),

            "serial_number":

                certificate.get("serialNumber"),

            "subject_alt_names":

                [

                    value

                    for key, value in certificate.get(
                        "subjectAltName",
                        [],
                    )

                ],

            "ocsp_urls":

                certificate.get(
                    "OCSP",
                    [],
                ),

            "ca_issuers":

                certificate.get(
                    "caIssuers",
                    [],
                ),

            "certificate_version": f"X.509 v{certificate.get('version')}",

            "issuer_organization": issuer.get("organizationName"),

            "issuer_country": issuer.get("countryName"),

            "san_count": len(sans),

            "primary_san": (
                sans[0]
                if sans
                else None
            ),

            "crl_distribution_points": certificate.get(
                "crlDistributionPoints",
                [],
            ),

            "subject_alt_names": sans,

            "ocsp_urls": list(
                certificate.get("OCSP", [])
            ),

            "ca_issuers": list(
                certificate.get("caIssuers", [])
            ),

        }