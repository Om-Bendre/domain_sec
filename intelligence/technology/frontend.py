from core.models.fact import Fact


FRONTEND_LIBRARIES = {

    "bootstrap": "Bootstrap",

    "tailwind": "Tailwind CSS",

    "bulma": "Bulma",

    "foundation": "Foundation",

    "material": "Material UI",

    "semantic-ui": "Semantic UI",

}


class FrontendAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        css = " ".join(

            normalized_data.get(

                "stylesheets",

                [],

            )

        ).lower()

        html = normalized_data.get(

            "html",

            "",

        ).lower()

        searchable = css + html

        for key, library in FRONTEND_LIBRARIES.items():

            if key in searchable:

                facts.append(

                    Fact(

                        category="Technology",

                        entity="Frontend",

                        name="library",

                        value=library,

                    )

                )

        return facts