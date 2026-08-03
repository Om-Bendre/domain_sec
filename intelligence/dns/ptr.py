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

        if not ptr:

            return findings

        findings.append(

            Finding(

                category="DNS",

                entity="PTR",

                name="ptr_present",

                value=True,

            )

        )

        for hostname in ptr:

            findings.append(

                Finding(

                    category="DNS",

                    entity="PTR",

                    name="ptr_hostname",

                    value=hostname,

                )

            )

        return findings