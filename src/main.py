from emodl_parser import parse_model_data
from emodl_silimarity_operator2 import similarity_operator

# Read model files
with open('./emodls/se.emodl', 'r') as file:
    model_SE = file.read()

with open('./emodls/si.emodl', 'r') as file:
    model_SI = file.read()

# Parse the models data
parsed_model_SE = parse_model_data(model_SE)
parsed_model_SI = parse_model_data(model_SI)

# Print the parsed dictionories
print("SE model: ", parsed_model_SE)
print("SI model: ", parsed_model_SI)


print("******* result dict of model: ",
      similarity_operator(parsed_model_SE, parsed_model_SI))
