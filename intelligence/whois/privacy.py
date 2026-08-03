from core.models.finding import Finding


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
    ) -> list[Finding]:

        findings = []

        searchable = str(
            normalized_data,
        ).lower()

        enabled = any(

            keyword in searchable

            for keyword

            in self.KEYWORDS

        )

        findings.append(

            Finding(

                category="WHOIS",

                entity="Privacy",

                name="privacy_enabled",

                value=enabled,

            )

        )

        return findings