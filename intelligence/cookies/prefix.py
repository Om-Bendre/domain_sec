class PrefixAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> dict:

        name = cookie["name"]

        if name.startswith("__Host-"):

            prefix = "__Host__"

            strength = "Very Strong"

        elif name.startswith("__Secure-"):

            prefix = "__Secure__"

            strength = "Strong"

        else:

            prefix = "None"

            strength = "Normal"

        return {

            "prefix": prefix,

            "prefix_strength": strength,

        }