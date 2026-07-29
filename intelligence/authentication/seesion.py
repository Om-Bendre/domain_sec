class SessionAnalyzer:

    SESSION_COOKIE_NAMES = {

        "session",
        "sessionid",
        "jsessionid",
        "phpsessid",
        "asp.net_sessionid",
        "connect.sid",
        "sid",

    }

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        cookies = normalized_data.get(
            "cookies",
            [],
        )

        session_cookie = None

        for cookie in cookies:

            cookie_name = (
                cookie.get(
                    "name",
                    "",
                ).lower()
            )

            if cookie_name in self.SESSION_COOKIE_NAMES:

                session_cookie = cookie

                break

        if session_cookie is None:

            return {

                "session_detected": False,

            }

        return {

            "session_detected": True,

            "session_cookie_name":
                session_cookie.get(
                    "name"
                ),

            "session_secure":
                session_cookie.get(
                    "secure"
                ),

            "session_httponly":
                session_cookie.get(
                    "httponly"
                ),

            "session_samesite":
                session_cookie.get(
                    "samesite"
                ),

            "session_expiration":
                session_cookie.get(
                    "expiration"
                ),

        }