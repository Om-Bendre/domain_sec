from core.models.finding import Finding


class CORSAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        cors = normalized_data.get(
            "cors",
            {},
        )

        mapping = {

            "origin":
                "allow_origin",

            "credentials":
                "allow_credentials",

            "headers":
                "allow_headers",

            "methods":
                "allow_methods",

            "max_age":
                "max_age",

            "expose_headers":
                "expose_headers",

        }

        for key, finding_name in mapping.items():

            value = cors.get(
                key,
            )

            if value is None:

                continue

            findings.append(

                Finding(

                    category="API Security",

                    entity="CORS",

                    name=finding_name,

                    value=value,

                )

            )

        return findings