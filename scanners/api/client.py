import requests


class APISecurityClient:

    DEFAULT_HEADERS = {

        "User-Agent": (

            "Mozilla/5.0 "

            "(X11; Linux x86_64) "

            "AppleWebKit/537.36 "

            "(KHTML, like Gecko) "

            "Chrome/138.0.0.0 "

            "Safari/537.36"

        )

    }

    def query(
        self,
        target: str,
        timeout: int = 10,
    ) -> dict:

        response = requests.get(

            target,

            headers=self.DEFAULT_HEADERS,

            allow_redirects=True,

            timeout=timeout,

        )

        try:

            options = requests.options(

                response.url,

                headers=self.DEFAULT_HEADERS,

                timeout=timeout,

            )

        except Exception:

            options = None

        return {

            #
            # Core
            #

            "url": response.url,

            "status_code": response.status_code,

            "reason": response.reason,

            "headers": dict(

                response.headers

            ),

            "body": response.text,

            "history": [

                r.url

                for r

                in response.history

            ],

            #
            # OPTIONS
            #

            "options":

                None

                if options is None

                else {

                    "status_code":

                        options.status_code,

                    "headers":

                        dict(

                            options.headers

                        ),

                }

        }