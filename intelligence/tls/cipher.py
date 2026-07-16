from core.contracts.intelligence import BaseIntelligence


class CipherAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        cipher = normalized.get(
            "cipher_suite",
            "",
        )

        bits = normalized.get(
            "cipher_bits",
            0,
        )

        if "AES_256" in cipher:

            encryption = "AES-256"

        elif "AES_128" in cipher:

            encryption = "AES-128"

        else:

            encryption = "Unknown"

        if "GCM" in cipher:

            mode = "GCM"

        elif "CBC" in cipher:

            mode = "CBC"

        else:

            mode = "Unknown"

        if "SHA384" in cipher:

            hash_algorithm = "SHA384"

        elif "SHA256" in cipher:

            hash_algorithm = "SHA256"

        else:

            hash_algorithm = "Unknown"

        return {

            "cipher_strength": (
                "Strong"
                if bits >= 256
                else "Weak"
            ),

            "encryption": encryption,

            "cipher_mode": mode,

            "hash_algorithm": hash_algorithm,

        }