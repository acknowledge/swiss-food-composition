"""Main."""

from NutritionalValues import NutritionalValues
from NutritionalValuesV2 import NutritionalValuesV2


def generate_all_files():
    """Generate the categories and food composition in each lang."""
    langs = ['fr', 'it', 'de', 'en']

    for lang in langs:
        nv = NutritionalValues(lang)
        nv.export_categories()
        nv.export_food()


def generate_french_fries():
    """Generate the categories and food composition in French."""
    nv = NutritionalValues('fr')
    nv.export_categories()
    nv.export_food()


def generate_new_version():
    """Test of the new version."""
    nv = NutritionalValuesV2()
    nv.export_categories()

    # nv.read_categories()
    # nv.categories_to_ids()

    nv.export_food('en')


if __name__ == '__main__':

    # generate_french_fries()
    # generate_all_files()

    generate_new_version()
