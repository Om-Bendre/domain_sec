import re

from core.models.fact import Fact


class CAAAnalyzer:

    def analyze(
        self,
        normalized_data: dict,
    ) -> list[Fact]:

        facts = []

        records = normalized_data.get(
            "records",
            {},
        )

        caa_records = records.get(
            "CAA",
            [],
        )

    
        for record in caa_records:

            text = str(record).strip()

            match = re.match(
                r"^\d+\s+(\S+)\s+\"?(.*?)\"?$",
                text,
            )

            if not match:
                continue

            tag = match.group(1).lower()
            value = match.group(2)

            facts.append(
                Fact(
                    category="DNS",
                    entity="CAA",
                    name=tag,
                    value=value,
                )
            )

        return facts