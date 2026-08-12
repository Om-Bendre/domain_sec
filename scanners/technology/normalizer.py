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

        #
        # Scripts
        #

        scripts = []

        inline_scripts = []

        for script in soup.find_all(
            "script"
        ):

            src = script.get(
                "src"
            )

            if src:
                scripts.append(src)

            else:
                content = script.string

                if content:
                    inline_scripts.append(
                        content
                    )

        #
        # Stylesheets
        #

        stylesheets = []

        for css in soup.find_all(
            "link",
            rel=lambda value: (
                value
                and "stylesheet" in value
            ),
        ):

            href = css.get(
                "href"
            )

            if href:
                stylesheets.append(
                    href
                )

        #
        # Meta tags
        #

        meta = {}

        for tag in soup.find_all(
            "meta"
        ):

            name = tag.get(
                "name"
            )

            content = tag.get(
                "content"
            )

            if name and content:

                meta[name.lower()] = content

            #
            # Also capture property-based
            # metadata such as og:*
            #

            prop = tag.get(
                "property"
            )

            if prop and content:

                meta[prop.lower()] = content

        #
        # Generator
        #

        generator = soup.find(
            "meta",
            attrs={
                "name": "generator"
            },
        )

        generator_value = None

        if generator:

            generator_value = generator.get(
                "content"
            )

        #
        # HTML attributes useful for
        # framework detection
        #

        html_attributes = []

        for tag in soup.find_all():

            for attribute in tag.attrs:

                html_attributes.append(
                    str(attribute).lower()
                )

        #
        # Response headers
        #

        headers = raw_data.get(
            "headers",
            {},
        )

        normalized_headers = {
            str(key).lower(): str(value)
            for key, value in headers.items()
        }

        return {

            "url":
                raw_data.get(
                    "url"
                ),

            "headers":
                normalized_headers,

            "html":
                html,

            "scripts":
                scripts,

            "inline_scripts":
                inline_scripts,

            "stylesheets":
                stylesheets,

            "meta":
                meta,

            "generator":
                generator_value,

            "cookies": raw_data.get(
                "cookie_headers",
                [],
            ),

            "html_attributes":
                list(
                    set(
                        html_attributes
                    )
                ),

        }