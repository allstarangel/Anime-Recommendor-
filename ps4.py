def word_count(src, dest=None, *words, missing_count=False):
    # Open the source file and read its contents
    with open(src, 'r') as file:
        content = file.read()

    # Create a dictionary to store the word counts
    word_counts = {}

    # Update the word counts in the dictionary
    for word in content.split():
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Print or write the word counts
    if dest is None:
        for word in words:
            count = word_counts.get(word.lower(), 0)
            print(f"{word}: {count}")
        
        # Calculate and print the count of missing words
        if missing_count:
            other_count = sum(word_counts.values()) - sum(word_counts.get(word.lower(), 0) for word in words)
            print(f"other: {other_count}")

    else:
        with open(dest, 'w') as file:
            for word in words:
                count = word_counts.get(word.lower(), 0)
                file.write(f"{word}: {count}\n")

            # Calculate and write the count of missing words
            if missing_count:
                other_count = sum(word_counts.values()) - sum(word_counts.get(word.lower(), 0) for word in words)
                file.write(f"other: {other_count}\n")

# Example function call
word_count('input.txt', None, 'word', 'my', missing_count=True)





class Rectangle:
    def __init__(self, height, length):
        self.height = height
        self.length = length

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
