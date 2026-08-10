from core.models.fact import Fact


class SameSiteAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> list[Fact]:

        return [

            Fact(

                category="Cookies",

                entity=cookie["name"],

                name="samesite",

                value=cookie["attributes"].get(

                    "samesite",

                ),

            )

        ]