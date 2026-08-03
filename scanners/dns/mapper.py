from core.models.finding import Finding


class DNSMapper:

    def map(
        self,
        findings: list[Finding],
    ) -> list[Finding]:

        return findings