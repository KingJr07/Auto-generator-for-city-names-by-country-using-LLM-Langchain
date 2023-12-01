## README

**City Name Autogenerator by Country using LLM Langchain**

This project uses an LLM (Large Language Model) model and Langchain to generate realistic and plausible city names based on a given country.

**Requirements:**

* Python 3.8+
* Pipenv (recommended)
* Langchain
* Access to an LLM API (e.g., OpenAI API)

**Installation:**

1. Clone this repository:
```
git clone https://github.com/bard/city_name_generator.git
```
2. Install the required dependencies:
```
pipenv install
```
3. Set up your LLM API credentials:
* Follow the instructions provided by your chosen LLM API provider to obtain your API key.
* Store your API key securely in a `.env` file within the project directory.

**Usage:**

1. Run the following command to generate city names for a specific country:
```
python city_name_generator.py [-c country_code]
```
2. Replace `country_code` with the desired two-letter ISO 3166-1 alpha-2 country code (e.g., US, GB, IN).
3. Optionally, specify the number of city names to generate with the `-n` flag:
```
python city_name_generator.py -c US -n 10
```
4. The script will generate and print the requested number of city names to the console.

**Example:**

```
python city_name_generator.py -c US -n 5

Output:
* Oakwood Hills
* Sunhaven
* Riverstone Springs
* Meadowbrook Valley
* Silver Creek
```

**Features:**

* Generates realistic and plausible city names based on the provided country.
* Uses Langchain to combine prompts and context for improved accuracy.
* Allows for specifying the number of city names to generate.

**Limitations:**

* Requires access to an LLM API with sufficient capabilities for generating creative text formats.
* Output may vary depending on the chosen LLM model and API provider.
* May occasionally generate unrealistic or nonsensical names.

**Future Enhancements:**

* Implement filtering options for city names based on specific characteristics (e.g., population size, climate).
* Allow for specifying additional context to influence the generated names.
* Integrate with a map service to visualize the generated city locations.

**Contributing:**

We welcome contributions to this project. You can fork the repository and submit pull requests with your improvements and suggestions.
