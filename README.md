
# VALORANT kill sounds

An API for VALORANT's skin custom kill sound.


## Installation

Install valorant_killsound with pip

```bash
  pip install valorant_killsound
```
    
## Usage

To use the API, you will need to import the `qing762` class from the module and create an instance of the class.

```python
import valorant-killsound
from valorant-killsound import qing762 as val

h = val()
```


## Features

The qing762 class includes the following function:

`Return_Successive_Kill(skinname)`: Retrieves the custom successive kill sound link for the specified skin.

`Return_1_Kill(skinname)`: Retrieves the custom first kill sound link for the specified skin.

`Return_2_Kill(skinname)`: Retrieves the custom second kill sound link for the specified skin.

`Return_3_Kill(skinname)`: Retrieves the custom third kill sound link for the specified skin.

`Return_4_Kill(skinname)`: Retrieves the custom fourth kill sound link for the specified skin.

`Return_5_Kill(skinname)`: Retrieves the custom fifth kill sound link for the specified skin.

`Return_6_Kill(skinname)`: Retrieves the custom sixth kill sound link for the specified skin.

`Return_All_Kill(skinname, type)`: Retrieves all of the custom kill sound links for the specified skin, including the successive kill sound.


### Here is a detailed information of some of the functions in it:
#### Return_Successive_Kill(skinname: str)
The Return_Succesive_Kill is a  function is a tool that retrieves the custom successive kill sound link for a given skin name. The function accepts a single parameter, "skinname," which should be a string representing the name of the desired skin. The function is case-insensitive, meaning that it will treat "SKINNAME" and "skinname" as equivalent.

Upon execution, the function will return a link to the successive kill sound for the specified skin. If the skin does not exist or does not have a custom kill sound, the function will return "None" instead.

Here is an example of how to use the "Return_Successive_Kill" function:
```python
# Import the qing762 class from the ValorantKillSounds module
from valorant-killsound import qing762 as val

# Create an instance of the qing762 class
h = val()

# Retrieve the link for the custom kill sound (successive) of the Sovereign skin
output = h.Return_Successive_Kill("Sovereign")

# Print the output
print(output)
```

#### Return_1_Kill(skinname: str)
The Return_1_Kill is a function that retrieves the custom first kill sound link for a given skin name. The function takes a single parameter, skinname, which is the name of the skin for which you want to retrieve the custom first kill sound link. The skin name should be a string and is case-insensitive.

It would returns a link for the first kill sound of the particular skin. If the skin does not exist or it doesn't have a custom kill sound, it would return None instead.

Here is an example of how you can use the Return_1_Kill function:

```python
# Import the qing762 class from the ValorantKillSounds module
from valorant-killsound import qing762 as val

# Create an instance of the qing762 class
h = val()

# Retrieve the link for the custom kill sound (1 kill) of the Sovereign skin
output = h.Return_1_kill("Sovereign")

# Print the output
print(output)
```
The concept of "Return_1_Kill" to "Return_6_Kill" works the same.

#### Return_All_Kill(skinname: str, type: str)
This function allows you to retrieve the links for all of the custom kill sounds of a particular skin in Valorant. The function accepts a skinname parameter, which specifies the name of the skin for which you want to retrieve the links. It also accepts an optional type parameter, which specifies the format in which you want the output to be returned. If the type parameter is not specified, the default output format is a JSON object.

The function returns a JSON object containing the links for all of the custom kill sounds, including the successive kill sound effect. The keys of the dictionary are successive_kill, 1_kill, 2_kill, 3_kill, 4_kill, 5_kill, and 6_kill, which correspond to the successive kill sound and six of the kill sounds, respectively. If the skin was not found or the skin doesn't have a custom kill sound, the value for that particular sound will be None.

If the type parameter is set to `string` or `str`, the function will return the output as a string.

For example, you can call the function as follows:

Simple mode:
```python
# Import the qing762 class from the ValorantKillSounds module
from valorant-killsound import qing762 as val

# Create an instance of the qing762 class
h = val()

# Retrieve the link for the custom kill sound (1 kill) of the Sovereign skin
output = h.Return_All_Kill("Sovereign")

# Print the output
print(output)
```

Advanced mode:
```python
# Import the qing762 class from the ValorantKillSounds module
from valorant-killsound import qing762 as val

# Create an instance of the qing762 class
h = val()

# Retrieve the link for the custom kill sound (1 kill) of the Sovereign skin
output = h.Return_All_Kill("Sovereign", type="str")

# Print the output
print(output)
```
## Roadmap

The API development roadmap includes the following tasks:

- [ ] Implement an API that returns all of the results in a JSON object, similar to the Honor of Kings API

- [ ] Add additional functions to the API

- [ ] Integrate [Valorant-API](https://valorant-api.com/) into the current API development roadmap


## Usage

Here is a sample list that you can use the module as a starting point:

- Discord bot development
- Web development
- App development

You are free to use the module as you wish, but please remember to adhere to the terms of the [MIT License](https://github.com/qing762/valorant_killsound/blob/main/LICENSE).

## FAQ

#### Q: Is the API free to use?

Yes, the API is free to use.

#### Q: Can I use the API for commercial purposes?

Yes, you can use the API for commercial purposes as long as you follow the terms of the [MIT License](https://github.com/qing762/valorant_killsound/blob/main/LICENSE).

#### Q: How do I report a bug or request a feature?
You can report a bug or request a feature by [opening an issue on the GitHub repository](https://github.com/qing762/valorant_killsound/issues).

#### Q: How do I contribute to the project?
You can fork the project and open a pull request.

#### Q: Can I use the API offline?
No, the API requires an active Internet connection to function. It makes HTTP requests to retrieve the skin kill sound links.
## Acknowledgements

I would like to thank the following individuals or organizations for their contribution to the project:

 - [Valorant Wiki](https://valorant.fandom.com/) for providing the audios files for every weapon skins.


## License

This API is licensed under the MIT License. See [LICENSE](https://github.com/qing762/valorant_killsound/blob/main/LICENSE) for more information.


## Authors

- [@qing762](https://www.github.com/qing762)

