def generate_gray_code(code_size):
    """Generates a list of Gray codes for the given code size.

    Args:
        code_size: The desired code size.

    Returns:
        A list of Gray codes.
    """

    gray_codes = []
    # Base case
    if code_size <= 0:
        return gray_codes

    # Start with the one-bit Gray code
    gray_codes.append("0")
    gray_codes.append("1")

    # Recursively generate Gray codes for larger code sizes
    for i in range(2, code_size + 1):
        # Create a new list to store the Gray codes for the current code size
        new_gray_codes = []

        # Iterate over the Gray codes for the previous code size
        for gray_code in gray_codes:
            # Prefix the previous Gray codes with a 0
            new_gray_codes.append("0" + gray_code)

            # Reverse the previous Gray codes and prefix them with a 1
            reversed_gray_code = gray_code[::-1]
            new_gray_codes.append("1" + reversed_gray_code)

        # Update the list of Gray codes to reflect the new Gray codes for the current code size
        gray_codes = new_gray_codes

    return gray_codes


if __name__ == "__main__":
    code_size = int(input("Enter the desired code size: "))
    gray_codes = generate_gray_code(code_size)

    print("The Gray codes for the given code size are:")
    for gray_code in gray_codes:
        print(gray_code)
