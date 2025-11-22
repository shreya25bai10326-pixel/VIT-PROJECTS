-----BILL-SPLITTING-CALCULATOR-----

##📌Project Overview

This project is a simple Python-based tool that help groups split a bill fairly. Users can enter the total amount, number of people, individual contributions, or shared expenses. The program calculates how much each person should pay or recieve, ensuring a transparent and accurate settlement. This helps avoid confusion and ensures fair contribution from everyone.

##🎯 Objective to provide a simple and efficient calculator that:

- Takes the total bill amount.
- Accepts the number of people in the group.
- Computes the amount each person has to pay.
- Handles invalid inputs using error validation.

##✨ Features

- Accepts total bill amount from the user.
- Accepts number of people in the group.
- Calculates individual shares.
- Prevents error like dividing by zero.
- User-friendly and beignner-friendly.

##👩‍💻 Technologies used

Python(Core Language)
No external libraries required

##📂 Project Files Used

'readme.md' → Project explanation and details

'statement.md' → Problem statement for submission

'utils.py', 'calculator.py', 'main.py' → Source code

##🔨 Steps to Install and Run the project

1. Install Python
2. Download the Project Files
3. Open the Project Folder
4. Run the Python Script

##🧪 Instructions for Testing the Project

1. Test with Simple Inputs
   - Provide small number of participants.
   - Enter equal contributions
   - Verify if the output matches expected results.
  
2. Test with Unequal Contributions
   - Enter different contribution amounts.
   - Ensure the calculator correctly shows who will receive or pay extra.
  
3. Test Error Handling
   - Try entering a non-numeric value for amount.
   - Enter zero or negative numbers.
   - Observe whether the program displays proper error messages.
  
4. Test Large Inputs
   - Use a high total bill amount.
   - Increase the number of participants.
   - Check if the program handles large values smoothly.
  
5. Test Boundary Cases
   - One participant only.
   - All participants contributing zero.
   - Total bill amount lower than contributions.
    
##🔍 Example Output

Enter the number of people: 3

Enter the name of participant 1: Shreya

Enter contribution by Shreya: 500

Enter the name of participant 2: Khushi

Enter contribution by Khushi: 300

Enter the name of participant 3: Chanda

Enter the contribution by Chanda: 400

Enter the total bill amount: 600

----------------------BILL SPLIT SUMMARY-----------------------------

Shreya should recieve ₹300.00

Khushi should recieve ₹100.00

Chanda should recieve ₹200.00

