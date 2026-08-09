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
                [],
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

            "certificate_version":
                f"X.509 v{certificate.get('version')}",

            "san_count":
                len(sans),

            "primary_san":
                sans[0] if sans else None,


            # Cryptography Fields 

            "public_key_algorithm":
                raw_data.get(
                    "public_key_algorithm"
                ),

            "public_key_size":
                raw_data.get(
                    "public_key_size"
                ),

            "signature_algorithm":
                raw_data.get(
                    "signature_algorithm"
                ),

            "certificate_fingerprint":
                raw_data.get(
                    "certificate_fingerprint"
                ),

        }