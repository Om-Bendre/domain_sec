from core.models.fact import Fact


class XContentTypeOptionsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        value = normalized_data.get(
            "x_content_type_options",
        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="X-Content-Type-Options",

                name="present",

                value=value is not None,

            )

        )

        if value:

            facts.append(

                Fact(

                    category="Security Headers",

                    entity="X-Content-Type-Options",

                    name="value",

                    value=value,

                )

            )

        return facts