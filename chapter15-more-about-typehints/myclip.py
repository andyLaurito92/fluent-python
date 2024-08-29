"""
Comment the following line to see the effects of postpone evaluation of annotations


"""
from __future__ import annotations

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

import inspect

"""
You can get type hints in runtime using inspect.get_annotations().
Type hints are stored as a dictionary in attr __annotations__ 
"""
inspect.get_annotations(myclip)

"""
Big difference: By default, type hints are evaluated at runtime. This might
be a costly operation in terms of both CPU and memory.

Since python 3.7 we can do from __future__ import annotations to force
the python interpreter to postpone the evaluation of annotations. This
causes annotations to be stored in the __annotations__ dictionary as
strings.

By commenting or uncommenting the first line of this file, you can see
the difference in the return value of inspect.get_annotations
"""
