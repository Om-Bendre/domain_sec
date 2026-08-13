from core.models.fact import Fact


class CertificateAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        fields = {

            "subject_common_name":
                "subject_common_name",

            "san_count":
                "san_count",

            "primary_san":
                "primary_san",

            "public_key_algorithm":
                "public_key_algorithm",

            "public_key_size":
                "public_key_size",

            "signature_algorithm":
                "signature_algorithm",


        }

        for field, name in fields.items():

            value = normalized_data.get(
                field,
            )

            if value is None:
                continue

            facts.append(

                Fact(

                    category="TLS",

                    entity="Certificate",

                    name=name,

                    value=value,

                )

            )

        return facts