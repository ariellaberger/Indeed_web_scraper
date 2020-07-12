# Indeed_web_scraper


### Brief Description

- Training project to parse job postings from Indeed.com

### Installation

- See `requrements.txt`

### Usage

- main_passage.py may be executed as python script with an argument.

    ```
    usage: main_passage.py <depth>.
    <depth> - the number of pages to parse; each page typically consists of 10 job positions.
    <depth> - must be more than 10 and less or equal to 50 pages. Currently the number of pages
              is rounded to the nearest ten.
    ```

The output of main.py is the list of URLs which is further processed.
    
    
- main_passage may be imported to other modules such as Web_Scraping_AB1.py.

```python
    import main_passage
    BASE_URL = "https://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=New+York&start="
    print(main_passage.parse_pages(BASE_URL, 12))
```

### Description

**Current project implementation**

- Currently, the project consists of two modules: `main_passage.py` and `Web_Scraping_AB1.py`
    - #### main_passage.py
        - The module sequently parses pages with job posting snippets and grabs individual urls for further parsing by `    Web_Scraping_AB1.py.`The module has two key functions: `parse_positions_from_page()` and `parse_pages()`
            - `parse_positions_from_page()` works with pages where job posting snippets are published.
            - `parse_pages()` merges information obtained by `parse_positions_from_page()`
        - Additional information is stored in a Pandas dataframe: **Title, Location, Company, Salary, Synopsis, URL**. Currently this dataframe is not exposed for external functions.
        - Function `parse_position_page()` is currently commented out. It might be used in `Web_Scraping_AB1.py` module.

    - #### Web_Scraping_AB1.py
        - The module takes an input of a list of URLs, each URL being a full job posting. The module parses each full job
            description, pulling out complete information including the entire job description.

### Issues

- Some parsed results show inconsistencies that are highlighted upon browsing. This requires further investigation.
- Some records in the dataframe of main_passage.py show duplications, to which further investigation is required.

### TODOs

- Make requirements.md readable
- Improve script execution with arguments
    - depth argument may be redesgined to more intuitive.
- Improved parser of the individual page with full job description.
    - Currently, the dataframe imports the text in the entirety. A parse according to hierarchy in formatting (e.g. bulletpoints,      paragraph order) may be in order. Noted that the format for job description vastly differs between records. 
- Further potential steps. It should be mentioned that our code currently uses 'Data Scientist' as search term but we are not 
restrcited to that.
    - Determine and investigate value added use cases. A few thoughts:
        - i.e. if ultimate goal to determine most frequent job requirements- method to extract job description highlights
        - i.e. if ultimate goal to determine analyze 'staleness' of job posting and other variable such as ZIP code
        - i.e. if uttimate goal to extract differentiated job roles across different regions (Aus, US UK)
        - i.e. if ultimate goal to seek corporate intelligence, to run global analysis of recruiting hires globally.
- Based on what will be determined as next steps, we would propose a database structure. Data outputs will be saved to a database upon which queries (SQL based) will be run, for further analysis.
