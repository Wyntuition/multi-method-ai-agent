from pyparsing import nestedExpr


class Transform:
    def __init__(self, country, inputs, outputs):
        self.country = country
        self.inputs = inputs
        self.outputs = outputs

    def __str__(self):
        input_str = "\n".join(
            [f"({key} {value})" for key, value in self.inputs.items()])
        output_str = "\n".join(
            [f"({key} {value})" for key, value in self.outputs.items()])
        return f"(TRANSFORM C\n   (INPUTS\n      {input_str}\n   )\n   (OUTPUTS\n      {output_str}\n   )\n)"

    ########################################
    # Parse transformation files
    # Input: full path to file
    # Return: country, inputs, outputs lists
    ########################################
    def parse_transformations_by_nested_parens(self, file_path):

        # Read file and remove unnecessary whitespace
        with open(file_path, "r") as file:
            input_string = file.read()
        input_string = input_string.replace("\n", "")

        # Parse the nested parentheses
        result = nestedExpr(opener='(', closer=')').parseString(
            input_string).asList()

        # Extract the values
        transform_type = result[0][0]
        self.country = result[0][1]
        self.inputs = result[0][2]
        self.outputs = result[0][3]
        # Remove the labels
        self.inputs.remove('INPUTS')
        self.outputs.remove('OUTPUTS')

        # Print the extracted values
        print("Transform type:", transform_type)
        print("Country:", self.country)
        print("Inputs:", self.inputs)
        print("Outputs:", self.outputs)


#######
# TODO: clean when definitely not going to use

# def read_schedule_from_file(file_path):
#     schedule_inputs = {}
#     schedule_outputs = {}

#     with open(file_path, "r") as file:
#         section = ""
#         for line in file:
#             line = line.strip()
#             if line == "":
#                 continue
#             if line.startswith("(TRANSFORM"):
#                 country = line.split()[11]
#             if line.startswith("(INPUTS"):
#                 section = "inputs"
#             elif line.startswith("(OUTPUTS"):
#                 section = "outputs"
#             else:
#                 key, value = line[1:-1].split()
#                 if section == "inputs":


#                     schedule_inputs[key] = int(value)
#                 elif section == "outputs":
#                     schedule_outputs[key] = int(value)

#     return Schedule(schedule_inputs, schedule_outputs)
