from core.models.fact import Fact


class ExpirationAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> list[Fact]:

        facts = []

        attributes = cookie["attributes"]

        if "expires" in attributes:

            facts.append(

                Fact(

                    category="Cookies",

                    entity=cookie["name"],

                    name="expires",

                    value=attributes["expires"],

                )

            )

        if "max-age" in attributes:

            facts.append(

                Fact(

                    category="Cookies",

                    entity=cookie["name"],

                    name="max_age",

                    value=attributes["max-age"],

                )

            )

        return facts