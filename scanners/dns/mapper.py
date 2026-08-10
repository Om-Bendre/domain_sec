from core.models.fact import Fact


class DNSMapper:

    def map(
        self,
        facts: list[Fact],
    ) -> list[Fact]:

        return facts