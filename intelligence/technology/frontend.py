from core.models.finding import Finding


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
    ) -> list[Finding]:

        findings = []

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

                findings.append(

                    Finding(

                        category="Technology",

                        entity="Frontend",

                        name="library",

                        value=library,

                    )

                )

        return findings