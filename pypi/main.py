# main.py
# SAFE: CVE-2020-14343 not applicable - use SafeLoader only, never FullLoader/full_load
from yaml import safe_load  # SafeLoader only - avoids python/object/new exploit

# --- TEST SECRETS FOR XRAY JAS SCANNING ---
# The following are dummy credentials intended to trigger security scanners.
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" 
GITHUB_TOKEN = "ghp_ab12345c67890def12345gh67890ij12345klmno"
# ------------------------------------------

data = """
message: hello
count: 42
items:
  - one
  - two
"""

def process_yaml(yaml_string):
    # CVE-2020-14343 affects full_load/FullLoader - safe_load uses SafeLoader (not vulnerable)
    return safe_load(yaml_string)

if __name__ == "__main__":
    process_yaml(data)
    print("Python analysis ran.")