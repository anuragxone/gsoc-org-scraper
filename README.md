# GOOGLE SUMMER OF CODE ORGANIZATIONS INFO SCRAPER
## This is a simple script written in Python to scrape the organizations information from GSoC website. It lists every organization's name that appeared in GSoC, with frequency of it's appearance and a list of the years that it appeared in.

### Requirements:
- python-3.11 (I used Python 3.11 but you can try other versions also.)
- Packages:
    - selenium-4.12
    ```Python
    pip install -U selenium
    ```

### Running
```Shell
python main.py
```
^ running this will create a text file `gsoc_orgs.txt` in the same directory.

> [!NOTE]
> This repository contains a `gsoc_orgs.txt` file generated on 16th September 2023, which contains information upto year 2022.
