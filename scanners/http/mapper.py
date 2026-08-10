from core.models.fact import Fact


class HTTPMapper:

    def map(
        self,
        facts: list[Fact],
    ) -> list[Fact]:

        return facts