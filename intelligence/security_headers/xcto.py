from core.models.finding import Finding


class XContentTypeOptionsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        value = normalized_data.get(
            "x_content_type_options",
        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="X-Content-Type-Options",

                name="present",

                value=value is not None,

            )

        )

        if value:

            findings.append(

                Finding(

                    category="Security Headers",

                    entity="X-Content-Type-Options",

                    name="value",

                    value=value,

                )

            )

        return findings