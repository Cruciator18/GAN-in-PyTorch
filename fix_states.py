import sys
import json

def fix_notebook_widgets(notebook_path):
    """
    Adds the missing 'state' key to widget metadata in a Jupyter Notebook.
    """
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        # Check for widget metadata in the main notebook metadata
        if 'metadata' in notebook and 'widgets' in notebook['metadata']:
            widgets = notebook['metadata']['widgets']
            for key, widget_data in widgets.items():
                if 'state' not in widget_data:
                    widget_data['state'] = {}
                    print(f"Fixed widget: {key}")

        print(f"\nSuccessfully processed '{notebook_path}'.")

        # Write the fixed content back to the file
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2)

    except FileNotFoundError:
        print(f"Error: The file '{notebook_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{notebook_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python fix_notebook.py <path_to_your_notebook.ipynb>")
    else:
        fix_notebook_widgets(sys.argv[1])
        