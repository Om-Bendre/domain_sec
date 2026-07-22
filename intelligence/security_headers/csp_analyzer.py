from core.contracts.intelligence import BaseIntelligence


class CSPAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        header = normalized_data.get(
            "csp"
        )

        findings = {}

        #
        # Header Missing
        #

        if not header:

            findings["csp_status"] = "Missing"

            return findings

        findings["csp_status"] = "Present"

        policy = header.lower()

        #
        # Unsafe Inline
        #

        findings["unsafe_inline"] = (
            "'unsafe-inline'" in policy
        )

        #
        # Unsafe Eval
        #

        findings["unsafe_eval"] = (
            "'unsafe-eval'" in policy
        )

        #
        # Wildcard
        #

        findings["wildcard_sources"] = (
            "*" in policy
        )

        #
        # Overall Strength
        #

        if (
            findings["unsafe_inline"]
            or findings["unsafe_eval"]
            or findings["wildcard_sources"]
        ):

            findings["csp_strength"] = "Weak"

        else:

            findings["csp_strength"] = "Strong"

        return findings