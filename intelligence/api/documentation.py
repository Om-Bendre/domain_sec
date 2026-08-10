from core.models.fact import Fact


DOCUMENTATION_PATTERNS = {

    "swagger": "Swagger",

    "swagger-ui": "Swagger UI",

    "swagger.json": "Swagger Specification",

    "openapi": "OpenAPI",

    "openapi.json": "OpenAPI Specification",

    "redoc": "ReDoc",

    "/docs": "API Documentation",

    "/api-docs": "API Documentation",

    "graphql playground": "GraphQL Playground",

    "graphiql": "GraphiQL",

}


class DocumentationAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        body = normalized_data.get(
            "documentation",
            {},
        ).get(
            "body",
            "",
        )

        for pattern, name in DOCUMENTATION_PATTERNS.items():

            if pattern in body:

                facts.append(

                    Fact(

                        category="API Security",

                        entity="Documentation",

                        name="documentation_exposed",

                        value=name,

                    )

                )

        return facts