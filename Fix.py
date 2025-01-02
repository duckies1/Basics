import json


def repair_notebook(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # Iterate over all cells
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "code":
            # Add 'execution_count' if missing
            if "execution_count" not in cell:
                cell["execution_count"] = None
            # Ensure 'outputs' is a list
            if "outputs" not in cell or not isinstance(cell["outputs"], list):
                cell["outputs"] = []

    # Save the fixed notebook
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=4)
    print("Notebook repaired successfully!")


# Replace 'Cancer detect.ipynb' with your file name
repair_notebook("Linear Regression.ipynb")
