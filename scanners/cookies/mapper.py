from core.models.finding import Finding


class CookieMapper:

    def map(
        self,
        findings: list[Finding],
    ) -> list[Finding]:

        return findings