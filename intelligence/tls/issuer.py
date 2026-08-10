from core.models.fact import Fact


class IssuerAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        fields = {

            "issuer_common_name":
                "issuer_common_name",

        }

        for field, name in fields.items():

            value = normalized_data.get(
                field,
            )

            if value is None:
                continue

            facts.append(

                Fact(

                    category="TLS",

                    entity="Issuer",

                    name=name,

                    value=value,

                )

            )

        return facts