from core.models.finding import Finding


class SecurityHeadersMapper:

    def map(
        self,
        findings: list[Finding],
    ) -> list[Finding]:

        return findings