"""
Playing aroud a bit: Implementing the clip function
"""
def myclip(text: str, max_len:int = 80) -> str:
    """
    Clip each line of the receieved text to be max_len. This function
    wont cut a word in the middle, so it might happen that some lines
    are longer than max_len
    """
    new_text = ""
    lines = text.split('\n')
    for line in lines:
        if len(line) <= max_len:
            new_text += line
        else:
            line_to_split = line
            text_splitted_in_lines = []
            while len(line_to_split) > max_len:
                idx = max_len
                while idx < len(line_to_split) and line_to_split[idx] != ' ':
                    idx += 1
                if idx == len(line_to_split):
                    # There's no space between line_to_split[max_len:len(line_to_split)]
                    # Therefore we cannot split the remainder of this line
                    break
                first_part = line_to_split[0:idx]
                line_to_split = line_to_split[min(idx + 1, len(line) - 1):len(line)]
                text_splitted_in_lines.append(first_part)
            text_splitted_in_lines.append(line_to_split)

            new_text += "\n".join(text_splitted_in_lines)
    return new_text
