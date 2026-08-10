from core.models.fact import Fact


class ServerAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        server = normalized_data.get(

            "headers",

            {},

        ).get(

            "Server"

        )

        if server:

            facts.append(

                Fact(

                    category="Technology",

                    entity="Server",

                    name="detected_server",

                    value=server,

                )

            )

        return facts