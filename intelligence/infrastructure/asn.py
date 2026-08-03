from core.models.finding import Finding


class ASNAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        asn = normalized_data.get(
            "asn",
            {},
        )

        mapping = {

            "number": "asn",

            "registry": "registry",

            "country": "country",

            "description": "description",

        }

        for field, name in mapping.items():

            value = asn.get(field)

            if value:

                findings.append(

                    Finding(

                        category="Infrastructure",

                        entity="ASN",

                        name=name,

                        value=value,

                    )

                )

        return findings