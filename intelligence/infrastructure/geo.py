from core.models.finding import Finding


class GeoAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        geo = normalized_data.get(
            "geo",
            {},
        )

        for field, value in geo.items():

            if value is None:

                continue

            findings.append(

                Finding(

                    category="Infrastructure",

                    entity="Geo",

                    name=field,

                    value=value,

                )

            )

        return findings