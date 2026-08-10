from core.models.fact import Fact


BACKENDS = {

    "php": "PHP",

    "django": "Python",

    "flask": "Python",

    "fastapi": "Python",

    "gunicorn": "Python",

    "uvicorn": "Python",

    "express": "Node.js",

    "node": "Node.js",

    "asp.net": ".NET",

    "kestrel": ".NET",

    "spring": "Java",

    "tomcat": "Java",

    "jetty": "Java",

    "go": "Go",

}


class BackendAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        headers = str(

            normalized_data.get(

                "headers",

                {},

            )

        ).lower()

        html = normalized_data.get(

            "html",

            "",

        ).lower()

        searchable = headers + html

        for key, backend in BACKENDS.items():

            if key in searchable:

                facts.append(

                    Fact(

                        category="Technology",

                        entity="Backend",

                        name="technology",

                        value=backend,

                    )

                )

        return facts