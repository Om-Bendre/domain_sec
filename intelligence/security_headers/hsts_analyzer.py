from core.contracts.intelligence import BaseIntelligence


class HSTSAnalyzer(BaseIntelligence):

    RECOMMENDED_MAX_AGE = 31536000

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        header = normalized_data.get(
            "hsts"
        )

        findings = {}

        #
        # Header Missing
        #

        if not header:

            findings["hsts_status"] = "Missing"

            return findings

        #
        # Header Present
        #

        findings["hsts_status"] = "Present"

        directives = {}

        for directive in header.split(";"):

            directive = directive.strip()

            if "=" in directive:

                key, value = directive.split(
                    "=",
                    1,
                )

                directives[
                    key.lower()
                ] = value

            else:

                directives[
                    directive.lower()
                ] = True

        #
        # max-age
        #

        max_age = directives.get(
            "max-age"
        )

        if max_age:

            findings["hsts_max_age"] = max_age

            try:

                max_age = int(max_age)

                if max_age >= self.RECOMMENDED_MAX_AGE:

                    findings[
                        "hsts_strength"
                    ] = "Strong"

                else:

                    findings[
                        "hsts_strength"
                    ] = "Weak"

            except ValueError:

                findings[
                    "hsts_strength"
                ] = "Invalid"

        #
        # includeSubDomains
        #

        findings[
            "hsts_include_subdomains"
        ] = (
            "includeSubDomains"
            in header
        )

        #
        # preload
        #

        findings[
            "hsts_preload"
        ] = (
            "preload"
            in header
        )

        return findings