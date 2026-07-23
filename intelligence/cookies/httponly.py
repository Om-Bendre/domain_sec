class HttpOnlyAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> dict:

        httponly = cookie["attributes"].get(
            "httponly",
            False,
        )

        return {

            "httponly": httponly,

            "httponly_strength":

                "Strong"

                if httponly

                else "Weak",

        }