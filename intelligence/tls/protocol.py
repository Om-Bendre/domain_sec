from core.contracts.intelligence import BaseIntelligence


class ProtocolAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        version = normalized.get(
            "tls_version",
            "",
        )

        modern = version in (
            "TLSv1.3",
            "TLSv1.2",
        )

        return {

            "protocol_category": (

                "Modern"

                if modern

                else "Legacy"

            ),

        }