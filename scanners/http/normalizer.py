class HTTPNormalizer:

    def normalize(
        self,
        raw_data,
    ):

        headers = raw_data["headers"]

        version_map = {

            10: "HTTP/1.0",

            11: "HTTP/1.1",

            20: "HTTP/2",

            30: "HTTP/3",

        }

        return {

            "final_url": raw_data["url"],

            "status_code": raw_data["status_code"],

            "reason": raw_data["reason"],

            "http_version": version_map.get(

                raw_data["http_version"],

                str(raw_data["http_version"])

            ),

            "response_time_ms":

                round(

                    raw_data["response_time_ms"],


                    2,

                ),

            "redirect_count":

                len(raw_data["history"]),

            "redirect_chain":

                raw_data["history"],

            "server":

                headers.get("Server"),

            "content_type":

                headers.get("Content-Type"),

            "content_encoding":

                headers.get("Content-Encoding"),

            "content_length":

                raw_data["content_length"],

            "cache_control":

                headers.get("Cache-Control"),

            "connection":

                headers.get("Connection"),

            "allow":

                headers.get("Allow"),

            "headers":

                headers,

        }