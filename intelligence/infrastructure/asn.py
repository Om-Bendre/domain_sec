from core.models.fact import Fact


class ASNAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        asn = normalized_data.get(
            "asn",
            {},
        )

        mapping = {

            "number": "asn",

            "registry": "registry",

        }

        for field, name in mapping.items():

            value = asn.get(field)

            if value:

                facts.append(

                    Fact(

                        category="Infrastructure",

                        entity="ASN",

                        name=name,

                        value=value,

                    )

                )

        return facts