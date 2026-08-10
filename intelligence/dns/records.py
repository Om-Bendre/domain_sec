from core.models.fact import Fact


class RecordsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        records = normalized_data.get(
            "records",
            {},
        )

        for record_type, values in records.items():

            if not values:
                continue

            facts.append(

                Fact(

                    category="DNS",

                    entity=record_type,

                    name=f"{record_type.lower()}_count",

                    value=len(values),

                )

            )

        return facts