from core.models.finding import Finding


class AuthenticationMapper:

    def map(
        self,
        findings: list[Finding],
    ) -> list[Finding]:

        unique_findings = []

        seen = set()

        for finding in findings:

            key = (
                finding.category,
                finding.entity,
                finding.name,
                finding.value,
            )

            if key in seen:
                continue

            seen.add(key)

            unique_findings.append(
                finding
            )

        return unique_findings