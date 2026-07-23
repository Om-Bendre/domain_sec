class SameSiteAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> dict:

        value = cookie["attributes"].get(
            "samesite"
        )

        if value:

            value = value.capitalize()

        if value == "Strict":

            strength = "Strong"

        elif value == "Lax":

            strength = "Good"

        elif value == "None":

            strength = "Weak"

        else:

            strength = "Weak"

        return {

            "samesite": value,

            "samesite_strength": strength,

        }