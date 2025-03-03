# import json
# import os
#
# def load_credentials(json_filename):
#     """Loads login credentials from a JSON file."""
#
#     json_path = os.path.join(os.getcwd(), json_filename)
#
#     print(f"🔍 Looking for {json_filename} at: {json_path}")
#
#     if not os.path.exists(json_path):
#         raise FileNotFoundError(f"🚨 ERROR: {json_path} not found!")
#
#     with open(json_path, "r") as file:
#         credentials = json.load(file)
#
#     return credentials

import json
import os


def load_credentials(file_path):
    """Load credentials from a JSON file."""
    try:
        if not os.path.exists(file_path):
            print(f"🚨 ERROR: {file_path} does NOT exist!")
            return []

        with open(file_path, "r") as file:
            data = json.load(file)

        if not data:
            print(f"🚨 ERROR: {file_path} is EMPTY!")
            return []

        print(f"✅ Loaded {len(data)} credentials from {file_path}.")
        return data
    except json.JSONDecodeError:
        print(f"🚨 ERROR: {file_path} contains INVALID JSON!")
        return []
    except Exception as e:
        print(f"🚨 ERROR loading {file_path}: {e}")
        return []
