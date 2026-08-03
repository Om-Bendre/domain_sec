from core.models.finding import Finding


class SameSiteAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> list[Finding]:

        return [

            Finding(

                category="Cookies",

                entity=cookie["name"],

                name="samesite",

                value=cookie["attributes"].get(

                    "samesite",

                ),

            )

        ]