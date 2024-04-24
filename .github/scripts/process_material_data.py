from pathlib import Path
import json


curdir = Path(__file__).parent
root = curdir.parent.parent


data = {}

with open(curdir / 'mc/output.txt') as fp:
    for line in fp:
        line = line.rstrip()
        if '[MaterialLogger]' not in line:
            continue

        line = line[34:]  # Strip "[15:32:41 INFO]: [MaterialLogger] "
        if line.startswith("true|"):
            line = line[5:]
            assert "[" not in line  # But don't process any further
            continue

        if not line.startswith("false|"):
            continue  # Hmmm???

        line = line[6:]
        try:
            material, states = line.split('[', 1)
            data[material] = {}

            states = states[:-1].split(',')  # Remove ']'
            for state in states:
                key, value = state.split('=', 1)
                if value.lower() == "false":
                    value = False
                elif value.lower() == "true":
                    value = True

                data[material][key] = value
        except ValueError:
            data[line] = {}  # No states


with open(root / "material_data.json", "w") as fp:
    json.dump(data, fp=fp, indent=4)
