from core.models.finding import Finding


class ReferrerPolicyAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        value = normalized_data.get(
            "referrer_policy",
        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="Referrer-Policy",

                name="present",

                value=value is not None,

            )

        )

        if value:

            findings.append(

                Finding(

                    category="Security Headers",

                    entity="Referrer-Policy",

                    name="value",

                    value=value,

                )

            )

        return findings