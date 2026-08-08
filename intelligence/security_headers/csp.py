from core.models.finding import Finding


class CSPAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        csp = normalized_data.get("csp")

        report_only = normalized_data.get(
            "csp_report_only",
        )

        #
        # Missing CSP
        #

        if not csp and not report_only:

            findings.append(

                Finding(

                    category="Security Headers",

                    entity="CSP",

                    name="present",

                    value=False,

                )

            )

            return findings

        #
        # Determine policy & mode
        #

        policy = csp or report_only

        mode = (
            "Enforced"
            if csp
            else "Report-Only"
        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="CSP",

                name="present",

                value=True,

            )

        )

        findings.append(

            Finding(

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

        findings.append(

            Finding(

                category="Security Headers",

                entity="CSP",

                name="directive_count",

                value=len(directives),

            )

        )

        #
        # Security properties
        #

        findings.append(

            Finding(

                category="Security Headers",

                entity="CSP",

                name="has_default_src",

                value=any(

                    d.startswith("default-src")

                    for d in directives

                ),

            )

        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="CSP",

                name="unsafe_inline",

                value="'unsafe-inline'" in policy,

            )

        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="CSP",

                name="unsafe_eval",

                value="'unsafe-eval'" in policy,

            )

        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="CSP",

                name="wildcard_sources",

                value="*" in policy,

            )

        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="CSP",

                name="frame_ancestors",

                value=any(

                    d.startswith("frame-ancestors")

                    for d in directives

                ),

            )

        )

        findings.append(

            Finding(

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

        return findings