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

        "secure_strength": "Secure Strength",

        "httponly_strength": "HttpOnly Strength",

        "samesite_strength": "SameSite Strength",

        "prefix_strength": "Prefix Strength",

    }

    SKIP_FIELDS = {

        "name",

        "value",

        "attributes",

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

            findings.append(

                Finding(

                    category="Cookie",

                    entity=cookie_name,

                    name=self.DISPLAY_NAMES.get(
                        key,
                        key.replace("_", " ").title(),
                    ),

                    value=value,

                )

            )

        return findings