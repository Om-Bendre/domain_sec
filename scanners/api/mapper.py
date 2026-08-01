from core.models.finding import Finding


class APISecurityMapper:

    def map(
        self,
        findings: list[Finding],
    ) -> list[Finding]:

        return findings