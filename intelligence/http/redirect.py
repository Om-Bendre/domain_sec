from core.models.fact import Fact


class RedirectAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        chain = normalized_data.get(
            "redirect_chain",
            [],
        )

        facts.append(

            Fact(
                category="HTTP",
                entity="Redirect",
                name="redirect_count",
                value=len(chain),
            )
        )

        facts.append(
            Fact(
                category="HTTP",
                entity="Response",
                name="initial_status",
                value=normalized_data.get(
                    "initial_status"
                ),
            )
        )

        facts.append(
            Fact(
                category="HTTP",
                entity="Response",
                name="final_status",
                value=normalized_data.get(
                    "final_status"
                ),
            )
        )

        facts.append(
            Fact(
                category="HTTP",
                entity="Response",
                name="final_url",
                value=normalized_data.get(
                    "final_url"
                ),
            )
        )

        facts.append(
            Fact(
                category="HTTP",
                entity="Redirect",
                name="redirect_statuses",
                value=normalized_data.get(
                    "redirect_statuses",
                    [],
                ),
            )
        )



        return facts