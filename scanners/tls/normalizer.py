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

        return {

            "tls_version":

                raw_data["tls_version"],

            "cipher_suite":

                raw_data["cipher"][0],

            "cipher_protocol":

                raw_data["cipher"][1],

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

        }