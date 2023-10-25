from pathlib import Path

import wikipediaapi


def write_data_to_txt(country: str, text: str):
    with open(f"countries/{country}.txt", "w") as f:
        f.write(text)


def get_country_description(country_name: str) -> str:
    # Create a Wikipedia API client
    wiki_wiki = wikipediaapi.Wikipedia("CountriesScraper (prrao87@gmail.com)", "en")

    # Fetch the page for the given country
    page = wiki_wiki.page(country_name)

    # Check if the page exists
    if country_name and page.exists():
        # Get the summary (description) of the country
        description = page.summary
        print(f"{country_name}")
        return description
    else:
        print(f"Country not found: {country_name}")
        return "Country {country_name} not found on Wikipedia"


def main(country_names_file: Path) -> None:
    countries = country_names_file.read_text().split("\n")
    for country in countries[:LIMIT]:
        country_description = get_country_description(country.strip())
        # Write to file
        write_data_to_txt(country, country_description)


if __name__ == "__main__":
    countries_dir = Path("countries")
    countries_dir.mkdir(exist_ok=True)
    # Read country names from CSV file
    country_names_file = Path("countries.csv")

    LIMIT = 1000  # Default limit is more than the number of countries on the planet
    main(country_names_file)
