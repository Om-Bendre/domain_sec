from core.contracts.intelligence import BaseIntelligence


class ReferrerPolicyAnalyzer(BaseIntelligence):

    RECOMMENDED = {
        "strict-origin",
        "strict-origin-when-cross-origin",
        "same-origin",
        "no-referrer",
    }

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        header = normalized_data.get(
            "referrer_policy"
        )

        findings = {}

        if not header:

            findings["referrer_status"] = "Missing"

            return findings

        findings["referrer_status"] = "Present"

        value = header.strip().lower()

        findings["referrer_value"] = value

        if value in self.RECOMMENDED:

            findings["referrer_strength"] = "Strong"

        else:

            findings["referrer_strength"] = "Weak"

        return findings