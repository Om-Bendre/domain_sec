from core.models.finding import Finding


class HSTSAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        hsts = normalized_data.get(
            "hsts",
        )

        #
        # HSTS Missing
        #

        if not hsts:

            findings.append(

                Finding(

                    category="Security Headers",

                    entity="HSTS",

                    name="present",

                    value=False,

                )

            )

            return findings

        #
        # HSTS Present
        #

        findings.append(

            Finding(

                category="Security Headers",

                entity="HSTS",

                name="present",

                value=True,

            )

        )

        #
        # Parse directives
        #

        max_age = None

        include_subdomains = False

        preload = False

        directives = [

            directive.strip()

            for directive in hsts.split(";")

            if directive.strip()

        ]

        for directive in directives:

            lower = directive.lower()

            if lower.startswith("max-age="):

                try:

                    max_age = int(

                        directive.split("=")[1]

                    )

                except ValueError:

                    pass

            elif lower == "includesubdomains":

                include_subdomains = True

            elif lower == "preload":

                preload = True

        #
        # Findings
        #

        findings.append(

            Finding(

                category="Security Headers",

                entity="HSTS",

                name="max_age",

                value=max_age,

            )

        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="HSTS",

                name="include_subdomains",

                value=include_subdomains,

            )

        )

        findings.append(

            Finding(

                category="Security Headers",

                entity="HSTS",

                name="preload",

                value=preload,

            )

        )

        return findings