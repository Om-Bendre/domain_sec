from datetime import datetime

from core.contracts.intelligence import BaseIntelligence


class ExpiryAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        expires = normalized.get(
            "valid_until",
        )

        if not expires:

            return {}

        expiry = datetime.strptime(

            expires,

            "%b %d %H:%M:%S %Y %Z",

        )

        remaining = (

            expiry - datetime.utcnow()

        ).days

        return {

            "days_until_expiry": remaining,

            "expired": remaining < 0,

        }