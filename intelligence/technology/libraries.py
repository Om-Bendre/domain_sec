from core.models.finding import Finding


LIBRARIES = {

    "jquery": "jQuery",

    "axios": "Axios",

    "lodash": "Lodash",

    "moment": "Moment.js",

    "chart.js": "Chart.js",

    "chartjs": "Chart.js",

    "d3": "D3.js",

    "three": "Three.js",

    "anime": "Anime.js",

    "leaflet": "Leaflet",

    "socket.io": "Socket.IO",

    "hammer": "Hammer.js",

}


class LibrariesAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        scripts = " ".join(

            normalized_data.get(

                "scripts",

                [],

            )

        ).lower()

        html = normalized_data.get(

            "html",

            "",

        ).lower()

        searchable = scripts + html

        for key, library in LIBRARIES.items():

            if key in searchable:

                findings.append(

                    Finding(

                        category="Technology",

                        entity="Libraries",

                        name="library",

                        value=library,

                    )

                )

        return findings