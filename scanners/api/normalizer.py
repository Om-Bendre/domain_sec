class APISecurityNormalizer:

    def normalize(
        self,
        raw_data: dict,
    ) -> dict:

        headers = raw_data.get(

            "headers",

            {},

        )

        options = raw_data.get(

            "options",

            {},

        )

        options_headers = {}

        if options:

            options_headers = options.get(

                "headers",

                {},

            )

        authentication = {

            "www_authenticate":

                headers.get(

                    "WWW-Authenticate"

                ),

            "authorization":

                headers.get(

                    "Authorization"

                ),

        }

        cors = {

            "origin":

                headers.get(

                    "Access-Control-Allow-Origin"

                ),

            "credentials":

                headers.get(

                    "Access-Control-Allow-Credentials"

                ),

            "headers":

                headers.get(

                    "Access-Control-Allow-Headers"

                ),

            "methods":

                headers.get(

                    "Access-Control-Allow-Methods"

                ),

            "max_age":

                headers.get(

                    "Access-Control-Max-Age"

                ),

            "expose_headers":

                headers.get(

                    "Access-Control-Expose-Headers"

                ),

        }

        rate_limiting = {

            "limit":

                headers.get(

                    "X-RateLimit-Limit"

                ),

            "remaining":

                headers.get(

                    "X-RateLimit-Remaining"

                ),

            "reset":

                headers.get(

                    "X-RateLimit-Reset"

                ),

            "retry_after":

                headers.get(

                    "Retry-After"

                ),

        }

        documentation = {

            "body":

                raw_data.get(

                    "body",

                    "",

                ).lower(),

        }

        api = {

            "content_type":

                headers.get(

                    "Content-Type"

                ),

            "allow":

                options_headers.get(

                    "Allow"

                ),

        }

        return {

            "url":

                raw_data.get(

                    "url"

                ),

            "status_code":

                raw_data.get(

                    "status_code"

                ),

            "headers":

                headers,

            "body":

                raw_data.get(

                    "body",

                    "",

                ),

            "authentication":

                authentication,

            "cors":

                cors,

            "rate_limiting":

                rate_limiting,

            "documentation":

                documentation,

            "api":

                api,

        }