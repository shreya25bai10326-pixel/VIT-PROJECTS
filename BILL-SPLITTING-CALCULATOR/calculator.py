# ==== calculator.py functions ====

def calculate_split(total_bill, participants):
  """
  Calculate how much each participant owes or should receivw.
  Positive means they get money back, negative means they owe money.
  """
  n = len(participants)
  fair_share = total_bill / n
  split_summary = {}

  for name, contribution in participants.items():
    split_summary[name] = contribution - fair_share

  return split_summary
  
