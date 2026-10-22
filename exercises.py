def every_other_element(arr):
    """
    Task:
        Given an array return the elements at the odd indices

    Hint: This can be done in a one-liner using a list comprehension but you're welcome to use a for-loop, too
    """
    return arr[1::2]


def is_palindrome(in_str):
    """
    Task:

    Determine if an input string is a palindrome. There are multiple ways of doing this but you should try doing this with
    a for-loop (you will have to do some indexing) and using string slicing.

    Additional task:
        - does your solution work with strings and lists?
    """
    return in_str == in_str[::-1]


def fizzbuzz(n):
    """
    Task:
    Given an integer n, return a string array answer (1-indexed) where:

         answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
         answer[i] == "Fizz" if i is divisible by 3.
         answer[i] == "Buzz" if i is divisible by 5.
         answer[i] == i (as a string) if none of the above conditions are true.

    """
    answer = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))

    return answer


def happy_numbers(n):
    """

    Context:

    A happy number is a number defined by the following process:

        Starting with any positive integer, replace the number by the sum of the squares of its digits.

        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

        Those numbers for which this process ends in 1 are happy.

    Task:
        Return true if n is a happy number, and false if not.
    """
    
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        total = 0

        for digit in str(n):
            total += int(digit) ** 2

        n = total

    return n == 1


def nth_fibonacci_number(n):
    """
    Context:
    A Fibonacci number is a number where the i-th Fibonacci number is the sum of the i-1th and i-2 Fibonacci numbers i.e.

        F_i = F_{i - 1} + F_{i - 2}

    A natural way of calculating this is via recursion.

    Task:
        When the input is 0 or negative, it should return 0. When the input is 1 or 2 it should return 1. In all other cases it should follow the recurrence formula we specified earlier.

        You may assume that the input number is greater-than-or-equal-to 0
    """
    
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return nth_fibonacci_number(n - 1) + nth_fibonacci_number(n - 2)



def safe_divide(numerator, denominator):
    """
    Context:
        1) there are multiple ways to handle errors:
            - Look Before You Leap (LBYL)
            - Easier to Ask Forgiveness Than Permission ( EAFP )
        the gist of these are that in one you defensively program, but in the other you let the error occur and then recover.
        There are arguments for one over the other, but we will make you use the EAFP approach here.

        For more information see: https://realpython.com/python-lbyl-vs-eafp/

    Task:
        Division by zero in python throws an exception: ZeroDivisionError. However, we might want to recover from this!

        For this task, do not check if the denominator is zero. Instead, catch the exception and return a tuple of the numerator, denominator, and a string describing what happened. If the division is successful, return the quotient
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return (numerator, denominator, "Denominator cannot be zero")


def count_frequencies(in_str, ignore_case=False):
    """
    Task:
        count the frequencies of the words coming into `in_str`. There is an optional argument
        that the user can pass in where they want to ignore the case of the words.

        Return a dictionary where the keys are the words and the values are the counts

    Hint:
        You might find the "split" and "lower" functions useful here
    """
    words = in_str.split()
    if ignore_case:
        words = [word.lower() for word in words]

    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


#####################################
# Simple test Cases:
# Note: the following tests do not test all the edge-cases! You should think through
#       them and add any others that might be necessary
#####################################


def test_every_other_element():
    assert every_other_element([1, 2, 3]) == [2]
    assert every_other_element(["uh-oh"]) == []


def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("wow") == True


def test_fizzbuzz():
    assert fizzbuzz(3) == ["1", "2", "Fizz"]
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_happy_numbers():
    assert happy_numbers(4) == False
    assert happy_numbers(13) == True


def test_fibonacci():
    assert nth_fibonacci_number(8) == 21
    assert nth_fibonacci_number(10) == 55


def test_safe_divide():
    # Normal division returns the quotient
    assert safe_divide(10, 2) == 5
    assert safe_divide(7, 2) == 3.5

    # Division by zero is recovered from: (numerator, denominator, message)
    result = safe_divide(10, 0)
    assert result[0] == 10
    assert result[1] == 0
    assert isinstance(result[2], str)


def test_count_frequencies():
    assert count_frequencies("the cat the dog") == {"the": 2, "cat": 1, "dog": 1}

    # Case matters by default
    assert count_frequencies("The the") == {"The": 1, "the": 1}

    # ...unless we ignore it
    assert count_frequencies("The the", ignore_case=True) == {"the": 2}

    # Edge case: empty string
    assert count_frequencies("") == {}


if __name__ == "__main__":
    test_every_other_element()
    test_is_palindrome()
    test_fizzbuzz()
    test_happy_numbers()
    test_fibonacci()
    test_safe_divide()
    test_count_frequencies()
