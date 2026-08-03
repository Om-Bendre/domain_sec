from datetime import datetime


class WHOISNormalizer:

    def _first(
        self,
        value,
    ):

        if isinstance(
            value,
            list,
        ):

            return value[0] if value else None

        return value

    def _list(
        self,
        value,
    ):

        if value is None:

            return []

        if isinstance(
            value,
            list,
        ):

            return value

        return [value]

    def normalize(
        self,
        raw_data: dict,
    ) -> dict:

        return {

            "registrar":
                self._first(
                    raw_data.get("registrar"),
                ),

            "registrar_url":
                self._first(
                    raw_data.get("registrar_url"),
                ),

            "registrar_iana_id":
                self._first(
                    raw_data.get("registrar_iana_id"),
                ),

            "creation_date":
                self._first(
                    raw_data.get("creation_date"),
                ),

            "updated_date":
                self._first(
                    raw_data.get("updated_date"),
                ),

            "expiration_date":
                self._first(
                    raw_data.get("expiration_date"),
                ),

            "status":
                self._list(
                    raw_data.get("status"),
                ),

            "name_servers":
                self._list(
                    raw_data.get("name_servers"),
                ),

            "registrant_country":
                self._first(
                    raw_data.get("registrant_country"),
                ),

            "registrant_organization":
                self._first(
                    raw_data.get("registrant_organization"),
                ),

            "registrant_email":
                self._first(
                    raw_data.get("registrant_email"),
                ),

            "abuse_email":
                self._first(
                    raw_data.get("abuse_email"),
                ),

        }