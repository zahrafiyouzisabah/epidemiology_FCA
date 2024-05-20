from emodl_silimarity_operator import process_reactions


def process_species(model_species1, model_species2):
    merged_species = {}

    # Collect all unique labels
    all_labels = set(item['label'] for item in model_species1).union(
        set(item['label'] for item in model_species2))

    # Create dictionaries for quick lookup
    species1_dict = {item['label']: item['initial'] for item in model_species1}
    species2_dict = {item['label']: item['initial'] for item in model_species2}

    for label in all_labels:
        if label in species1_dict and label in species2_dict:
            initial1 = species1_dict[label]
            initial2 = species2_dict[label]
            if initial1 == initial2:
                merged_species[label] = initial1
            else:
                merged_species[label] = [
                    min(initial1, initial2), max(initial1, initial2)]
        elif label in species1_dict:
            merged_species[label] = [0, species1_dict[label]]
        elif label in species2_dict:
            merged_species[label] = [0, species2_dict[label]]

    # Convert merged_species dictionary to the desired output format
    result = [{'label': label, 'initial': initial}
              for label, initial in merged_species.items()]
    return result


def similarity_operator(model1, model2):
    return {
        'species': process_species(model1['species'], model2['species']),
        'reactions': process_reactions(model1['reactions'], model2['reactions'])
    }
