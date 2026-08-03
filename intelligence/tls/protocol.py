from core.models.finding import Finding


class ProtocolAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        protocol = normalized_data.get(
            "protocol",
        )

        if not protocol:

            return []

        return [

            Finding(

                category="TLS",

                entity="Protocol",

                name="tls_version",

                value=protocol,

            )

        ]