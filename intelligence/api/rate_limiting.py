from core.models.fact import Fact


class RateLimitingAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        rate = normalized_data.get(
            "rate_limiting",
            {},
        )

        if any(rate.values()):

            facts.append(

                Fact(

                    category="API Security",

                    entity="Rate Limiting",

                    name="rate_limiting_present",

                    value=True,

                )

            )

        mapping = {

            "limit":

                "limit",

            "remaining":

                "remaining",

            "reset":

                "reset",

            "retry_after":

                "retry_after",

        }

        for key, Fact_name in mapping.items():

            value = rate.get(
                key,
            )

            if value is None:

                continue

            facts.append(

                Fact(

                    category="API Security",

                    entity="Rate Limiting",

                    name=Fact_name,

                    value=value,

                )

            )

        return facts