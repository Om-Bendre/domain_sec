from core.models.fact import Fact


class CompressionAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        encoding = normalized_data.get(
            "content_encoding",
        )

        if not encoding:

            return []

        return [

            Fact(

                category="HTTP",

                entity="Compression",

                name="content_encoding",

                value=encoding,

            )

        ]