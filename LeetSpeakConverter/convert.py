def convert(text:str) -> str:
    translation_table = {
        "a":"@",
        "A":"4",
        "B":"8",
        "b":"8",
        "E":"3",
        "e":"3",
        "I":"!",
        "i":"!",
        "L":"1",
        "l":"1",
        "O":"0",
        "o":"0",
        "S":"5",
        "s":"5"
    }
    characters = []
    for char in text:
        if char in translation_table:
            characters.append(translation_table[char])
    cleaned_list = ''.join(characters).split(',')
    return cleaned_list

