from core.models.finding import Finding


class RecordsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        records = normalized_data.get(
            "records",
            {},
        )

        for record_type, values in records.items():

            if not values:
                continue

            findings.append(

                Finding(

                    category="DNS",

                    entity=record_type,

                    name=f"{record_type.lower()}_records",

                    value=len(values),

                )

            )

            for value in values:

                findings.append(

                    Finding(

                        category="DNS",

                        entity=record_type,

                        name=record_type.lower(),

                        value=value,

                    )

                )

        return findings