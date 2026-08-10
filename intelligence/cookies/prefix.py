from core.models.fact import Fact


class PrefixAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> list[Fact]:

        facts = []

        name = cookie["name"]

        if name.startswith("__Host-"):

            facts.append(

                Fact(

                    category="Cookies",

                    entity=name,

                    name="prefix",

                    value="__Host-",

                )

            )

        elif name.startswith("__Secure-"):

            facts.append(

                Fact(

                    category="Cookies",

                    entity=name,

                    name="prefix",

                    value="__Secure-",

                )

            )

        return facts