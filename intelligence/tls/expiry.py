from core.models.fact import Fact


class ExpiryAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        valid_from = normalized_data.get(
            "valid_from",
        )

        valid_until = normalized_data.get(
            "valid_until",
        )

        if valid_from:

            facts.append(

                Fact(

                    category="TLS",

                    entity="Certificate",

                    name="valid_from",

                    value=valid_from,

                )

            )

        if valid_until:

            facts.append(

                Fact(

                    category="TLS",

                    entity="Certificate",

                    name="valid_until",

                    value=valid_until,

                )

            )

        return facts