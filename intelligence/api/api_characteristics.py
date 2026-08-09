from core.models.finding import Finding


class APICharacteristicsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        body = normalized_data.get(
            "body",
            "",
        ).lower()

        content_type = normalized_data.get(
            "api",
            {},
        ).get(
            "content_type",
            "",
        ).lower()

        #
        # JSON API
        #

        if "application/json" in content_type:

            findings.append(

                Finding(

                    category="API Security",

                    entity="API Characteristics",

                    name="response_type",

                    value="JSON",

                )

            )

 

        if any(

            keyword in body

            for keyword in (

                "graphql",

                "__schema",

                "__type",

            )

        ):

            findings.append(

                Finding(

                    category="API Security",

                    entity="API Characteristics",

                    name="api_style",

                    value="GraphQL",

                )

            )

        #
        # SOAP
        #

        if any(

            keyword in body

            for keyword in (

                "<soap",

                "soapenv",

                "soap:",

            )

        ):

            findings.append(

                Finding(

                    category="API Security",

                    entity="API Characteristics",

                    name="api_style",

                    value="SOAP",

                )

            )

        #
        # REST
        #

        if "application/json" in content_type:

            findings.append(

                Finding(

                    category="API Security",

                    entity="API Characteristics",

                    name="api_style",

                    value="REST",

                )

            )

        return findings