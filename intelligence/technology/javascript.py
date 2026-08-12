from core.models.fact import Fact


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

        inline_scripts = " ".join(
            normalized_data.get(
                "inline_scripts",
                [],
            )
        ).lower()

        attributes = normalized_data.get(
            "html_attributes",
            [],
        )

        searchable = (
            html
            + scripts
            + inline_scripts
        )

        detections = set()

        if (
            "react-dom" in searchable
            or "react.production" in searchable
            or "react.development" in searchable
            or "data-reactroot" in html
        ):
            detections.add("React")

        if (
            "__next_data__" in html
            or "/_next/" in searchable
        ):
            detections.add("Next.js")

        if (
            "vue.runtime" in searchable
            or "vue.global" in searchable
            or "vue.min.js" in searchable
        ):
            detections.add("Vue.js")

        if (
            "__nuxt__" in html
            or "/_nuxt/" in searchable
        ):
            detections.add("Nuxt.js")

        if (
            "ng-version" in html
            or "@angular/" in searchable
        ):
            detections.add("Angular")

        if (
            ".svelte" in searchable
            or "svelte-" in searchable
        ):
            detections.add("Svelte")

        if (
            "astro-island" in html
            or "/_astro/" in searchable
        ):
            detections.add("Astro")

        if (
            "solid-js" in searchable
            or "solidjs" in searchable
        ):
            detections.add("SolidJS")

        if (
            "preact" in searchable
        ):
            detections.add("Preact")

        for framework in sorted(detections):

            facts.append(
                Fact(
                    category="Technology",
                    entity="JavaScript",
                    name="framework",
                    value=framework,
                )
            )

        return facts