from core.models.finding import Finding


class CSPAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        csp = normalized_data.get(
            "csp",
        )

        if not csp:

            findings.append(

                Finding(

                    category="Security Headers",

                    entity="CSP",

                    name="present",

                    value=False,

                )

            )

            return findings

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

                value=normalized_data.get(
                    "csp_mode",
                ),

            )

        )

        directives = [

            item.strip()

            for item in csp.split(";")

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

        for directive in directives:

            findings.append(

                Finding(

                    category="Security Headers",

                    entity="CSP",

                    name="directive",

                    value=directive,

                )

            )

        return findings