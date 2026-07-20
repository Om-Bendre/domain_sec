from core.models.finding import Finding


class TLSMapper:

    SKIP_FIELDS = {
        "subject_alt_names",
    }

    def map(
        self,
        normalized,
    ):

        findings = []

        for key, value in normalized.items():

            if key in self.SKIP_FIELDS:
                continue

            if value is None:
                continue

            findings.append(

                Finding(
                    name=key.replace("_", " ").title(),
                    category="tls",
                    value=str(value),
                    metadata={},
                )

            )

        return findings