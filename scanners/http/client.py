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

        original_response = (
            response.raw._original_response
        )

        cookie_headers = (
            original_response.msg.get_all(
                "Set-Cookie",
                [],
            )
        )

        redirect_statuses = [
            redirect.status_code
            for redirect in response.history
        ]

        return {

            "url":
                response.url,

            "status_code":
                response.status_code,

            "reason":
                response.reason,

            "http_version":
                response.raw.version,

            "headers":
                dict(response.headers),

            "cookie_headers":
                cookie_headers,

            "response_time_ms":
                response.elapsed.total_seconds() * 1000,

            "history": [
                redirect.url
                for redirect in response.history
            ],

            "redirect_statuses":
                redirect_statuses,

            "initial_status":
                (
                    response.history[0].status_code
                    if response.history
                    else response.status_code
                ),

            "final_status":
                response.status_code,

            "final_url":
                response.url,

            "body":
                response.text,
        }