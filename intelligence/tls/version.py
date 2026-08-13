from core.models.fact import Fact


class VersionAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        version = normalized_data.get(
             "tls_version",
        
        )

        facts.append(

            Fact(

                category="TLS",

                entity="TLS version",

                name="TLS version",

                value=version,

            )

        )

        return facts
