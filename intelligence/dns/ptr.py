from core.models.fact import Fact


class PTRAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        ptr = normalized_data.get(
            "ptr",
            [],
        )

        facts.append(

            Fact(

                category="DNS",

                entity="PTR",

                name="ptr_present",

                value=bool(ptr),

            )

        )

        if not ptr:
            return facts

        

        return facts