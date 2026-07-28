from core.models.finding import Finding


class CookieMapper:
    """
    Converts analyzed cookies into Finding objects.
    """

    DISPLAY_NAMES = {

        "secure": "Secure",

        "httponly": "HttpOnly",

        "samesite": "SameSite",

        "persistent": "Persistent",

        "expiration_type": "Expiration",

        "prefix": "Prefix",

    }

    SKIP_FIELDS = {

        "name",

        "value",

        "attributes",

        "secure_strength",

        "httponly_strength",

        "samesite_strength",

        "prefix_strength",

    }

    def map(
        self,
        cookie: dict,
    ) -> list[Finding]:

        findings = []

        cookie_name = cookie["name"]

        for key, value in cookie.items():

            if key in self.SKIP_FIELDS:
                continue

            metadata = {}

            if key == "secure":

                metadata["rating"] = cookie.get(
                    "secure_strength"
                )

            elif key == "httponly":

                metadata["rating"] = cookie.get(
                    "httponly_strength"
                )

            elif key == "samesite":

                metadata["rating"] = cookie.get(
                    "samesite_strength"
                )

            elif key == "prefix":

                metadata["rating"] = cookie.get(
                    "prefix_strength"
                )

            findings.append(

                Finding(

                    category="Cookie",

                    entity=cookie["name"],

                    name=self.DISPLAY_NAMES.get(
                        key,
                        key,
                    ),

                    value=value,

                    metadata=metadata,

                )

            )