from core.contracts.intelligence import BaseIntelligence


class RedirectAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        count = normalized.get(
            "redirect_count",
            0,
        )

        chain = normalized.get(
            "redirect_chain",
            [],
        )

        return {

            "redirects_present": count > 0,

            "redirect_type": (
                "Redirected"
                if count > 0
                else "Direct"
            ),

            "final_destination": (
                chain[-1]
                if chain
                else normalized.get("final_url")
            ),

        }