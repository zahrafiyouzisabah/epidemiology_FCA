
def process_species(species_list1, species_list2):
    combined_species = {}
    # Create a combined dictionary of species with their initial values
    for species in species_list1 + species_list2:
        label = species['label']
        if label in combined_species:
            combined_species[label].add(species['initial'])
        else:
            combined_species[label] = {species['initial']}

    # Convert the sets to the desired format
    result_species = []
    for label, initials in combined_species.items():
        species_dict = {'label': label}
        if len(initials) > 1:
            species_dict['initial'] = [min(initials), max(initials)]
        else:
            species_dict['initial'] = list(initials)[0]
        # Check if the species is in both lists
        if label not in [s['label'] for s in species_list1] or label not in [s['label'] for s in species_list2]:
            species_dict['optional'] = True
        result_species.append(species_dict)
    # print(" spec Result --> ", result_species)
    return result_species


def process_reactions(reactions_list1, reactions_list2):
    combined_reactions = []
    all_reactions = reactions_list1 + reactions_list2
    unique_reactions = {(r['from'], r['to']): [] for r in all_reactions}

    for reaction in all_reactions:
        unique_reactions[(reaction['from'], reaction['to'])].append(reaction)

    for key, reaction_list in unique_reactions.items():
        reaction_dict = {'from': key[0], 'to': key[1]}
        if len(reaction_list) == 1:  # Only one dict has this reaction
            reaction_dict.update(reaction_list[0])  # Copy exact details
            reaction_dict['optional'] = True
        else:
            rates = {r['rate'] for r in reaction_list}
            if len(rates) == 1:
                reaction_dict['rate'] = rates.pop()
            else:
                reaction_dict['rate'] = 'FORMULA'
        combined_reactions.append(reaction_dict)

    # print("Resut Reactions: ", combined_reactions)
    return combined_reactions


def similarity_operator(model1, model2):
    return {
        'species': process_species(model1['species'], model2['species']),
        'reactions': process_reactions(model1['reactions'], model2['reactions'])
    }
