from core.models.finding import Finding


class ServerAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        server = normalized_data.get(
            "server",
        )

        if not server:

            return []

        return [

            Finding(

                category="HTTP",

                entity="Server",

                name="server",

                value=server,

            )

        ]