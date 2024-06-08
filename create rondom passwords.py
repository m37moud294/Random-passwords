import random
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True,
                      include_digits=True, include_symbols=True):
  """
  Generates a random password with the specified criteria.

  Args:
      length (int, optional): The length of the password. Defaults to 12.
      include_uppercase (bool, optional): Whether to include uppercase letters. Defaults to True.
      include_lowercase (bool, optional): Whether to include lowercase letters. Defaults to True.
      include_digits (bool, optional): Whether to include digits. Defaults to True.
      include_symbols (bool, optional): Whether to include symbols. Defaults to True.

  Returns:
      str: The generated random password.
  """

  all_characters = ""

  if include_uppercase:
    all_characters += string.ascii_uppercase
  if include_lowercase:
    all_characters += string.ascii_lowercase
  if include_digits:
    all_characters += string.digits
  if include_symbols:
    all_characters += string.punctuation

  if not all_characters:
    raise ValueError("At least one character type must be included.")

  password = ''.join(random.choice(all_characters) for _ in range(length))
  return password

# Example usage
password = generate_password()
print(password)

# Generate a password with specific criteria
password = generate_password(16, include_symbols=False)
print(password)
