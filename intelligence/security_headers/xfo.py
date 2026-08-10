from core.models.fact import Fact


class XFrameOptionsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        value = normalized_data.get(
            "x_frame_options",
        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="X-Frame-Options",

                name="present",

                value=value is not None,

            )

        )

        if value:

            facts.append(

                Fact(

                    category="Security Headers",

                    entity="X-Frame-Options",

                    name="value",

                    value=value,

                )

            )

        return facts