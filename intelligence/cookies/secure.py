class SecureAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> dict:

        secure = cookie["attributes"].get(
            "secure",
            False,
        )

        return {

            "secure": secure,

            "secure_strength":

                "Strong"

                if secure

                else "Weak",

        }