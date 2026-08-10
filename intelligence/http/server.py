from core.models.fact import Fact


class ServerAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        server = normalized_data.get(
            "server",
        )

        if not server:

            return []

        return [

            Fact(

                category="HTTP",

                entity="Server",

                name="response_server",

                value=server,

            )

        ]