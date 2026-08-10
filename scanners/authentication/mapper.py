from core.models.fact import Fact


class AuthenticationMapper:

    def map(
        self,
        facts: list[Fact],
    ) -> list[Fact]:

        unique_facts = []

        seen = set()

        for fact in facts:

            key = (
                fact.category,
                fact.entity,
                fact.name,
                fact.value,
            )

            if key in seen:
                continue

            seen.add(key)

            unique_facts.append(
                fact
            )

        return unique_facts