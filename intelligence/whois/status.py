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

        facts.append(

            Fact(

                category="WHOIS",

                entity="Status",

                name="status_count",

                value=len(statuses),

            )

        )

        # for status in statuses:

        #     facts.append(

        #         Fact(

        #             category="WHOIS",

        #             entity="Status",

        #             name="domain_status",

        #             value=status,

        #         )

        #     )

        return facts