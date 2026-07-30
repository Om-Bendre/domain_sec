COMMON_CSRF_NAMES = {

    "csrf",

    "_csrf",

    "csrftoken",

    "csrfmiddlewaretoken",

    "authenticity_token",

    "__requestverificationtoken",

    "_token",

}


class CSRFAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        forms = normalized_data.get(
            "forms",
            [],
        )

        for form in forms:

            for field in form["inputs"]:

                if field["type"] != "hidden":

                    continue

                name = field["name"].lower()

                if name in COMMON_CSRF_NAMES:

                    return {

                        "csrf_detected": True,

                        "csrf_field": field,

                    }

        return {

            "csrf_detected": False,

            "csrf_field": None,

        }