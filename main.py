import scrape
import fileprocessing
import memory


def operation(types, limiter):
    scraper = scrape.Scraper()  # create a scrape object
    extractor = scrape.Extractor()
    testCase = scraper.urlScrape(f'https://maxappliances.ca/product-category/{types}/')
    # scraper.beautify(scraper.memory)  # print the links
    # print(scraper.memory)
    extractor.prepare_to_extract(scraper.memory, limiter)
    # print(extractor.content_per_url)
    for item in extractor.content_per_url:
        extractor.get_details(item)
    # print(extractor.appliances)
    for appliance in extractor.appliances:
        fileprocessing.store(appliance.name, appliance.img, appliance)
    memory.memorize(extractor.appliances, f"{types}")
    choice5 = input("Search for Depth? (Y/N):")
    if choice5.strip("") == "Y":
        choice6 = input("Integer entry: ")
        extractor.testDepth(choice6)
    return extractor.appliances

# TODO: look on all pages
# TODO: Search by colour
# TODO: Washing machines
# TODO: Search by Brand
# TODO: Dryer machines
# TODO: OPEN BOX or USED
# TODO: json file for efficient memory storage, that way we do not have to keep downloading all appliances
#       we can simply update the appliances
# TODO: automated upload to kijiji using json
# TODO: automated upload to facebook using json
# TODO: related appliances by size or price range


if __name__ == '__main__':
    print("                                           _ _                           \n",
          " _ __ ___   __ ___  __   __ _ _ __  _ __ | (_) __ _ _ __   ___ ___  ___ \n",
          "| '_ ` _ \ / _` \ \/ /  / _` | '_ \| '_ \| | |/ _` | '_ \ / __/ _ \/ __|\n",
          "| | | | | | (_| |>  <  | (_| | |_) | |_) | | | (_| | | | | (_|  __/\__ \ \n",
          "|_| |_| |_|\__,_/_/\_\  \__,_| .__/| .__/|_|_|\__,_|_| |_|\___\___||___/\n",
          "                             |_|   |_|                                  ")
    print("The permissable types are:")
    print("dishwashers     refrigerators    microwaves    stoves    televisions")
    print("washer-dryer-sets    wall-ovens")
    permissable = ['dishwashers', 'refrigerators', 'microwaves',
                   'stoves', 'televisions', 'washer-dryer-sets',
                   'wall-ovens']
    choice = input("Choose a type: ")
    print(f"How many appliances do you wish to download?")
    choice2 = input("Integer entry: ")
    if choice in permissable:
        appliances = operation(choice, int(choice2))

