from core.models.fact import Fact


class APICharacteristicsAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

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

            facts.append(

                Fact(

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

            facts.append(

                Fact(

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

            facts.append(

                Fact(

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

            facts.append(

                Fact(

                    category="API Security",

                    entity="API Characteristics",

                    name="api_style",

                    value="REST",

                )

            )

        return facts