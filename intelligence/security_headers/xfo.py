from core.models.finding import Finding


class XFrameOptionsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        value = normalized_data.get(
            "x_frame_options",
        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="X-Frame-Options",

                name="present",

                value=value is not None,

            )

        )

        if value:

            findings.append(

                Finding(

                    category="Security Headers",

                    entity="X-Frame-Options",

                    name="value",

                    value=value,

                )

            )

        return findings