from core.contracts.intelligence import BaseIntelligence


class KeyAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized_data: dict,
    ) -> dict:

        algorithm = normalized_data.get(
            "public_key_algorithm"
        )

        key_size = normalized_data.get(
            "public_key_size"
        )

        findings = {}

        if algorithm:

            findings[
                "public_key_algorithm"
            ] = algorithm

        if key_size:

            findings[
                "public_key_size"
            ] = key_size

        #
        # Key Strength
        #

        if algorithm == "RSA":

            if key_size >= 4096:
                strength = "Very Strong"

            elif key_size >= 3072:
                strength = "Strong"

            elif key_size >= 2048:
                strength = "Good"

            else:
                strength = "Weak"

            findings[
                "key_strength"
            ] = strength

        elif algorithm in (
            "ECDSA",
            "Ed25519",
            "Ed448",
        ):

            findings[
                "key_strength"
            ] = "Modern"

        return findings