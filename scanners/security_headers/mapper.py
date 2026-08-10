from core.models.fact import Fact


class SecurityHeadersMapper:

    def map(
        self,
        facts: list[Fact],
    ) -> list[Fact]:

        return facts