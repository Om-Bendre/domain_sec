from core.contracts.intelligence import BaseIntelligence


class CertificateAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        subject = normalized.get(
            "subject_common_name",
        )

        issuer = normalized.get(
            "issuer_common_name",
        )

        return {

            "self_signed": subject == issuer,

            "wildcard_certificate":

                subject.startswith("*."),

        }