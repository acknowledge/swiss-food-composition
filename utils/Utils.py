"""Utilities library."""
import os
import json


class Utils:
    """Utils class."""

    @staticmethod
    def ask_user(question):
        """Wait for user input."""
        answer = input(question)
        return answer

    @staticmethod
    def format_folder_name(name):
        """Replace space with underscore for folder or files names."""
        name = name.replace(' ', '_').strip()
        return name

    @staticmethod
    def format_folder_id(id):
        """Fill 3 digits."""
        return str(id).zfill(3)

    @staticmethod
    def save_to_file(folder, filename, content):
        """Save content to file."""
        filename = folder + filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            try:
                f.write(content)
            except UnicodeEncodeError:
                print('UnicodeEncodingError for file ' + filename)
            except:
                print('Error for file ' + filename)

    @staticmethod
    def append_to_file(folder, filename, content):
        """Append content to existing file."""
        filename = folder + filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "a") as f:
            try:
                f.write(content)
            except UnicodeEncodeError:
                print('UnicodeEncodingError for file ' + filename)
            except:
                print('Error for file ' + filename)

    @staticmethod
    def save_json_file(path, filename, content):
        """Save JSON file."""
        filename = path + filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(content, f, indent=4, sort_keys=True)

    @staticmethod
    def open_json_file(path, filename):
        """Open JSON file."""
        if not os.path.exists(path + filename):
            Utils.save_json_file(path, filename, {})

        with open(path + filename, encoding="utf-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def open_xml_file(path, filename):
        """Open XML file."""
        with open(path + filename, encoding="latin-1") as f:
            data = f.read().replace('\n', '')
        return data

    @staticmethod
    def open_tsv_file(path, filename):
        """Open TSV file."""
        with open(path + filename, encoding="latin-1") as f:
            # data = f.read().replace('\n', '')
            data = [line.strip().split('\t') for line in f]
        return data

    @staticmethod
    def open_html_file(path, filename):
        """Open HTML file."""
        data = ''
        with open(path + filename) as f:
            try:
                data = f.read().replace('\n', '')
            except UnicodeDecodeError:
                print('UnicodeDecodeError for file ' + filename)
            except:
                print('Error for file ' + filename)
        return data

    @staticmethod
    def open_file(path, filename):
        """Open file."""
        with open(path + filename, encoding="latin-1") as f:
            data = f.read()
        return data
