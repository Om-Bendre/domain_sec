from core.models.fact import Fact


class StatusAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

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

      

        unique_statuses = {}

        for status in statuses:

            code = str(status).strip().split()[0] if status else ""

            if code and code not in unique_statuses:

                unique_statuses[code] = str(status).strip()

        deduped = list(unique_statuses.values())

        facts.append(

            Fact(

                category="WHOIS",

                entity="Status",

                name="status_count",

                value=len(deduped),

            )

        )

        facts.append(

            Fact(

                category="WHOIS",

                entity="Status",

                name="domain_status",

                value=[

                    code for code in unique_statuses.keys()

                ],

            )

        )

        return facts