class SecurityHeadersNormalizer:

    SECURITY_HEADERS = {
        "Strict-Transport-Security": "hsts",
        "X-Frame-Options": "x_frame_options",
        "X-Content-Type-Options": "x_content_type_options",
        "Referrer-Policy": "referrer_policy",
        "Permissions-Policy": "permissions_policy",
    }

    def normalize(
        self,
        raw_data,
    ):

        headers = raw_data.get(
            "headers",
            {},
        )

        normalized = {}

        #
        # Normal headers
        #

        for header, key in self.SECURITY_HEADERS.items():

            normalized[key] = headers.get(header)

        #
        # CSP (supports both enforced and report-only)
        #

        if headers.get("Content-Security-Policy"):

            normalized["csp"] = headers.get(
                "Content-Security-Policy"
            )

            normalized["csp_mode"] = "Enforced"

        elif headers.get("Content-Security-Policy-Report-Only"):

            normalized["csp"] = headers.get(
                "Content-Security-Policy-Report-Only"
            )

            normalized["csp_mode"] = "Report-Only"

        else:

            normalized["csp"] = None
            normalized["csp_mode"] = "Missing"

        return normalized