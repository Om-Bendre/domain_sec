from bs4 import BeautifulSoup


class TechnologyNormalizer:

    def normalize(
        self,
        raw_data: dict,
    ) -> dict:

        html = raw_data.get(

            "body",

            "",

        )

        soup = BeautifulSoup(

            html,

            "lxml",

        )

        scripts = [

            script.get(

                "src",

                "",

            )

            for script

            in soup.find_all(

                "script",

                src=True,

            )

        ]

        stylesheets = [

            css.get(

                "href",

                "",

            )

            for css

            in soup.find_all(

                "link",

                rel="stylesheet",

            )

        ]

        meta = {

            tag.get(

                "name",

                ""
            ).lower():

            tag.get(

                "content",

                ""

            )

            for tag

            in soup.find_all(

                "meta"

            )

        }

        return {

            "url":

                raw_data.get(

                    "url"

                ),

            "headers":

                raw_data.get(

                    "headers",

                    {},

                ),

            "html":

                html,

            "scripts":

                scripts,

            "stylesheets":

                stylesheets,

            "meta":

                meta,

        }