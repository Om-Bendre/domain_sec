from datetime import datetime


class WHOISNormalizer:

    def normalize(
        self,
        raw_data,
    ):

        def normalize_value(value):

            if isinstance(value, list):

                cleaned = []

                for item in value:

                    if isinstance(item, datetime):
                        item = item.isoformat()

                    if item not in cleaned:
                        cleaned.append(item)

                return cleaned

            if isinstance(value, datetime):
                return value.isoformat()

            return value

        return {
            "domain_name": normalize_value(raw_data.domain_name),
            "registrar": normalize_value(raw_data.registrar),
            "creation_date": normalize_value(raw_data.creation_date),
            "expiration_date": normalize_value(raw_data.expiration_date),
            "updated_date": normalize_value(raw_data.updated_date),
            "name_servers": normalize_value(raw_data.name_servers),
            "status": normalize_value(raw_data.status),
            "emails": normalize_value(raw_data.emails),
        }