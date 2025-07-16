vowel = ('a','e','i','o','u')
starts_with = ('xr','yt')

def split_word(word: str):
    """
    split word into until first vowel
    return tuple with first consonents and rest of word
    """

    if not word:
        return None
    
    consonents_list = []
    for char in word:
        if not char in vowel and char.isalpha():
            consonents_list.append(char)
        else:
            break
    
    if not consonents_list:
        return None

    consonents = ''.join(consonents_list)
    rest_of_word = ''.join(word.split(consonents)[1:])
    return (consonents, rest_of_word)

def translate(text: str):
    result = []
    for word in text.split():
        if word.startswith(vowel) or word.startswith(starts_with):
            result.append(text + "ay")
        elif "qu" in word:
            x = word.split("qu")
            result.append(f"{x[1]}{x[0]}quay")
        elif "y" in word:
            y = word.split("y")
            result.append(f"y{y[1]}{y[0]}ay")
        else:
            first, rest = split_word(word)
            if first and rest:
                result.append(rest + first + "ay")

    return ' '.join(result)

