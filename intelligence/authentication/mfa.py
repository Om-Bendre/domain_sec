class MFAAnalyzer:

    MFA_KEYWORDS = {

        "otp",
        "totp",
        "2fa",
        "mfa",
        "verification code",
        "one-time password",
        "authenticator",
        "passkey",
        "webauthn",

    }

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        html = normalized_data.get(
            "html",
            "",
        ).lower()

        detected = []

        for keyword in self.MFA_KEYWORDS:

            if keyword in html:

                detected.append(
                    keyword
                )

        return {

            "mfa_detected":
                len(detected) > 0,

            "mfa_methods":
                detected,

        }