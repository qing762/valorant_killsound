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

import urllib.parse, re, requests, json
from bs4 import BeautifulSoup
from Converters.ignoretext import qing556

class qing762:
    def Return_Successive_Kill(self, skinname = None):
        """
        Return the link for the successive kill sound of a particular skin. If the skin does not exist or it doesn't have a custom kill sound, it would return None instead.
        """
        if skinname == None:
            return "None"
        else:
            try:
                if "to" in skinname.lower():
                    skinname = qing556().title_ignore_to(skinname)
                elif "of" in skinname.lower():
                    skinname = qing556().title_ignore_of(skinname)
                elif "11z" in skinname.lower():
                    skinname = qing556().title_ignore_11z(skinname)
                name = str(skinname).replace(" ", "_")
                name = name.capitalize()

                l = f"https://valorant.fandom.com/wiki/{name}_Collection"
                response = requests.get(l)
                soup = BeautifulSoup(response.content, "html.parser")
                audio_tags = soup.find_all("audio")
                for audio in audio_tags:
                    if f"{name}_Kill_Successive.mp3" in audio["src"]:
                        if urllib.parse.urlparse(audio["src"]).scheme:
                            return audio["src"]
            except requests.exceptions.ConnectionError as e:
                raise ConnectionError(f"Your device is not connected to the Internet. Please connect to the Internet and try again. If this problem still occurs, please contact the API owner. {e}")

    def Return_1_Kill(self, skinname = None):
        """
        Return the link for the first kill sound of a particular skin. If the skin does not exist or it doesn't have a custom kill sound, it would return None instead.
        """
        if skinname == None:
            return "None"
        else:
            try:
                if "to" in skinname.lower():
                    skinname = qing556().title_ignore_to(skinname)
                elif "of" in skinname.lower():
                    skinname = qing556().title_ignore_of(skinname)
                elif "11z" in skinname.lower():
                    skinname = qing556().title_ignore_11z(skinname)
                name = str(skinname).replace(" ", "_")
                name = name.capitalize()

                l = f"https://valorant.fandom.com/wiki/{name}_Collection"
                response = requests.get(l)
                soup = BeautifulSoup(response.content, "html.parser")
                audio_tags = soup.find_all("audio")
                for audio in audio_tags:
                    if f"{name.title()}_Kill_1.mp3" in audio["src"]:
                        if urllib.parse.urlparse(audio["src"]).scheme:
                            return audio["src"]
            except requests.exceptions.ConnectionError:
                raise ConnectionError("Your device is not connected to the Internet. Please connect to the Internet and try again. If this problem still occurs, please contact the API owner.")
            except Exception as e:
                raise TimeoutError(f"{e}")

    def Return_2_Kill(self, skinname = None):
        """
        Return the link for the second kill sound of a particular skin. If the skin does not exist or it doesn't have a custom kill sound, it would return None instead.
        """
        if skinname == None:
            return "None"
        else:
            try:
                if "to" in skinname.lower():
                    skinname = qing556().title_ignore_to(skinname)
                elif "of" in skinname.lower():
                    skinname = qing556().title_ignore_of(skinname)
                elif "11z" in skinname.lower():
                    skinname = qing556().title_ignore_11z(skinname)
                name = str(skinname).replace(" ", "_")
                name = name.capitalize()

                l = f"https://valorant.fandom.com/wiki/{name}_Collection"
                response = requests.get(l)
                soup = BeautifulSoup(response.content, "html.parser")
                audio_tags = soup.find_all("audio")
                for audio in audio_tags:
                    if f"{name.title()}_Kill_2.mp3" in audio["src"]:
                        if urllib.parse.urlparse(audio["src"]).scheme:
                            return audio["src"]
            except requests.exceptions.ConnectionError:
                raise ConnectionError("Your device is not connected to the Internet. Please connect to the Internet and try again. If this problem still occurs, please contact the API owner.")
            except Exception as e:
                raise TimeoutError(f"{e}")

    def Return_3_Kill(self, skinname = None):
        """
        Return the link for the third kill sound of a particular skin. If the skin does not exist or it doesn't have a custom kill sound, it would return None instead.
        """
        if skinname == None:
            return "None"
        else:
            try:
                if "to" in skinname.lower():
                    skinname = qing556().title_ignore_to(skinname)
                elif "of" in skinname.lower():
                    skinname = qing556().title_ignore_of(skinname)
                elif "11z" in skinname.lower():
                    skinname = qing556().title_ignore_11z(skinname)
                name = str(skinname).replace(" ", "_")
                name = name.capitalize()

                l = f"https://valorant.fandom.com/wiki/{name}_Collection"
                response = requests.get(l)
                soup = BeautifulSoup(response.content, "html.parser")
                audio_tags = soup.find_all("audio")
                for audio in audio_tags:
                    if f"{name.title()}_Kill_3.mp3" in audio["src"]:
                        if urllib.parse.urlparse(audio["src"]).scheme:
                            return audio["src"]
            except requests.exceptions.ConnectionError:
                raise ConnectionError("Your device is not connected to the Internet. Please connect to the Internet and try again. If this problem still occurs, please contact the API owner.")
            except Exception as e:
                raise TimeoutError(f"{e}")

    def Return_4_Kill(self, skinname = None):
        """
        Return the link for the fouth kill sound of a particular skin. If the skin does not exist or it doesn't have a custom kill sound, it would return None instead.
        """
        if skinname == None:
            return "None"
        else:
            try:
                if "to" in skinname.lower():
                    skinname = qing556().title_ignore_to(skinname)
                elif "of" in skinname.lower():
                    skinname = qing556().title_ignore_of(skinname)
                elif "11z" in skinname.lower():
                    skinname = qing556().title_ignore_11z(skinname)
                name = str(skinname).replace(" ", "_")
                name = name.capitalize()

                l = f"https://valorant.fandom.com/wiki/{name}_Collection"
                response = requests.get(l)
                soup = BeautifulSoup(response.content, "html.parser")
                audio_tags = soup.find_all("audio")
                for audio in audio_tags:
                    if f"{name.title()}_Kill_4.mp3" in audio["src"]:
                        if urllib.parse.urlparse(audio["src"]).scheme:
                            return audio["src"]
            except requests.exceptions.ConnectionError:
                raise ConnectionError("Your device is not connected to the Internet. Please connect to the Internet and try again. If this problem still occurs, please contact the API owner.")
            except Exception as e:
                raise TimeoutError(f"{e}")

    def Return_5_Kill(self, skinname = None):
        """
        Return the link for the fifth kill (ace) sound of a particular skin. If the skin does not exist or it doesn't have a custom kill sound, it would return None instead.
        """
        if skinname == None:
            return "None"
        else:
            try:
                if "to" in skinname.lower():
                    skinname = qing556().title_ignore_to(skinname)
                elif "of" in skinname.lower():
                    skinname = qing556().title_ignore_of(skinname)
                elif "11z" in skinname.lower():
                    skinname = qing556().title_ignore_11z(skinname)
                name = str(skinname).replace(" ", "_")
                name = name.capitalize()

                l = f"https://valorant.fandom.com/wiki/{name}_Collection"
                response = requests.get(l)
                soup = BeautifulSoup(response.content, "html.parser")
                audio_tags = soup.find_all("audio")
                for audio in audio_tags:
                    if f"{name.title()}_Kill_5.mp3" in audio["src"]:
                        if urllib.parse.urlparse(audio["src"]).scheme:
                            return audio["src"]
            except requests.exceptions.ConnectionError:
                raise ConnectionError("Your device is not connected to the Internet. Please connect to the Internet and try again. If this problem still occurs, please contact the API owner.")
            except Exception as e:
                raise TimeoutError(f"{e}")
                
    def Return_6_Kill(self, skinname = None):
        """
        Return the link for the sixth kill (ace) sound of a particular skin. The sixth kill is only available on the Spectrum skin (A skin collaborated with Zedd) or other skins with a sixth kill sound. If the skin does not exist or it doesn't have a custom kill sound, it would return None instead.
        """
        if skinname == None:
            return "None"
        else:
            try:
                if "to" in skinname.lower():
                    skinname = qing556().title_ignore_to(skinname)
                elif "of" in skinname.lower():
                    skinname = qing556().title_ignore_of(skinname)
                elif "11z" in skinname.lower():
                    skinname = qing556().title_ignore_11z(skinname)
                name = str(skinname).replace(" ", "_")
                name = name.capitalize()

                l = f"https://valorant.fandom.com/wiki/{name}_Collection"
                response = requests.get(l)
                soup = BeautifulSoup(response.content, "html.parser")
                audio_tags = soup.find_all("audio")
                for audio in audio_tags:
                    if f"{name.title()}_Kill_6.mp3" in audio["src"]:
                        if urllib.parse.urlparse(audio["src"]).scheme:
                            return audio["src"]
            except requests.exceptions.ConnectionError:
                raise ConnectionError("Your device is not connected to the Internet. Please connect to the Internet and try again. If this problem still occurs, please contact the API owner.")
            except Exception as e:
                raise TimeoutError(f"{e}")

    def Return_All_Kill(self, skinname = None, type : str = None):
        """
        Returns the links for all of the kill sound. Including the sucessive kill sound effect. If the skin was not found or the skin doesn't have a custom kill sound, None would be return instead. It will output out in a JSON format.
        """
        successive_kill = self.Return_Successive_Kill(skinname)
        first_kill = self.Return_1_Kill(skinname)
        second_kill = self.Return_2_Kill(skinname)
        third_kill = self.Return_3_Kill(skinname)
        fouth_kill = self.Return_4_Kill(skinname)
        fifth_kill = self.Return_5_Kill(skinname)
        sixth_kill = self.Return_6_Kill(skinname)

        if type == None:
            return {
                "successive_kill": successive_kill,
                "1_kill": first_kill,
                "2_kill": second_kill,
                "3_kill": third_kill,
                "4_kill": fouth_kill,
                "5_kill": fifth_kill,
                "6_kill": sixth_kill
            }
        elif type == "json":
            return {
                "successive_kill": successive_kill,
                "1_kill": first_kill,
                "2_kill": second_kill,
                "3_kill": third_kill,
                "4_kill": fouth_kill,
                "5_kill": fifth_kill,
                "6_kill": sixth_kill
            }
        elif type == "string":
            return f"""
                'successive_kill': {successive_kill}
                '1_kill': {first_kill}
                '2_kill': {second_kill}
                '3_kill': {third_kill}
                '4_kill': {fouth_kill}
                '5_kill': {fifth_kill}
                '6_kill': {sixth_kill}
            """
        elif type == "str":
            return f"""
                'successive_kill': {successive_kill}
                '1_kill': {first_kill}
                '2_kill': {second_kill}
                '3_kill': {third_kill}
                '4_kill': {fouth_kill}
                '5_kill': {fifth_kill}
                '6_kill': {sixth_kill}
            """
        else:
            return {
                "successive_kill": successive_kill,
                "1_kill": first_kill,
                "2_kill": second_kill,
                "3_kill": third_kill,
                "4_kill": fouth_kill,
                "5_kill": fifth_kill,
                "6_kill": sixth_kill
            }

if __name__ == "__main__":
    qing = qing762()