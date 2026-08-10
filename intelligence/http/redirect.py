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

        # for url in chain:

        #     facts.append(

        #         Fact(

        #             category="HTTP",

        #             entity="Redirect",

        #             name="redirect",

        #             value=url,

        #         )

        #     )

        return facts