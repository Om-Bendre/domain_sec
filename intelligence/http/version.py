from core.models.fact import Fact


class HTTPVersionAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        version = normalized_data.get(
            "http_version",
        )

        if not version:

            return []

        return [

            Fact(

                category="HTTP",

                entity="Protocol",

                name="http_version",

                value=version,

            )

        ]