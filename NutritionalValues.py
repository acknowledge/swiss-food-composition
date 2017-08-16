"""Food composition file wrapper."""
from utils import Utils


class NutritionalValues:
    """Nutrional values class."""

    data_path = 'data/'
    full_dataset = 'full-dataset.tsv'
    categories_dataset = {
        'de': 'dataset-categories-de.json',
        'fr': 'dataset-categories-fr.json',
        'it': 'dataset-categories-it.json',
        'en': 'dataset-categories-en.json'
    }
    food_dataset = {
        'de': 'dataset-de.json',
        'fr': 'dataset-fr.json',
        'it': 'dataset-it.json',
        'en': 'dataset-en.json'
    }

    category_id = {
        'de': 11,
        'fr': 12,
        'it': 13,
        'en': 14
    }
    name_id = {
        'de': 3,
        'fr': 5,
        'it': 7,
        'en': 9
    }
    synonym_id = {
        'de': 4,
        'fr': 6,
        'it': 8,
        'en': 10
    }
    liquid_or_solid_id = 18
    composition_id = {
        'energy-kJ': 16,
        'energy-kcal': 21,
        'protein': 26,
        'alcohol': 31,
        'water': 36,
        'carbohydrates': 41,
        'starch': 46,
        'sugars': 51,
        'dietary-fibres': 56,
        'fat': 61,
        'cholesterol': 66,
        'fatty-acids-monounsaturated': 71,
        'fatty-acids-saturated': 76,
        'fatty-acids-polyunsaturated': 81,
        'vitamin-A': 86,
        'all-trans-retinol-equivalents': 91,
        'beta-carotene-activity': 96,
        'beta-carotene': 101,
        'vitamin-B1': 106,
        'vitamin-B2': 111,
        'vitamin-B6': 116,
        'vitamin-B12': 121,
        'niacin': 126,
        'folate': 131,
        'pantothenic-acid': 136,
        'vitamin-C': 141,
        'vitamin-D': 146,
        'vitamin-E': 151,
        'sodium': 156,
        'potassium': 161,
        'chloride': 166,
        'calcium': 171,
        'magnesium': 167,
        'phosphorus': 181,
        'iron': 186,
        'iodide': 191,
        'zinc': 196
    }

    def __init__(self, lang):
        """Constructor."""
        self.lang = lang

    def _format_categories(self, categories):
        categories_list = {}
        for categ in categories:
            cat_details = categ.split('/')
            main_categ = cat_details[0]
            if len(cat_details) > 1:
                sub_categ = cat_details[1]
            else:
                sub_categ = None

            if main_categ not in categories_list:
                categories_list[main_categ] = []

            if sub_categ is not None:
                categories_list[main_categ].append(sub_categ)
        return categories_list

    def _convert_unit(self, unit_name):
        if unit_name == 'kilojoule':
            return 'kJ'
        if unit_name == 'kilocalorie':
            return 'kcal'
        if unit_name == 'gram':
            return 'g'
        if unit_name is not '':
            print('Warning: a unit name is not converted !', unit_name)
        return unit_name

    def read_categories(self):
        """Just print the categories."""
        categories = Utils.open_json_file(self.data_path,
                                          self.categories_dataset[self.lang])

        for idx, cat in enumerate(categories):
            print(idx, cat)
            for idx2, subcat in enumerate(categories[cat]):
                print('\t', idx2, subcat)

    def export_categories(self):
        """Export categories to a file."""
        valnut = Utils.open_tsv_file(self.data_path, self.full_dataset)

        # remove the header line
        del valnut[0]

        categories = []
        for entry in valnut:
            # each product can have several categories
            cats = entry[self.category_id[self.lang]].split(';')
            for cat in cats:
                if cat not in categories:
                    categories.append(cat)
        cat_structure = self._format_categories(categories)

        Utils.save_json_file(self.data_path,
                             self.categories_dataset[self.lang],
                             cat_structure)

    def read_food(self):
        """Just print the categories."""
        food = Utils.open_json_file(self.data_path,
                                    self.food_dataset[self.lang])

        for idx, f in enumerate(food):
            print(idx, f)
            for idx2, subcat in enumerate(food[f]):
                print('\t', idx2, subcat)

    def export_food(self):
        """Export categories to a file."""
        valnut = Utils.open_tsv_file(self.data_path, self.full_dataset)

        # remove the header line
        del valnut[0]

        food_structure = {}
        for idx, entry in enumerate(valnut):
            food_name = entry[self.name_id[self.lang]]
            food_data = {}

            # synonyms
            if entry[self.synonym_id[self.lang]]:
                syns = entry[self.synonym_id[self.lang]].split(';')
                food_data['synonyms'] = syns

            # categories
            categories = entry[self.category_id[self.lang]].split(';')
            food_data['categories'] = self._format_categories(categories)

            # liquid or solid
            liquid_or_solid = entry[self.liquid_or_solid_id]
            if '100g' in liquid_or_solid:
                food_data['liquid'] = 0
            elif '100ml' in liquid_or_solid:
                food_data['liquid'] = 1
            else:
                print(food_name, '-->', liquid_or_solid)
                print('WTF is this food ?! It\'s neither liquid nor solid. '
                      'Please contact an administrator. '
                      'maybe the product is a plasma state.')

            # composition
            desired_fields = ['energy-kJ',  # write here the fields you need
                              'protein',
                              'sugars',
                              'fat']
            composition = {}
            for field in desired_fields:
                value = entry[self.composition_id[field]]
                unit = self._convert_unit(
                    entry[self.composition_id[field] + 1])
                composition[field] = {
                    'value': value,
                    'unit': unit
                }
            food_data['composition'] = composition

            # add the entry to the full array of food items
            food_structure[food_name] = food_data

        # save the full structure to a JSON file
        Utils.save_json_file(self.data_path,
                             self.food_dataset[self.lang],
                             food_structure)
