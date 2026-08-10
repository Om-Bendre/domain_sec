from core.models.fact import Fact


COMMON_SESSION_COOKIES = {

    "phpsessid",

    "jsessionid",

    "asp.net_sessionid",

    "sessionid",

    "connect.sid",

    "_gh_sess",

    "laravel_session",

    "ci_session",

    "sid",

    "sessid",

}


class SessionAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        cookies = normalized_data.get(
            "cookies",
            [],
        )

        for cookie in cookies:

            cookie_name = cookie.split(
                "=",
                1,
            )[0].strip().lower()

            if cookie_name in COMMON_SESSION_COOKIES:

                facts.append(
                    Fact(
                        category="Authentication",
                        entity="Session",
                        name="session_cookie",
                        value=cookie_name,
                        description="Session cookie detected",
                    )
                )

        return facts