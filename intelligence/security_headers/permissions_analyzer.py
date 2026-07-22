from core.contracts.intelligence import BaseIntelligence


class PermissionsPolicyAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        header = normalized_data.get(
            "permissions_policy"
        )

        findings = {}

        if not header:

            findings["permissions_status"] = "Missing"

            return findings

        findings["permissions_status"] = "Present"

        directives = [
            directive.strip()
            for directive in header.split(",")
            if directive.strip()
        ]

        findings["permissions_directive_count"] = len(
            directives
        )

        findings["permissions_strength"] = (
            "Configured"
        )

        return findings