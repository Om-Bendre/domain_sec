from core.contracts.intelligence import BaseIntelligence


class CipherAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        bits = normalized.get(
            "cipher_bits",
            0,
        )

        return {

            "strong_cipher": bits >= 256,

            "cipher_strength": (

                "Strong"

                if bits >= 256

                else "Weak"

            ),

        }