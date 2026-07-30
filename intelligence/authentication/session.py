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
    ) -> dict:

        cookies = normalized_data.get(
            "cookies",
            [],
        )

        for cookie in cookies:

            lower_cookie = cookie.lower()

            #
            # Known session cookie names
            #

            for name in COMMON_SESSION_COOKIES:

                if name in lower_cookie:

                    return {

                        "session_detected": True,

                        "session_cookie": name,

                    }

            #
            # Generic session heuristic
            #

            if "session" in lower_cookie:

                cookie_name = lower_cookie.split("=")[0]

                return {

                    "session_detected": True,

                    "session_cookie": cookie_name,

                }

        return {

            "session_detected": False,

            "session_cookie": None,

        }