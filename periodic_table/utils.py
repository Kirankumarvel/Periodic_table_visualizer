"""
Utility functions for the periodic table visualizer
"""

def validate_atomic_number(number):
    """Validate if a number is a valid atomic number (1-118)."""
    try:
        num = int(number)
        return 1 <= num <= 118
    except (ValueError, TypeError):
        return False

def export_element_data(element, format_type="txt"):
    """
    Export element data to a file.
    Supported formats: txt, csv, json
    """
    if not element:
        return False
    
    try:
        if format_type == "txt":
            return _export_to_txt(element)
        elif format_type == "csv":
            return _export_to_csv(element)
        elif format_type == "json":
            return _export_to_json(element)
        else:
            raise ValueError("Unsupported format type")
    except Exception as e:
        print(f"Export failed: {str(e)}")
        return False

def _export_to_txt(element):
    """Export element data to a text file."""
    filename = f"{element['name']}_data.txt"
    with open(filename, 'w') as f:
        for key, value in element.items():
            f.write(f"{key}: {value}\n")
    return True

def _export_to_csv(element):
    """Export element data to a CSV file."""
    import csv
    filename = f"{element['name']}_data.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Property", "Value"])
        for key, value in element.items():
            writer.writerow([key, value])
    return True

def _export_to_json(element):
    """Export element data to a JSON file."""
    import json
    filename = f"{element['name']}_data.json"
    with open(filename, 'w') as f:
        json.dump(element, f, indent=4)
    return True