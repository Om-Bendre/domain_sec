from core.models.finding import Finding


class CertificateAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        fields = {

            "subject_common_name":
                "subject_common_name",

            "serial_number":
                "serial_number",

            "certificate_version":
                "certificate_version",

            "san_count":
                "san_count",

            "primary_san":
                "primary_san",

            "subject_alt_names":
                "subject_alt_names",

            "public_key_algorithm":
                "public_key_algorithm",

            "public_key_size":
                "public_key_size",

            "signature_algorithm":
                "signature_algorithm",

            "certificate_fingerprint":
                "certificate_fingerprint",

        }

        for field, name in fields.items():

            value = normalized_data.get(
                field,
            )

            if value is None:
                continue

            findings.append(

                Finding(

                    category="TLS",

                    entity="Certificate",

                    name=name,

                    value=value,

                )

            )

        return findings