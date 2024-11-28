import string as st
 
def find_minimum(numbers):
    """Returns the smallest number in a list. Return None for an empty list."""
    if not numbers:
        return None
    else:
        return min(numbers)

def calculate_factorial(n):
    """Calculates the factorial of a non-negative integer iteratively.""" 
    x = 1
    for i in  range(1,n+1):
        x *= i
    return x      
print(calculate_factorial(5))

def unique_elements(items):
    """Returns a list of unique elements, maintaining their order."""
    return list(set(items))
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))

def check_palindrome(string):
    """Returns True if the input string is a palindrome, False otherwise."""
    string = string.replace(" ","").lower()
    return string[::-1] == string
print(check_palindrome("racecar"))

def fibonacci_sequence(n):
    """Returns the first `n` numbers in the Fibonacci sequence."""
    a = 0
    b = 1
    new_list = [a,b]
    for i in range(n):
        c = a + b
        new_list.append(c)
        a = b
        b = c
    return new_list[:n]
        
print(fibonacci_sequence(5))

def find_max(numbers):
    """Returns the largest number in a list. Return None for an empty list."""
    return max(numbers)

def find_min(numbers):
    """Returns the smallest number in a list. Return None for an empty list."""
    return min(numbers)

def find_average(numbers):
    """Returns the average of a list of numbers. Return None for an empty list."""
    return sum(numbers)/len(numbers)
print(find_average([1, 2, 3, 4, 5]))

def find_even_numbers(numbers):
    """Returns a list of even numbers in a list."""
    new_lis =[]
    for i in numbers:
        if i % 2 == 0 :
            new_lis.append(i)
    return tuple(new_lis)
print(find_even_numbers([1, 2, 3, 4, 5]))

def find_odd_numbers(numbers):
    """Returns a list of odd numbers in a list."""
    new_li =[]
    for i in numbers:
        if not i % 2 == 0 :
            new_li.append(i)
    return tuple(new_li)
print(find_odd_numbers([1, 2, 3, 4, 5]))

def find_number_of_even_numbers(numbers):
    """Returns the number of even numbers in a list."""
    even_numbers = 0
    for i in numbers:
        if i % 2 == 0 :
            even_numbers +=1
    return even_numbers
print(find_number_of_even_numbers([1, 2, 3, 4, 5]))

def find_number_of_odd_numbers(numbers):
    """Returns the number of odd numbers in a list."""
    odd_numbers = 0
    for i in numbers:
        if not i % 2 == 0 :
            odd_numbers +=1
    return odd_numbers
print(find_number_of_odd_numbers([1, 2, 3, 4, 5]))

def return_list_stats(numbers):
    """Returns a dictionary with the minimum, maximum, average, and number of elements in a list."""

def process_characters(string):
    """Returns a dictionary with the number of letters, digits, and special characters in a string."""
    digit = []
    alphabet = []
    for i in string:
        if i.isdigit():
            digit.append(int(i))
        elif i.isalpha():
            alphabet.append(i)
    return sorted(set(alphabet)),sorted(set(digit))
print(process_characters(['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e']))

def generate_squared_dict(n):
    """Generates a dictionary with the square of numbers from 1 to n."""
    dictionary = {}
    if n >= 0:
        for i in range(1,n+1):
            dictionary[i] = i**2
            
    else:
        for i in range(n,0):
            dictionary[i] =i**2
            
    return dictionary
print(generate_squared_dict(5))
        
        

def convert_to_word_list(string):
    """Converts a string to a list of words."""
    return list(map(lambda x: x.strip("!:?,.'\""), string.lower().split()))
print(convert_to_word_list("i am going to sleep,goodluck to me"))

def letters_count_map(string):
    """Returns a dictionary with the count of each letter in a string."""
    
    string1 = string.lower()
    dict = {}
    for i in st.ascii_lowercase:
        dict[i]= list(string1).count(i)
    return dict
        


def text_to_morse(text):
    """Converts text to Morse code."""
    morse_code = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","1": ".----","2": "..---","3": "...--","4": "....-","5": ".....","6": "-....","7": "--...","8": "---..","9": "----.","0": "-----"," ": " ","!": "-.-.--","\"": ".-..-.","$": "...-..-","&": ".-...","'": ".----.","(": "-.--.",")": "-.--.-","*": "-..-","+": ".-.-.","-": "-....-",".": ".-.-.-","/": "-..-.",";": "-.-.-.","=": "-...-","?": "..--..","@": ".--.-.","_": "..--.-"}
    pass

# if __name__ == "__main__":
#     list1 = [1, 2,3,2, 3, 4, 5]
#     a = set(list1)
#     print(a)
#     print(a)
