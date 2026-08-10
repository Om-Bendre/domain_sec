from core.models.fact import Fact


class HttpOnlyAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> list[Fact]:

        return [

            Fact(

                category="Cookies",

                entity=cookie["name"],

                name="httponly",

                value="httponly" in cookie["attributes"],

            )

        ]