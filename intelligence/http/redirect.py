from core.models.finding import Finding


class RedirectAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        chain = normalized_data.get(
            "redirect_chain",
            [],
        )

        findings.append(

            Finding(

                category="HTTP",

                entity="Redirect",

                name="redirect_count",

                value=len(chain),

            )

        )

        for url in chain:

            findings.append(

                Finding(

                    category="HTTP",

                    entity="Redirect",

                    name="redirect",

                    value=url,

                )

            )

        return findings