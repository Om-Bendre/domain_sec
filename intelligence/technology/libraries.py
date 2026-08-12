from core.models.fact import Fact


class LibrariesAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        scripts = " ".join(
            normalized_data.get(
                "scripts",
                [],
            )
        ).lower()

        detections = set()

        if "jquery" in scripts:
            detections.add("jQuery")

        if "axios" in scripts:
            detections.add("Axios")

        if "lodash" in scripts:
            detections.add("Lodash")

        if "moment" in scripts:
            detections.add("Moment.js")

        if "chart.js" in scripts:
            detections.add("Chart.js")

        if "d3.js" in scripts:
            detections.add("D3.js")

        if "three.js" in scripts:
            detections.add("Three.js")

        if "anime.js" in scripts:
            detections.add("Anime.js")

        if "leaflet" in scripts:
            detections.add("Leaflet")

        if "socket.io" in scripts:
            detections.add("Socket.IO")

        if "hammer.js" in scripts:
            detections.add("Hammer.js")

        for library in sorted(detections):

            facts.append(
                Fact(
                    category="Technology",
                    entity="Libraries",
                    name="library",
                    value=library,
                )
            )

        return facts