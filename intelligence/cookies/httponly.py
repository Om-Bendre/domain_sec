from core.models.finding import Finding


class HttpOnlyAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> list[Finding]:

        return [

            Finding(

                category="Cookies",

                entity=cookie["name"],

                name="httponly",

                value="httponly" in cookie["attributes"],

            )

        ]