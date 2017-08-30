Swiss Food Composition
======================

The Swiss Federal Food Safety and Veterinary Office ([FSVO](https://www.blv.admin.ch/blv/en/home.html)) has and maintain a [database](http://www.valeursnutritives.ch) of Swiss food composition. The database is available as a xslx file or through a webservice (more info [here](http://www.valeursnutritives.ch/request?xml=MessageData&xml=MetaData&xsl=Download&lan=en&pageKey=Start)).

The goal of this repo is to convert the xlsx file into personalized JSON files. The files can contain just the needed data, in the needed language. Well constructed JSON files can be easier to query than a huge xlsx file or slow webservice.

The dataset is available in four languages (English, German, French and Italian).


Data
----

The JSON files generated are of two types: the categories and the food items.

### Categories

There are 105 categories and more than hundred sub-categories. Here is a sample of the structure generated:

    {
        "categories": [
            {
                "id": 5,
                "name": "Alcoholic beverages",
                "name-de": "Alkoholhaltige Getränke",
                "name-fr": "Boissons alcoolisées",
                "name-it": "Bevande alcoliche",
                "subcategories": [
                    {
                        "id": 0,
                        "name": "Wine",
                        "name-de": "Wein",
                        "name-fr": "Vin",
                        "name-it": "Vino"
                    },
                    ...
                ]
            },
            ...
        ],
        "version": 5.3
    }


### Food items

For the food and its composition, we have approx. 1000 items. The structure looks like this:

    {
        "food-items": [
            {
                "id": 637,
                "name": "Raclette cheese",
                "categories": [
                    "6/0"
                ],
                "liquid": 0,
                "composition": {
                    "energy-kJ": {
                        "unit": "kJ",
                        "value": "1490"
                    },
                    "fat": {
                        "unit": "g",
                        "value": "27.9"
                    },
                    "sugars": {
                        "unit": "g",
                        "value": "0"
                    }
                }
            }, {
                "id": 14,
                "name": "Apple juice",
                "categories": [
                    "3/3",
                    "4/0"
                ],
                "liquid": 1,
                "composition": {
                    "energy-kJ": {
                        "unit": "kJ",
                        "value": "189"
                    },
                    "fat": {
                        "unit": "g",
                        "value": "0.1"
                    },
                    "sugars": {
                        "unit": "g",
                        "value": "10.3"
                    }
                }
            },
            ...
        ]
    }

This file is very modular. We can choose the language of the items in the four languages available (en-fr-de-it). Regarding the composition, we can choose to generage each of the 37 components (vitamins, protein, carbs, calcium, water, and so on). The configuration is made in the `config.py` file.


Usage
-----

The program is made for Python 3 and does not require any additional library. Just run it.

	python3.5 main.py

Feel free to change the content of the `main.py` file to your needs. Without changes, it generates files in the `data/` folder: the categories file and the food items file for each of the four languages.

The data is based on the version 5.3 of the database. If a new version is out, just convert it to tsv and replace the content of `data/full-dataset.tsv` with it.


Contribute
----------

We'd love to get your ideas for any improvement! Open an issue ;)