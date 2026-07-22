from core.contracts.intelligence import BaseIntelligence


class XFrameOptionsAnalyzer(BaseIntelligence):

    VALID_VALUES = {
        "deny",
        "sameorigin",
    }

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        header = normalized_data.get(
            "x_frame_options"
        )

        findings = {}

        if not header:

            findings["xfo_status"] = "Missing"
            return findings

        findings["xfo_status"] = "Present"

        value = header.strip().lower()

        findings["xfo_value"] = value

        if value in self.VALID_VALUES:

            findings["xfo_strength"] = "Strong"

        else:

            findings["xfo_strength"] = "Weak"

        return findings