# Indeed_web_scraper


### Brief Description

- training project to parse job postings from Indeed.com

### Installation

- see `requrements.txt`

### Usage

- main_passage.py can be executed as python script with an argument.

    ```
    usage: main_passage.py <depth>
    <depth> is number of pages to parse; each page typically consists of 10 job positions
    <depth> must be more than 10 and less or equal to 50 pages currently
    number of pages will be rounded to the nearest ten
    ```

    in this case its output is the list of URLs for further processing
    
    
- main_passage can be imported to other modules

```python
    import main_passage
    BASE_URL = "https://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=New+York&start="
    print(main_passage.parse_pages(BASE_URL, 12))
```

### Description

**Current project implementation**

- consists of two modules: `main_passage.py` and `Web_Scraping_AB1.py`
    - #### main_passage.py
        - The module can consequently passage pages with job posting snippets to grab individual urls for further parsing by `Web_Scraping_AB1.py` It has two key functions: `parse_positions_from_page()` and `parse_pages()`
            - `parse_positions_from_page()` is working with pages where job posting snippets are published.
            - `parse_pages()` merges information obtained by `parse_positions_from_page()`
        - Additional information is stored in a Pandas dataframe: **Title, Location, Company, Salary, Synopsis, URL**. Currently this dataframe is not exposed for external functions.
        - Function `parse_position_page()` is currently commented out. It might be used in `Web_Scraping_AB1.py` module.

    - #### Web_Scraping_AB1.py
        - parse an individual page with full description of a job position

### Issues

- sometimes parsing results are not the same as we can see with regular browsing (the issue requires further investigation)
- some records in dataframe are duplicated (further investigation is also needed)

### TODOs

- improve script execution with arguments
    - depth argument can be interpreted differently by a user
- improve parser of an individual page with full description of a job position
    - find and store publishing date of a job posting
- implement saving parsing results to a csv file
    - next saves should avoid duplication of records
- next steps
    - describe different cases of working with project, for example:
        - analyse requirements for job applicants
    - based on these cases propose database structure
    - store results of parsing in MySQL database