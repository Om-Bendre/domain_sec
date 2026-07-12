from core.contracts.intelligence import BaseIntelligence

class PTRAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        ptr = normalized.get("ptr")

        if not ptr:

            return {

                "reverse_dns": None,

                "ptr_available": False,

            }

        return {

            "reverse_dns": ptr,

            "ptr_available": True,

        }