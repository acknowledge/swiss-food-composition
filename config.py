"""Configuration file."""

# Languages in the categories file
# - possibilities: 'en', 'fr', 'de', 'it'
# - note: english is by default the official name of the category
category_languages = ['en', 'fr', 'de', 'it']

# Copy/paste this array and keep only the values you
#     want to appear on the output JSON file.
'''desired_values = {
    'energy-kJ',
    'energy-kcal',
    'protein',
    'alcohol',
    'water',
    'carbohydrates',
    'starch',
    'sugars',
    'dietary-fibres',
    'fat',
    'cholesterol',
    'fatty-acids-monounsaturated',
    'fatty-acids-saturated',
    'fatty-acids-polyunsaturated',
    'vitamin-A',
    'all-trans-retinol-equivalents',
    'beta-carotene-activity',
    'beta-carotene',
    'vitamin-B1',
    'vitamin-B2',
    'vitamin-B6',
    'vitamin-B12',
    'niacin',
    'folate',
    'pantothenic-acid',
    'vitamin-C',
    'vitamin-D',
    'vitamin-E',
    'sodium',
    'potassium',
    'chloride',
    'calcium',
    'magnesium',
    'phosphorus',
    'iron',
    'iodide',
    'zinc'
}'''
desired_values = ['energy-kJ', 'protein', 'sugars', 'fat']
