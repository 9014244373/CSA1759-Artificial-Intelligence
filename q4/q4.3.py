from itertools import permutations

def solve_crypt_arithmetic():
    # Define the letters involved in the problem
    letters = "SENDMOREY"
    
    # Generate all permutations of digits for these letters
    for perm in permutations(range(10), len(letters)):
        # Create a dictionary to map each letter to a digit
        letter_to_digit = {letter: digit for letter, digit in zip(letters, perm)}
        
        # Ensure first letters ('S' and 'M') are not zero
        if letter_to_digit['S'] == 0 or letter_to_digit['M'] == 0:
            continue
        
        # Form the numbers based on the mapping
        send = (
            1000 * letter_to_digit['S'] +
            100 * letter_to_digit['E'] +
            10 * letter_to_digit['N'] +
            letter_to_digit['D']
        )
        more = (
            1000 * letter_to_digit['M'] +
            100 * letter_to_digit['O'] +
            10 * letter_to_digit['R'] +
            letter_to_digit['E']
        )
        money = (
            10000 * letter_to_digit['M'] +
            1000 * letter_to_digit['O'] +
            100 * letter_to_digit['N'] +
            10 * letter_to_digit['E'] +
            letter_to_digit['Y']
        )
        
        # Check if the equation holds
        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            print("Mapping:", letter_to_digit)
            return  # Stop after finding the first solution

# Run the solver
solve_crypt_arithmetic()
