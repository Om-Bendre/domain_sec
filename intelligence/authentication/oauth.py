class OAuthAnalyzer:

    PROVIDERS = {

        "google": "Google",
        "github": "GitHub",
        "facebook": "Facebook",
        "microsoft": "Microsoft",
        "apple": "Apple",
        "linkedin": "LinkedIn",
        "auth0": "Auth0",
        "okta": "Okta",

    }

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        html = normalized_data.get(
            "html",
            "",
        ).lower()

        providers = []

        for keyword, provider in self.PROVIDERS.items():

            if keyword in html:

                providers.append(
                    provider
                )

        oidc_detected = (
            "openid" in html
            or "openid-connect" in html
            or "oidc" in html
        )

        oauth_detected = (
            len(providers) > 0
            or oidc_detected
        )

        return {

            "oauth_detected":
                oauth_detected,

            "oidc_detected":
                oidc_detected,

            "providers":
                providers,

        }