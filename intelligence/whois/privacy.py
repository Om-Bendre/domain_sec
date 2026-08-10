from core.models.fact import Fact


class PrivacyAnalyzer:

    KEYWORDS = (

        "privacy",

        "redacted",

        "proxy",

        "whoisguard",

        "gdpr",

    )

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        searchable = str(
            normalized_data,
        ).lower()

        enabled = any(

            keyword in searchable

            for keyword

            in self.KEYWORDS

        )

        facts.append(

            Fact(

                category="WHOIS",

                entity="Privacy",

                name="privacy_enabled",

                value=enabled,

            )

        )

        return facts