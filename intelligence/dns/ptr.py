from core.models.finding import Finding


class PTRAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        ptr = normalized_data.get(
            "ptr",
            [],
        )

        findings.append(

            Finding(

                category="DNS",

                entity="PTR",

                name="ptr_present",

                value=bool(ptr),

            )

        )

        if not ptr:
            return findings

        

        return findings