from core.models.fact import Fact


class ServerAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        server = normalized_data.get(
            "headers",
            {},
        ).get(
            "server"
        )

        if not server:
            return []

        return [
            Fact(
                category="Technology",
                entity="Server",
                name="detected_server",
                value=server,
            )
        ]