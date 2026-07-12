from core.contracts.intelligence import BaseIntelligence

class GeoAnalyzer(BaseIntelligence):

    def analyze(
        self,
        normalized,
    ):

        return {

            "location":

                ", ".join(

                    filter(

                        None,

                        [

                            normalized.get("city"),

                            normalized.get("region"),

                            normalized.get("country"),

                        ],

                    )

                ),

            "coordinates":

                f"{normalized.get('latitude')}, {normalized.get('longitude')}",

        }