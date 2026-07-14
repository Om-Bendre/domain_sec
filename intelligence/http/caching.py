from core.contracts.intelligence import BaseIntelligence


class CacheAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        cache = normalized.get(
            "cache_control"
        )

        if cache is None:

            policy = "Unknown"

        elif "no-store" in cache.lower():

            policy = "No Store"

        elif "no-cache" in cache.lower():

            policy = "No Cache"

        elif "private" in cache.lower():

            policy = "Private"

        elif "public" in cache.lower():

            policy = "Public"

        else:

            policy = "Custom"

        return {

            "cache_enabled": cache is not None,

            "cache_policy": policy,

        }