from core.models.finding import Finding


class StatusAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        statuses = normalized_data.get(
            "status",
            [],
        )

        if isinstance(
            statuses,
            str,
        ):

            statuses = [

                statuses,

            ]

        findings.append(

            Finding(

                category="WHOIS",

                entity="Status",

                name="status_count",

                value=len(statuses),

            )

        )

        # for status in statuses:

        #     findings.append(

        #         Finding(

        #             category="WHOIS",

        #             entity="Status",

        #             name="domain_status",

        #             value=status,

        #         )

        #     )

        return findings