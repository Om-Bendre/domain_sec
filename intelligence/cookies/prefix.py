class PrefixAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> dict:

        name = cookie["name"]

        if name.startswith("__Host-"):

            return {

                "prefix": "__Host-",

                "prefix_strength": "Very Strong",

            }

        if name.startswith("__Secure-"):

            return {

                "prefix": "__Secure-",

                "prefix_strength": "Strong",

            }

        return {

            "prefix": "None",

            "prefix_strength": "Normal",

        }