from core.models.finding import Finding


class WHOISMapper:

    def map(
        self,
        findings: list[Finding],
    ) -> list[Finding]:

        return findings