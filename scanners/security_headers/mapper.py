from core.models.finding import Finding


class SecurityHeadersMapper:

    SKIP_FIELDS = {
        "hsts",
        "csp",
        "x_frame_options",
        "x_content_type_options",
        "referrer_policy",
        "permissions_policy",
    }

    DISPLAY_NAMES = {

        "hsts_status": "HSTS Status",
        "hsts_max_age": "HSTS Max Age",
        "hsts_strength": "HSTS Strength",
        "hsts_include_subdomains": "HSTS Include Subdomains",
        "hsts_preload": "HSTS Preload",

        "csp_status": "CSP Status",
        "csp_mode": "CSP Mode",
        "unsafe_inline": "Unsafe Inline",
        "unsafe_eval": "Unsafe Eval",
        "wildcard_sources": "Wildcard Sources",
        "csp_strength": "CSP Strength",

        "xfo_status": "X-Frame-Options Status",
        "xfo_value": "X-Frame-Options Value",
        "xfo_strength": "X-Frame-Options Strength",

        "xcto_status": "X-Content-Type-Options Status",
        "xcto_value": "X-Content-Type-Options Value",
        "xcto_strength": "X-Content-Type-Options Strength",

        "referrer_status": "Referrer Policy Status",
        "referrer_value": "Referrer Policy Value",
        "referrer_strength": "Referrer Policy Strength",

        "permissions_status": "Permissions Policy Status",
        "permissions_directive_count": "Permissions Policy Directives",
        "permissions_strength": "Permissions Policy Strength",
    }

    def map(
        self,
        normalized,
    ):

        findings = []

        for key, value in normalized.items():

            if key in self.SKIP_FIELDS:
                continue

            if value is None:
                continue

            findings.append(

                Finding(

                    name=self.DISPLAY_NAMES.get(
                        key,
                        key.replace("_", " ").title(),
                    ),

                    category="security_headers",

                    value=str(value),

                    metadata={},

                )

            )

        return findings