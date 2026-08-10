from core.models.fact import Fact


class TLSMapper:

    def map(
        self,
        facts: list[Fact],
    ) -> list[Fact]:

        return facts