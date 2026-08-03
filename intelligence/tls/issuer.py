from core.models.finding import Finding


class IssuerAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        fields = {

            "issuer_common_name":
                "issuer_common_name",

            "issuer_organization":
                "issuer_organization",

            "issuer_country":
                "issuer_country",

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

                    entity="Issuer",

                    name=name,

                    value=value,

                )

            )

        return findings