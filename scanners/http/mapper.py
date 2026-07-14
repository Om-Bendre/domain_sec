from core.models.finding import Finding


class HTTPMapper:

    def map(
        self,
        normalized,
    ):

        findings = []

        for key, value in normalized.items():

            if key == "headers":
                continue

            if value is None:
                continue

            findings.append(

                Finding(
                    name=key.replace("_", " ").title(),
                    category="http",
                    value=str(value),
                    metadata={},
                )

            )

        return findings