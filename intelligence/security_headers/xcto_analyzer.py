from core.contracts.intelligence import BaseIntelligence


class XContentTypeOptionsAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        header = normalized_data.get(
            "x_content_type_options"
        )

        findings = {}

        if not header:

            findings["xcto_status"] = "Missing"

            return findings

        findings["xcto_status"] = "Present"

        findings["xcto_value"] = header

        if header.lower() == "nosniff":

            findings["xcto_strength"] = "Strong"

        else:

            findings["xcto_strength"] = "Weak"

        return findings