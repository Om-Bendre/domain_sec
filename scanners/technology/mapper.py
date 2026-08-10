from core.models.fact import Fact


class TechnologyMapper:

    def map(
        self,
        facts: list[Fact],
    ) -> list[Fact]:

        return facts