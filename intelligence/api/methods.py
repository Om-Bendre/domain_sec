from core.models.finding import Finding


class MethodsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        allow = normalized_data.get(
            "api",
            {},
        ).get(
            "allow",
        )

        if not allow:

            return findings

        methods = [

            method.strip()

            for method

            in allow.split(",")

        ]

        for method in methods:

            findings.append(

                Finding(

                    category="API Security",

                    entity="HTTP Methods",

                    name="allowed_method",

                    value=method,

                )

            )

        return findings