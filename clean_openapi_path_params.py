import sys
import yaml
import re
from copy import deepcopy

# Usage: python clean_openapi_path_params.py openapi.yaml cleaned_openapi.yaml

def extract_path_params(path):
    return set(re.findall(r"{(.*?)}", path))

def clean_openapi_yaml(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        openapi = yaml.safe_load(f)
    openapi_clean = deepcopy(openapi)
    paths = openapi_clean.get('paths', {})
    removed = []
    for path, path_item in paths.items():
        valid_params = extract_path_params(path)
        for method in list(path_item.keys()):
            op = path_item[method]
            if not isinstance(op, dict):
                continue
            if 'parameters' in op:
                new_params = []
                for param in op['parameters']:
                    if param.get('in') == 'path' and param.get('name') not in valid_params:
                        removed.append((path, method, param.get('name')))
                        continue
                    new_params.append(param)
                op['parameters'] = new_params
        # Also check top-level parameters (rare)
        if 'parameters' in path_item:
            new_params = []
            for param in path_item['parameters']:
                if param.get('in') == 'path' and param.get('name') not in valid_params:
                    removed.append((path, 'ALL', param.get('name')))
                    continue
                new_params.append(param)
            path_item['parameters'] = new_params
    # Optionally, remove requestBody $ref that are not schemas (not implemented here)
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(openapi_clean, f, sort_keys=False, allow_unicode=True)
    print(f"Removed {len(removed)} invalid path parameters:")
    for r in removed:
        print(f"  Path: {r[0]}, Method: {r[1]}, Param: {r[2]}")
    print(f"Cleaned OpenAPI YAML written to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_openapi_path_params.py openapi.yaml cleaned_openapi.yaml")
        sys.exit(1)
    clean_openapi_yaml(sys.argv[1], sys.argv[2])
