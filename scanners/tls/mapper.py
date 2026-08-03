from core.models.finding import Finding


class TLSMapper:

    def map(
        self,
        findings: list[Finding],
    ) -> list[Finding]:

        return findings