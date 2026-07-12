from core.contracts.intelligence import BaseIntelligence

class ASNAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        return {

            "organization": normalized.get(
                "asn_description"
            ),

            "registry": normalized.get(
                "asn_registry"
            ),

            "country": normalized.get(
                "asn_country"
            ),

            "public_asn": normalized.get(
                "asn"
            ) is not None,

        }