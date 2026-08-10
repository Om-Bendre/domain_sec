from core.models.fact import Fact


class CSPAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        csp = normalized_data.get("csp")

        report_only = normalized_data.get(
            "csp_report_only",
        )

        #
        # Missing CSP
        #

        if not csp and not report_only:

            facts.append(

                Fact(

                    category="Security Headers",

                    entity="CSP",

                    name="present",

                    value=False,

                )

            )

            return facts

        #
        # Determine policy & mode
        #

        policy = csp or report_only

        mode = (
            "Enforced"
            if csp
            else "Report-Only"
        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="CSP",

                name="present",

                value=True,

            )

        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="CSP",

                name="mode",

                value=mode,

            )

        )

        #
        # Parse directives
        #

        directives = [

            item.strip()

            for item in policy.split(";")

            if item.strip()

        ]

        facts.append(

            Fact(

                category="Security Headers",

                entity="CSP",

                name="directive_count",

                value=len(directives),

            )

        )

        #
        # Security properties
        #

        facts.append(

            Fact(

                category="Security Headers",

                entity="CSP",

                name="has_default_src",

                value=any(

                    d.startswith("default-src")

                    for d in directives

                ),

            )

        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="CSP",

                name="unsafe_inline",

                value="'unsafe-inline'" in policy,

            )

        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="CSP",

                name="unsafe_eval",

                value="'unsafe-eval'" in policy,

            )

        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="CSP",

                name="wildcard_sources",

                value="*" in policy,

            )

        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="CSP",

                name="frame_ancestors",

                value=any(

                    d.startswith("frame-ancestors")

                    for d in directives

                ),

            )

        )

        facts.append(

            Fact(

                category="Security Headers",

                entity="CSP",

                name="upgrade_insecure_requests",

                value=any(

                    d.startswith(
                        "upgrade-insecure-requests"
                    )

                    for d in directives

                ),

            )

        )

        return facts