from core.models.finding import Finding


class HTTPVersionAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        version = normalized_data.get(
            "http_version",
        )

        if not version:

            return []

        return [

            Finding(

                category="HTTP",

                entity="Protocol",

                name="http_version",

                value=version,

            )

        ]