import requests


class AuthenticationClient:
    """
    Collects all raw data required by the Authentication Scanner.

    """

    DEFAULT_HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
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

        original_response = response.raw._original_response

        cookie_headers = original_response.msg.get_all(
            "Set-Cookie",
            [],
        )

        return {

            "url": response.url,

            "status_code": response.status_code,

            "reason": response.reason,

            "http_version": response.raw.version,

            "headers": dict(response.headers),

            "cookie_headers": cookie_headers,

            "content_length": len(response.content),

            "response_time_ms": round(
                response.elapsed.total_seconds() * 1000,
                2,
            ),

            "history": [
                redirect.url
                for redirect in response.history
            ],

            #
            # Required by Authentication Scanner
            #
            "html": response.text,

        }