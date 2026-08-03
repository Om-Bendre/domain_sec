from core.models.finding import Finding


class InfrastructureMapper:

    def map(
        self,
        findings: list[Finding],
    ) -> list[Finding]:

        return findings