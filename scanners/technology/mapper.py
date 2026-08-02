from core.models.finding import Finding


class TechnologyMapper:

    def map(
        self,
        findings: list[Finding],
    ) -> list[Finding]:

        return findings