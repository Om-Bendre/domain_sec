from core.models.finding import Finding


class CacheAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        cache = normalized_data.get(
            "cache_control",
        )

        if not cache:

            return []

        return [

            Finding(

                category="HTTP",

                entity="Caching",

                name="cache_control",

                value=cache,

            )

        ]