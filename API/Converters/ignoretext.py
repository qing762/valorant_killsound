"""
The MIT License (MIT)

Copyright (c) 2022-present qing762

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

class qing556():
    def __init__(self) -> None:
        return
    def title_ignore_of(self, string):
        words = string.split()
        new_string = ""
        for i, word in enumerate(words):
            if word.lower() == "of":
                new_string += word.lower() + " "
            else:
                new_string += word.capitalize() + " "
        return new_string.strip()
    def title_ignore_to(self, string):
        words = string.split()
        new_string = ""
        for i, word in enumerate(words):
            if word.lower() == "to":
                new_string += word.lower() + " "
            else:
                new_string += word.capitalize() + " "
        return new_string.strip()
    def title_ignore_11z(self, string):
        words = string.split()
        new_string = words[0].upper() + " "
        for i, word in enumerate(words[1:]):
            if word.lower() != "11z":
                new_string += word.capitalize() + " "
            else:
                new_string += word[:2] + word[2:].lower() + " "

if __name__ == "__main__":
    b = qing556()