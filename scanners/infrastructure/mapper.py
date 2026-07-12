from core.models.finding import Finding


class InfrastructureMapper:

    def map(
        self,
        normalized,
    ):

        findings = []

        for key, value in normalized.items():

            if value is None:
                continue

            findings.append(

                Finding(
                    name=key.replace("_", " ").title(),
                    category="infrastructure",
                    value=str(value),
                    metadata={},
                )

            )

        return findings