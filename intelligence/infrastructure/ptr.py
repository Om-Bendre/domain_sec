from core.models.finding import Finding


class PTRAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        ptr = normalized_data.get(
            "ip",
            {},
        ).get(
            "ptr",
        )

        if not ptr:

            return []

        return [

            Finding(

                category="Infrastructure",

                entity="PTR",

                name="hostname",

                value=ptr,

            )

        ]