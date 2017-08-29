"""Food composition file wrapper."""
from utils import Utils
import config
import time


class NutritionalValues:
    """Nutrional values class."""

    version = 5.3
    data_path = 'data/'
    full_dataset = 'full-dataset.tsv'
    categories_dataset = 'categories.json'
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

    def __init__(self):
        """Constructor."""

    def _format_categories(self, categories):
        categories_list = []
        for categ in categories:
            # add '/' at the end when no sub-category
            categ = list(map(lambda x: x if ('/' in x) else x + '/', categ))
            cat_details = [e.split('/') for e in categ]
            mcats, scats = zip(*cat_details)

            # main_categ and sub_categ are defined by the english names
            main_categ = mcats[0]
            sub_categ = scats[0] if scats[1] != '' else None

            # create main categories if necessary
            if not any(d['name'] == main_categ for d in categories_list):
                cat_item = {
                    'id': len(categories_list),
                    'name': main_categ,
                    'subcategories': []
                }
                if 'fr' in config.category_languages:
                    cat_item['name-fr'] = mcats[1]
                if 'de' in config.category_languages:
                    cat_item['name-de'] = mcats[2]
                if 'it' in config.category_languages:
                    cat_item['name-it'] = mcats[3]
                categories_list.append(cat_item)

            # create sub categories if necessary
            if sub_categ is not None:
                cat = [d for d in categories_list
                       if d['name'] == main_categ][0]
                if not any(d['name'] == sub_categ
                           for d in cat['subcategories']):
                    # subcategory doesn't exist already --> creation
                    subcat_item = {
                        'id': len(cat['subcategories']),
                        'name': sub_categ
                    }
                    if 'fr' in config.category_languages:
                        subcat_item['name-fr'] = scats[1]
                    if 'de' in config.category_languages:
                        subcat_item['name-de'] = scats[2]
                    if 'it' in config.category_languages:
                        subcat_item['name-it'] = scats[3]

                    cat['subcategories'].append(subcat_item)
        return categories_list

    def _convert_unit(self, unit_name):
        if unit_name == 'kilojoule':
            return 'kJ'
        if unit_name == 'kilocalorie':
            return 'kcal'
        if unit_name == 'gram':
            return 'g'
        if unit_name == 'milligram':
            return 'mg'
        if unit_name == 'microgram':
            return 'µg'
        if unit_name is not '':
            print('Warning: a unit name is not converted !', unit_name)
        return unit_name

    def read_categories(self):
        """Just print the categories."""
        categories = Utils.open_json_file(self.data_path,
                                          self.categories_dataset)
        for cat in categories['categories']:
            print(str(cat['id']) + ' --> ' + cat['name'])
            for subcat in cat['subcategories']:
                print('\t' + str(subcat['id']) + ' --> ' + subcat['name'])

    def export_categories(self):
        """Export categories to a file."""
        valnut = Utils.open_tsv_file(self.data_path, self.full_dataset)

        # remove the header line
        del valnut[0]

        categories = []
        for entry in valnut:
            # each product can have several categories
            cats_en = entry[self.category_id['en']].split(';')
            cats_fr = entry[self.category_id['fr']].split(';')
            cats_de = entry[self.category_id['de']].split(';')
            cats_it = entry[self.category_id['it']].split(';')
            cats = zip(cats_en, cats_fr, cats_de, cats_it)
            for cat in cats:
                if cat not in categories:
                    categories.append(cat)

        cat_structure = {
            'categories': self._format_categories(categories),
            'version': self.version,
            'date': time.strftime("%d/%m/%Y")
        }

        Utils.save_json_file(self.data_path,
                             self.categories_dataset,
                             cat_structure)

    def categories_to_ids(self):
        """Convert categories to ids."""
        file_content = Utils.open_json_file(self.data_path,
                                            self.categories_dataset)
        categories_list = {}
        for category in file_content['categories']:
            if len(category['subcategories']) > 0:
                for subcat in category['subcategories']:
                    cat_name = category['name'] + '/' + subcat['name']
                    cat_id = str(category['id']) + '/' + str(subcat['id'])
                    categories_list[cat_name] = cat_id
            else:
                cat_name = category['name']
                cat_id = str(category['id'])
                categories_list[cat_name] = cat_id
        return categories_list

    def read_food(self, lang):
        """Just print the categories."""
        food = Utils.open_json_file(self.data_path,
                                    self.food_dataset[lang])

        for idx, f in enumerate(food):
            print(idx, f)
            for idx2, subcat in enumerate(food[f]):
                print('\t', idx2, subcat)

    def export_food(self, lang):
        """Export categories to a file."""
        valnut = Utils.open_tsv_file(self.data_path, self.full_dataset)

        # remove the header line
        del valnut[0]

        food_structure = []
        for idx, entry in enumerate(valnut):
            food_name = entry[self.name_id[lang]]
            food_data = {}

            # synonyms
            if entry[self.synonym_id[lang]]:
                syns = entry[self.synonym_id[lang]].split(';')
                food_data['synonyms'] = syns

            # categories
            categories = entry[self.category_id['en']].split(';')
            categ_links = self.categories_to_ids()
            categs_list = []
            for categ in categories:
                categs_list.append(categ_links[categ])
            food_data['categories'] = categs_list

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
            composition = {}
            for field in config.desired_values:
                value = entry[self.composition_id[field]]
                unit = self._convert_unit(
                    entry[self.composition_id[field] + 1])
                if value != '':
                    composition[field] = {
                        'value': value,
                        'unit': unit
                    }
            food_data['composition'] = composition

            food_data['name'] = food_name
            food_data['id'] = len(food_structure)

            # add the entry to the full array of food items
            food_structure.append(food_data)

        data = {
            'food-items': food_structure,
            'version': self.version,
            'date': time.strftime("%d/%m/%Y")
        }

        # save the full structure to a JSON file
        Utils.save_json_file(self.data_path,
                             self.food_dataset[lang],
                             data)
