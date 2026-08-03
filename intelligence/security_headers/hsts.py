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

        findings.append(

            Finding(

                category="Security Headers",

                entity="HSTS",

                name="present",

                value=True,

            )

        )

        directives = [

            directive.strip()

            for directive in hsts.split(";")

        ]

        for directive in directives:

            if "=" in directive:

                key, value = directive.split(

                    "=",

                    1,

                )

                findings.append(

                    Finding(

                        category="Security Headers",

                        entity="HSTS",

                        name=key.lower(),

                        value=value,

                    )

                )

            else:

                findings.append(

                    Finding(

                        category="Security Headers",

                        entity="HSTS",

                        name=directive.lower(),

                        value=True,

                    )

                )

        return findings