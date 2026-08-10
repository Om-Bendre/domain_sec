from core.models.fact import Fact


class ReferrerPolicyAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        value = normalized_data.get(
            "referrer_policy",
        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="Referrer-Policy",

                name="present",

                value=value is not None,

            )

        )

        if value:

            facts.append(

                Fact(

                    category="Security Headers",

                    entity="Referrer-Policy",

                    name="value",

                    value=value,

                )

            )

        return facts