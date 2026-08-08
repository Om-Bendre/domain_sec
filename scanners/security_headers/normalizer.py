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
        # Security headers
        #

        for header, key in self.SECURITY_HEADERS.items():

            normalized[key] = headers.get(header)

        #
        # CSP
        #

        normalized["csp"] = headers.get(
            "Content-Security-Policy"
        )

        normalized["csp_report_only"] = headers.get(
            "Content-Security-Policy-Report-Only"
        )

        return normalized