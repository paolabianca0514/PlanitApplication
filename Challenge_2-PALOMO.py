'''CHALLENGE 2: Write a solution to find the character
that has the highest number of occurrences within a certain string, ignoring  case.
If there is more than one character with equal highest occurrences,
return the character that appeared first  within the string.'''
while True:
    from collections import Counter#dictionary sublass for counting hashable items
    user_input = input('Please enter a string:').lower().strip()#accepts user input and converts it to lowercase letters
    count = Counter(user_input)#creates an instance for the input, counts occurence for each letter
    count = max(count, key = count.get)#obtains the letter with the maximum occurence through get function
    print('The character with the highest number of occurence from the string \'{}\' is \'{}\'.'
      .format(user_input,count))#prints the output
