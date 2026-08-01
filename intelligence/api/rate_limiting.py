from core.models.finding import Finding


class RateLimitingAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        rate = normalized_data.get(
            "rate_limiting",
            {},
        )

        if any(rate.values()):

            findings.append(

                Finding(

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

        for key, finding_name in mapping.items():

            value = rate.get(
                key,
            )

            if value is None:

                continue

            findings.append(

                Finding(

                    category="API Security",

                    entity="Rate Limiting",

                    name=finding_name,

                    value=value,

                )

            )

        return findings