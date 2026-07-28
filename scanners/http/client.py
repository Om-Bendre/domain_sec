import requests


class HTTPClient:

    def query(
        self,
        target: str,
    ):

        response = requests.get(
            target,
            allow_redirects=True,
            timeout=10,
        )

        #
        # Preserve every Set-Cookie header separately
        #

        original_response = response.raw._original_response

        cookie_headers = original_response.msg.get_all(
            "Set-Cookie",
            []
        )

        return {

            "url": response.url,

            "status_code": response.status_code,

            "reason": response.reason,

            "http_version": response.raw.version,

            "headers": dict(response.headers),

            "cookie_headers": cookie_headers,

            "content_length": len(response.content),

            "response_time_ms":
                response.elapsed.total_seconds() * 1000,

            "history": [

                redirect.url

                for redirect in response.history

            ],

        }