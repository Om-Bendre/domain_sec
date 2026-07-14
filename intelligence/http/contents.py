from core.contracts.intelligence import BaseIntelligence


class ContentAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        content_type = (
            normalized.get("content_type")
            or ""
        ).lower()

        detected = "Unknown"

        if "text/html" in content_type:

            detected = "HTML"

        elif "application/json" in content_type:

            detected = "JSON"

        elif "application/xml" in content_type:

            detected = "XML"

        elif "text/plain" in content_type:

            detected = "Plain Text"

        elif "javascript" in content_type:

            detected = "JavaScript"

        elif "image/" in content_type:

            detected = "Image"

        elif "pdf" in content_type:

            detected = "PDF"

        return {

            "content_category": detected,

        }