function decode(s) {
    // Reverse the string of digits
    const reversedStr = s.split('').reverse().join('');
    
    // Initialize an empty array to store ASCII characters
    const asciiChars = [];
    
    // Iterate through the reversed string
    let i = 0;
    while (i < reversedStr.length) {
        // Check if the current substring has 3 digits
        if (i + 2 < reversedStr.length && parseInt(reversedStr.substr(i, 3)) >= 100) {
            asciiChars.push(String.fromCharCode(parseInt(reversedStr.substr(i, 3))));
            i += 3;
        } else {
            // Otherwise, the current substring has 2 digits
            asciiChars.push(String.fromCharCode(parseInt(reversedStr.substr(i, 2))));
            i += 2;
        }
    }
    
    // Join the ASCII characters to form the decoded string
    const decodedString = asciiChars.join('');
    
    return decodedString;
}

// Test the function
const encodedString = "7010117928411101701997927";
const decodedString = decode(encodedString);
console.log("Decoded string:", decodedString);
