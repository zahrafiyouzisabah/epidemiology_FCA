# {
#     species: [{label: "S", initial: 990}, {label: "I", initial: 10}],
#     reactions: [{from: "S", to: "I", rate: * Kl S}]
# }

import re

with open('./emodls/se.emodl', 'r') as file:
    model_data = file.read()


def parse_model_data(data):
    # Dictionary to store the species and reactions
    model_dict = {"species": [], "reactions": []}

    # Regular expression to match species
    species_pattern = re.compile(r"\(species (\w+)\s*(?:(\d+))?\)")
    for match in species_pattern.finditer(data):
        model_dict["species"].append({
            "label": match.group(1),
            "initial":  int(match.group(2)) if match.group(2) else 0
        })

    # Regular expression to match reactions
    reaction_pattern = re.compile(
        r"\(reaction \w+\s*\((\w+)\)\s*\((\w+)\)\s*(.*)\)")
    for match in reaction_pattern.finditer(data):
        model_dict["reactions"].append({
            "from": match.group(1),
            "to": match.group(2),
            "rate": match.group(3).strip()
        })

    return model_dict


# Parse the model data
parsed_model = parse_model_data(model_data)

# Print the dictionary
print(parsed_model)
