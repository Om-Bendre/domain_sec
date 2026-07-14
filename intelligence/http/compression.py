from core.contracts.intelligence import BaseIntelligence


class CompressionAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        encoding = normalized.get(
            "content_encoding"
        )

        return {

            "compression_enabled":

                encoding is not None,

            "compression_algorithm":

                encoding
                if encoding
                else "None",

        }