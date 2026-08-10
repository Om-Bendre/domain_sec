from core.models.fact import Fact


class MethodsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        allow = normalized_data.get(
            "api",
            {},
        ).get(
            "allow",
        )

        if not allow:

            return facts

        methods = [

            method.strip()

            for method

            in allow.split(",")

        ]

        for method in methods:

            facts.append(

                Fact(

                    category="API Security",

                    entity="HTTP Methods",

                    name="allowed_method",

                    value=method,

                )

            )

        return facts