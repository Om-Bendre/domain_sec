from core.models.fact import Fact


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
    ) -> list[Fact]:

        facts = []

        html = normalized_data.get(
            "html",
            "",
        ).lower()

        for keyword, method in MFA_KEYWORDS.items():

            if keyword in html:

                facts.append(

                    Fact(

                        category="Authentication",

                        entity="MFA",

                        name="mfa_indicator",

                        value=method,

                        description="MFA-related indicator detected in the response",

                    )

                )

        return facts