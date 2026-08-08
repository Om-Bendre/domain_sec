from core.models.finding import Finding


class PermissionsPolicyAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        policy = normalized_data.get(
            "permissions_policy",
        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="Permissions-Policy",

                name="present",

                value=policy is not None,

            )

        )

        if not policy:

            return findings

        directives = [

            item.strip()

            for item in policy.split(",")

            if item.strip()

        ]

        findings.append(

            Finding(

                category="Security Headers",

                entity="Permissions-Policy",

                name="directive_count",

                value=len(directives),

            )

        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="Permissions-Policy",

                name="uses_wildcard",

                value="*" in policy,

            )

        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="Permissions-Policy",

                name="uses_self",

                value="'self'" in policy,

            )

        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="Permissions-Policy",

                name="uses_none",

                value="()" in policy,

            )

        )

        return findings