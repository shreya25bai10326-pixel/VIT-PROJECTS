#==== utils.py functions ====

def get_participants():
  """
  Collect participant name and their contributions.
  Returns a dictionary of participants with contibutions.
  """
  participants = {}
  n = int(input("Enter the number of participants: "))

  for i in range(n):
    name = input(f"Enter the name of participant {i+1}: ")
    contribution = float(input(f"Enter contribution by {name}:
    participants[name] = contribution

  return participants

