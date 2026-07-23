class ExpirationAnalyzer:

    def analyze(
        self,
        cookie: dict,
    ) -> dict:

        attrs = cookie["attributes"]

        persistent = (

            "expires" in attrs

            or

            "max-age" in attrs

        )

        return {

            "persistent": persistent,

            "expiration_type":

                "Persistent"

                if persistent

                else "Session",

        }