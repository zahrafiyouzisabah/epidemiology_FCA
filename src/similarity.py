from samples.model1 import model1
from samples.model2 import model2


def combine_two_models():
    combined_compartments = handle_compartments()
    combined_flows = handle_flows()
    print("combinedCompartments :", combined_compartments)
    print("Combined flows:", combined_flows)


def handle_compartments():
    compartments1 = model1['compartments'][:]
    compartments2 = model2['compartments'][:]

    result, remainings = get_abstracted_compartments(
        compartments1, compartments2)
    result2, _ = get_abstracted_compartments(remainings, [])

    return result + result2


def handle_flows():
    flows1 = model1['flows'][:]
    flows2 = model2['flows'][:]

    result, remainings = get_abstracted_flows(flows1, flows2)
    result2, _ = get_abstracted_flows(remainings, [])
    return result + result2


def get_abstracted_compartments(compartments1, compartments2):
    result = []
    for c1 in compartments1:
        matched_compartments = []
        unmatched_compartments = [
            c2 for c2 in compartments2 if not are_components_matched(c1, c2)]
        matched_compartments = [
            c2 for c2 in compartments2 if are_components_matched(c1, c2)]

        if not matched_compartments:
            matched_compartments.append([""])

        matched_compartments.append(c1)

        combined_compartment = get_combined_compartments(matched_compartments)
        result.append(combined_compartment)

        compartments2 = unmatched_compartments

    return result, compartments2


def get_combined_compartments(matched_compartments):
    combined = set()
    for sub_array in matched_compartments:
        combined.update(sub_array)
    return list(combined)


def are_components_matched(c1, c2):
    found = False
    for item1 in c1:
        for item2 in c2:
            prefix1 = item1.split('_')[0]
            prefix2 = item2.split('_')[0]
            if prefix1 == prefix2:
                found = True
                break
    return found


def get_abstracted_flows(flows1, flows2):
    result = []

    for f1 in flows1:
        matched_flows = []
        matched_froms1 = []
        matched_tos1 = []
        unmatched_flows = []

        # Check and filter flows based on matches
        for f2 in flows2:
            matched, matched_froms, matched_tos = flows_match_check(f1, f2)
            if matched:
                matched_flows.append(f2)
                matched_froms1.extend(matched_froms)
                matched_tos1.extend(matched_tos)
            else:
                unmatched_flows.append(f2)

        flows2 = unmatched_flows

        # Handle unmatched cases
        if not matched_froms1:
            matched_froms1.append([""])
        matched_froms1.append(f1[0])
        combined_from = get_combined_compartments(matched_froms1)

        if not matched_tos1:
            matched_tos1.append([""])
        matched_tos1.append(f1[1])
        combined_to = get_combined_compartments(matched_tos1)

        # Include all parameter arrays from the matched flows plus the current flow's parameters
        matched_params = [flow[2] for flow in matched_flows] + [f1[2]]
        if not matched_flows:
            matched_params.append([""])
        combined_params = get_combined_compartments(matched_params)

        result.append([combined_from, combined_to, combined_params])

    return result, flows2


def flows_match_check(f1, f2):
    from1, to1 = f1[0], f1[1]
    from2, to2 = f2[0], f2[1]

    are_froms_match = are_components_matched(from1, from2)
    are_tos_match = are_components_matched(to1, to2)

    matched_froms = [from1, from2] if are_froms_match else []
    matched_tos = [to1, to2] if are_tos_match else []

    return are_froms_match or are_tos_match, matched_froms, matched_tos


combine_two_models()
