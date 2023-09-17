import time
from collections import defaultdict

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_organizations_2009_2015(driver, year):
    """Get organizations for years 2009 to 2015"""
    url = f"https://www.google-melange.com/archive/gsoc/{year}"
    driver.get(url)
    time.sleep(3)
    elements = driver.find_elements(By.XPATH, '//li[@class="mdl-list__item mdl-list__item--one-line"]//a')
    return [elem.text for elem in elements]


def get_organizations_2016_2023(driver, year):
    """Get organizations for years 2016 to 2023"""
    url = f"https://summerofcode.withgoogle.com/archive/{year}/organizations"
    driver.get(url)
    time.sleep(3)
    elements = driver.find_elements(By.XPATH, '//div[@class="name"]')
    return [elem.text for elem in elements]


def main():
    # Create a dictionary to store organization names and years they appeared
    org_data = defaultdict(list)

    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # Run chrome in headless mode
    with webdriver.Chrome(options=options) as driver:
        for year in range(2009, 2016):
            orgs = get_organizations_2009_2015(driver, year)
            for org in orgs:
                org_data[org].append(year)

        for year in range(2016, 2024):
            orgs = get_organizations_2016_2023(driver, year)
            for org in orgs:
                org_data[org].append(year)

    # Store results in a text file
    with open("gsoc_orgs.txt", "w") as file:
        for org, years in sorted(org_data.items(), key=lambda x: len(x[1]), reverse=True):
            file.write(f"{org} ({len(years)} times): {', '.join(map(str, years))}\n")


if __name__ == "__main__":
    main()
