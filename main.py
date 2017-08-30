"""Main."""

from NutritionalValues import NutritionalValues


def generate_all_files():
    """Generate the categories and food composition in each lang."""
    langs = ['fr', 'it', 'de', 'en']

    nv = NutritionalValues()
    nv.export_categories()
    for lang in langs:
        nv.export_food(lang)


def generate_french_fries():
    """Generate the categories and food composition in French."""
    nv = NutritionalValues()
    nv.export_categories()
    # nv.categories_to_ids()
    nv.export_food('fr')


if __name__ == '__main__':

    generate_all_files()
    # generate_french_fries()
