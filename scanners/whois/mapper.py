from core.models.fact import Fact


class WHOISMapper:

    def map(
        self,
        facts: list[Fact],
    ) -> list[Fact]:

        return facts