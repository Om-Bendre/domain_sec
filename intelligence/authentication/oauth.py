from core.models.fact import Fact


OAUTH_PROVIDERS = {

    "accounts.google.com": "Google",

    "github.com/login/oauth": "GitHub",

    "facebook.com": "Facebook",

    "login.microsoftonline.com": "Microsoft",

    "appleid.apple.com": "Apple",

    "linkedin.com/oauth": "LinkedIn",

    "auth0.com": "Auth0",

    "okta.com": "Okta",

}


class OAuthAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        html = normalized_data.get(
            "html",
            "",
        ).lower()

        for endpoint, provider in OAUTH_PROVIDERS.items():

            if endpoint.lower() in html:

                facts.append(

                    Fact(

                        category="Authentication",

                        entity="OAuth",

                        name="oauth_indicator",

                        value=provider,

                        description="OAuth-related provider indicator detected in the response",

                    )

                )

        return facts