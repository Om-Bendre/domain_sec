from core.models.finding import Finding


class ExpirationAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> list[Finding]:

        findings = []

        attributes = cookie["attributes"]

        if "expires" in attributes:

            findings.append(

                Finding(

                    category="Cookies",

                    entity=cookie["name"],

                    name="expires",

                    value=attributes["expires"],

                )

            )

        if "max-age" in attributes:

            findings.append(

                Finding(

                    category="Cookies",

                    entity=cookie["name"],

                    name="max_age",

                    value=attributes["max-age"],

                )

            )

        return findings