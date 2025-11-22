# ==== main.py code ====
def main():
  print("=== Bill Splitting Calculator ===\n")

  participants = get_participants()

  total_bill = float(input("\nEnter the total bill amount: "))

  split_summary = calculate_split(total_bill, participants)

  print("\n--- Bill Split Summary ---")
  for name, amount in split_summary.items():
    if amount >=0:
      print(f"{name} should recieve ₹{amount:.2f}")
    else:
      print(f"{name} oews ₹{-amount:.2f}")

if __name__ == "__main__":
  main()
      
