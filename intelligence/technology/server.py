from core.models.finding import Finding


class ServerAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        server = normalized_data.get(

            "headers",

            {},

        ).get(

            "Server"

        )

        if server:

            findings.append(

                Finding(

                    category="Technology",

                    entity="Server",

                    name="detected_server",

                    value=server,

                )

            )

        return findings