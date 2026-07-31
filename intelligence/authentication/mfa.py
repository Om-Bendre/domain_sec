from core.models.finding import Finding


MFA_KEYWORDS = {

    "otp": "OTP",

    "totp": "TOTP",

    "2fa": "2FA",

    "mfa": "MFA",

    "webauthn": "WebAuthn",

    "passkey": "Passkey",

    "authenticator": "Authenticator",

    "verification code": "Verification Code",

    "one-time password": "One Time Password",

}


class MFAAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Finding]:

        findings = []

        html = normalized_data.get(
            "html",
            "",
        ).lower()

        for keyword, method in MFA_KEYWORDS.items():

            if keyword in html:

                findings.append(

                    Finding(

                        category="Authentication",

                        entity="MFA",

                        name="mfa_method",

                        value=method,

                        description="Multi-factor authentication indicator detected",

                    )

                )

        return findings