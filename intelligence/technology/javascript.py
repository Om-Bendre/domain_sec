from core.models.fact import Fact


JAVASCRIPT_FRAMEWORKS = {

    "react": "React",

    "react-dom": "React",

    "_next": "Next.js",

    "__next": "Next.js",

    "vue": "Vue.js",

    "__nuxt": "Nuxt.js",

    "angular": "Angular",

    "ng-": "Angular",

    "svelte": "Svelte",

    "astro": "Astro",

    "solid": "SolidJS",

    "preact": "Preact",

}


class JavaScriptAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        html = normalized_data.get(
            "html",
            "",
        ).lower()

        scripts = " ".join(
            normalized_data.get(
                "scripts",
                [],
            )
        ).lower()

        searchable = html + scripts

        for key, framework in JAVASCRIPT_FRAMEWORKS.items():

            if key in searchable:

                facts.append(

                    Fact(

                        category="Technology",

                        entity="JavaScript",

                        name="framework",

                        value=framework,

                    )

                )

        return facts