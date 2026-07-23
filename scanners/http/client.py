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

        return {

            "url": response.url,

            "status_code": response.status_code,

            "reason": response.reason,

            "http_version": response.raw.version,

            "headers": dict(response.headers),

            "raw_headers":response.raw.headers,

            "content_length": len(response.content),

            "response_time_ms":
                response.elapsed.total_seconds() * 1000,

            "history": [

                redirect.url

                for redirect in response.history

            ],

        }