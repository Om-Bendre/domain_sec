import re

from core.models.finding import Finding


class AuthenticationAnalyzer:

    AUTH_SCHEMES = {

        "bearer": "Bearer",

        "basic": "Basic",

        "digest": "Digest",

        "apikey": "API Key",

        "api-key": "API Key",

        "token": "Token",

        "oauth": "OAuth",

        "jwt": "JWT",

    }

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        auth = normalized_data.get(
            "authentication",
            {},
        )

        headers = normalized_data.get(
            "headers",
            {},
        )

        body = normalized_data.get(
            "body",
            "",
        ).lower()

        challenge = auth.get(
            "www_authenticate",
        )

        #
        # Authentication Required
        #

        if challenge:

            findings.append(

                Finding(

                    category="API Security",

                    entity="Authentication",

                    name="authentication_required",

                    value=True,

                )

            )

        #
        # Detect authentication schemes
        #

        searchable = " ".join(

            [

                challenge or "",

                str(headers),

                body,

            ]

        ).lower()

        detected = set()

        for keyword, scheme in self.AUTH_SCHEMES.items():

            if keyword in searchable:

                detected.add(

                    scheme

                )

        for scheme in sorted(

            detected

        ):

            findings.append(

                Finding(

                    category="API Security",

                    entity="Authentication",

                    name="authentication_scheme",

                    value=scheme,

                )

            )

        #
        # WWW-Authenticate header
        #

        if challenge:

            findings.append(

                Finding(

                    category="API Security",

                    entity="Authentication",

                    name="www_authenticate",

                    value=challenge,

                )

            )

        #
        # Authorization header advertised
        #

        allow_headers = normalized_data.get(
            "cors",
            {},
        ).get(
            "headers",
            "",
        )

        if "authorization" in (

            allow_headers or ""

        ).lower():

            findings.append(

                Finding(

                    category="API Security",

                    entity="Authentication",

                    name="authorization_header_supported",

                    value=True,

                )

            )

        #
        # JWT Indicator
        #

        jwt_regex = re.compile(

            r"eyJ[A-Za-z0-9_\-=]+\.[A-Za-z0-9_\-=]+\.[A-Za-z0-9_\-=]+"

        )

        if jwt_regex.search(

            body

        ):

            findings.append(

                Finding(

                    category="API Security",

                    entity="Authentication",

                    name="jwt_indicator",

                    value=True,

                )

            )

        #
        # OAuth Indicator
        #

        oauth_keywords = [

            "oauth",

            "oauth2",

            "authorization_code",

            "client_credentials",

            "refresh_token",

            "access_token",

        ]

        if any(

            keyword in body

            for keyword in oauth_keywords

        ):

            findings.append(

                Finding(

                    category="API Security",

                    entity="Authentication",

                    name="oauth_indicator",

                    value=True,

                )

            )

        #
        # API Key Indicator
        #

        api_key_keywords = [

            "x-api-key",

            "api-key",

            "apikey",

        ]

        if any(

            keyword in searchable

            for keyword in api_key_keywords

        ):

            findings.append(

                Finding(

                    category="API Security",

                    entity="Authentication",

                    name="api_key_indicator",

                    value=True,

                )

            )

        return findings