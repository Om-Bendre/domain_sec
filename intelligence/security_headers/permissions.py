from core.models.fact import Fact


class PermissionsPolicyAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        policy = normalized_data.get(
            "permissions_policy",
        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="Permissions-Policy",

                name="present",

                value=policy is not None,

            )

        )

        if not policy:

            return facts

        directives = [

            item.strip()

            for item in policy.split(",")

            if item.strip()

        ]

        facts.append(

            Fact(

                category="Security Headers",

                entity="Permissions-Policy",

                name="directive_count",

                value=len(directives),

            )

        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="Permissions-Policy",

                name="uses_wildcard",

                value="*" in policy,

            )

        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="Permissions-Policy",

                name="uses_self",

                value="'self'" in policy,

            )

        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="Permissions-Policy",

                name="uses_none",

                value="()" in policy,

            )

        )

        return facts