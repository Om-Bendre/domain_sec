from core.models.finding import Finding


class ContentAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        content_type = normalized_data.get(
            "content_type",
        )

        if content_type:

            findings.append(

                Finding(

                    category="HTTP",

                    entity="Content",

                    name="content_type",

                    value=content_type,

                )

            )

        content_length = normalized_data.get(
            "headers",
            {},
        ).get(
            "Content-Length",
        )

        if content_length:

            findings.append(

                Finding(

                    category="HTTP",

                    entity="Content",

                    name="content_length",

                    value=content_length,

                )

            )

        return findings