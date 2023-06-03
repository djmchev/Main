import random
import string


def generate_random_code():
  code_format = "TP$$$$$$"
  code = ""

  for char in code_format:
    if char == "$":
      code += random.choice(string.ascii_uppercase + string.digits)
    else:
      code += char

  return code


def generate_multiple_codes(num_codes):
  codes = []

  for _ in range(num_codes):
    code = generate_random_code()
    codes.append(code)

  return codes


def save_codes_to_file(codes, filename):
  with open(filename, "w") as file:
    for code in codes:
      file.write(code + "\n")


num_codes_to_generate = int(input("Enter the number of codes to generate: "))
generated_codes = generate_multiple_codes(num_codes_to_generate)



filename = input("Enter the filename to save the codes: ")
save_codes_to_file(generated_codes, filename + ".txt")
