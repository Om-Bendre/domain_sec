from core.models.fact import Fact


class APISecurityMapper:

    def map(
        self,
        facts: list[Fact],
    ) -> list[Fact]:

        return facts