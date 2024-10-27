def dog_years(human_years):
    
    """
    Create a program that counts a dog's age in human years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """

    #enter your code here
    con_1 = 10.5
    con_2 = 4
    dog_years = 0
    if human_years <= 2:
        for i in range(human_years):
            dog_years = dog_years + con_1
    else:
        dog_years = con_1 * 2
        human_years = human_years - 2
        dog_years += human_years * con_2
    if dog_years != float:
        dog_years = int(dog_years)
    
    return "The dog's age in dog years is " + str(dog_years)

def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """
    #enter your code here
    fizz_buzz = "FizzBuzz "
    fizz =  "Fizz "
    buzz =  "Buzz "
    list_num = ""
    output_set = ""
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            list_num += fizz_buzz
        elif i % 3 == 0:
            list_num += fizz
        elif i % 5 == 0:
            list_num += buzz
        else:
            list_num += str(i) + " "
    if num % 3 == 0 and num % 5 == 0:
        output_set = fizz_buzz
    elif num % 3 == 0:
        output_set = fizz
    elif num % 5 == 0:
            output_set += buzz

    return output_set + "(" + str(num) + ") => " + list_num

def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    Input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7} ##talk about glazing!!##
    ```
    """
    #enter your code here
    sentence = sentence.split(" ")
    dict_ouput = {}
    for word in range(len(sentence)):
        dict_ouput[sentence[word]] = len(sentence[word])

    return dict_ouput


def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36 ##Was using ^ instead of ** supposed to be a trick??##
    ```
    """
    #enter your code here
    number = str(number)
    cube_sum = 0
    for i in range(len(number)):
        cube_sum = cube_sum + int(number[i]) ** 3

    return cube_sum

if __name__ == '__main__':
    dog_years(15)
    print()
    fizzbuzz(15)
    print()
    word_lengths("Yankho Chantel Maria Saliji Sponge Bob Big Mom is amazing")
    print()
    cube_sum(123)