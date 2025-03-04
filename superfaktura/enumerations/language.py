"""
Language Enumeration.

This module provides an enumeration of languages that can be used in the SuperFaktura API.

Classes:
    - Language: Enumeration of languages.

Usage:
    from superfaktura.enumerations.language import Language
    language = Language.Czech
"""


class Language:
    """
    Language Enumeration.

    This enumeration represents the different languages that can be used in the SuperFaktura API.

    Values:
        - Czech: Czech
        - German: German
        - English: English
        - Croatian: Croatian
        - Hungarian: Hungarian
        - Italian: Italian
        - Dutch: Dutch
        - Polish: Polish
        - Romanian: Romanian
        - Russian: Russian
        - Slovak: Slovak
        - Slovene: Slovene
        - Spanish: Spanish
        - Ukrainian: Ukrainian

    Usage:
        language = Language.Czech
    """

    Czech = "cze"
    German = "deu"
    English = "eng"
    Croatian = "hrv"
    Hungarian = "hun"
    Italian = "ita"
    Dutch = "nld"
    Polish = "pol"
    Romanian = "rom"
    Russian = "rus"
    Slovak = "slo"
    Slovene = "slv"
    Spanish = "spa"
    Ukrainian = "ukr"
