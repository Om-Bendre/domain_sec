from core.models.finding import Finding


class CompressionAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        encoding = normalized_data.get(
            "content_encoding",
        )

        if not encoding:

            return []

        return [

            Finding(

                category="HTTP",

                entity="Compression",

                name="content_encoding",

                value=encoding,

            )

        ]