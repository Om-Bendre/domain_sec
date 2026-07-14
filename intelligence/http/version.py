from core.contracts.intelligence import BaseIntelligence


class HTTPVersionAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        version = normalized.get(
            "http_version"
        )

        modern = version in (

            "HTTP/2",

            "HTTP/3",

        )

        return {

            "modern_http": modern,

            "http_generation": (

                "Modern"

                if modern

                else "Legacy"

            ),

        }