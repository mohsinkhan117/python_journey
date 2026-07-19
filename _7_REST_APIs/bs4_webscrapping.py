import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO


url = "https://www.scrapethissite.com/pages/forms/"


print("\n================= FETCHING THE PAGE =================")
# requests.get() -> downloads the raw HTML of the page as text
response = requests.get(url)
print(response.status_code)     # 200 = success
html_data = response.text       # the full HTML source as one big string
print(len(html_data))           # just to confirm we actually got content

# -----------------------------------------------------------

print("\n================= CREATING A BEAUTIFULSOUP OBJECT =================")
# BeautifulSoup() -> parses raw HTML text into a navigable, searchable structure
# "lxml" is the parser engine - html.parser also works, lxml is just faster
soup = BeautifulSoup(html_data, "lxml")
print(type(soup))

# -----------------------------------------------------------

print("\n================= BASIC NAVIGATION =================")
# Access tags directly like attributes - grabs the FIRST match only
print(soup.title)          # the <title> tag itself
print(soup.title.string)    # just the text inside <title>
print(soup.h1)              # the first <h1> tag on the page
print(soup.a)                # the first <a> (link) tag on the page

# -----------------------------------------------------------

print("\n================= find() — FIRST MATCHING TAG =================")
# find(tag_name, attrs) -> returns the FIRST tag that matches
first_p = soup.find("p")                              # first <p> paragraph tag
print(first_p.get_text())                              # .get_text() -> just the visible text, no HTML tags

first_table = soup.find("table")                        # first <table> tag
print(first_table.get("class"))                         # .get(attr) -> reads an attribute safely (None if missing)

# find() with attribute filters -> narrow down by class, id, etc.
hockey_table = soup.find("table", {"class": "table"})   # this site's main data table
print(hockey_table is not None)

# -----------------------------------------------------------

print("\n================= find_all() — EVERY MATCHING TAG =================")
# find_all() -> returns a LIST of ALL matching tags (not just the first)
all_paragraphs = soup.find_all("p")
print(len(all_paragraphs))                # how many <p> tags exist on the page
print(all_paragraphs[0].get_text()[:100])  # text of the first paragraph, truncated

all_headings = soup.find_all(["h2", "h3"])   # pass a LIST to match multiple tag types at once
print(len(all_headings))

all_links = soup.find_all("a")
print(len(all_links))

# -----------------------------------------------------------

print("\n================= EXTRACTING ATTRIBUTES (e.g. LINKS) =================")
# Tags behave like dictionaries for their attributes -> tag['attr'] or tag.get('attr')
for link in all_links[:5]:                 # just the first 5, to keep output short
    href = link.get("href")                 # the URL the link points to
    text = link.get_text(strip=True)        # visible text, strip=True removes extra whitespace
    print(text, "->", href)

# -----------------------------------------------------------

print("\n================= CSS SELECT() — CSS-STYLE SELECTORS =================")
# select() -> works like CSS selectors (great if you know a bit of CSS)
paragraphs_css = soup.select("p")                 # same as find_all("p")
headings_css = soup.select("h2, h3")               # comma = "or", matches either tag
main_table_css = soup.select("table.table")         # ".table" -> matches class="table"
first_bold_css = soup.select_one("b")               # select_one() -> like find(), just the first match
print(len(paragraphs_css), len(headings_css))

# -----------------------------------------------------------

print("\n================= NAVIGATING THE TREE (PARENT / CHILDREN / SIBLINGS) =================")
# BeautifulSoup keeps the tag hierarchy, so you can move up/down/sideways
sample_tag = soup.find("p")
print(sample_tag.parent.name)          # the tag that CONTAINS this <p> (often a <div>)
print(list(sample_tag.children)[:3])   # direct children of this tag (truncated)
print(sample_tag.find_next("p"))        # the NEXT <p> tag anywhere after this one

# -----------------------------------------------------------

print("\n================= EXTRACTING TABLES: MANUAL BEAUTIFULSOUP WAY =================")
# The "hard way" - manually walking table -> rows -> cells.
# Useful when a table is irregular and pandas can't parse it cleanly.
table = soup.find("table", {"class": "table"})   # this site's hockey team stats table

rows_data = []
if table:
    rows = table.find_all("tr")             # <tr> = table row
    for row in rows:
        cells = row.find_all(["td", "th"])   # <td> = data cell, <th> = header cell
        row_text = [cell.get_text(strip=True) for cell in cells]
        rows_data.append(row_text)

print(rows_data[:3])   # first few rows as plain lists of strings -> team name, year, wins, losses, etc.

# Turning that manually-parsed data into a DataFrame ourselves
manual_df = pd.DataFrame(rows_data[1:], columns=rows_data[0] if rows_data else None)
print(manual_df.head())

# -----------------------------------------------------------

print("\n================= EXTRACTING TABLES: THE EASY PANDAS WAY =================")
# pd.read_html() -> automatically finds EVERY <table> on the page and
# returns a LIST of DataFrames, one per table. Much less code than BeautifulSoup!
tables = pd.read_html(url)          # passing a URL directly works out of the box

# NOTE: if you already have the HTML as a STRING (e.g. from response.text or
# html_data above) instead of a URL, wrap it in StringIO() - newer pandas
# versions require this and will raise a FileNotFoundError otherwise:
#   tables = pd.read_html(StringIO(html_data))
print(f"Found {len(tables)} tables on the page")

# Inspect the table to confirm it looks right
print(tables[0].head())    # the hockey team stats table -> team name, year, wins, losses, etc.

# -----------------------------------------------------------

print("\n================= pd.read_html() USEFUL PARAMETERS =================")
# match="text" -> only return tables that contain this text somewhere (great for narrowing down)
# tables_filtered = pd.read_html(url, match="Wins")

# attrs={"class": "table"} -> only tables with this exact HTML attribute
# tables_filtered = pd.read_html(url, attrs={"class": "table"})

# header=0 -> same meaning as in read_csv(): treat row 0 as column names
# tables_filtered = pd.read_html(url, header=0)

# -----------------------------------------------------------

print("\n================= SAVING A SCRAPED TABLE TO CSV =================")
# Once you've picked the right table out of the list, save it like any DataFrame
chosen_table = tables[0]
chosen_table.to_csv("hockey_team_stats.csv", index=False)
print("Saved to hockey_team_stats.csv")

# -----------------------------------------------------------

print("\n================= BEAUTIFULSOUP vs PANDAS FOR TABLES — WHEN TO USE WHICH =================")
#   SITUATION                                   BEST TOOL
#   -------------------------------------------  ------------------------------------------
#   Clean, standard HTML <table>                  pd.read_html() -> fastest, least code
#   Table has merged cells / irregular structure   BeautifulSoup manual parsing -> full control
#   You need text, links, images, non-table data    BeautifulSoup -> find()/find_all()/select()
#   You need multiple tables at once, quickly        pd.read_html() -> returns them all as a list

# -----------------------------------------------------------

print("\n================= QUICK BEAUTIFULSOUP METHOD CHEAT SHEET =================")
#   METHOD                       RETURNS                         USE CASE
#   ----------------------------  ------------------------------  --------------------------------
#   soup.tag_name                  first matching tag (shortcut)     quick access, e.g. soup.title
#   find(tag, attrs)                 first matching tag                 most common lookup
#   find_all(tag, attrs)               list of ALL matching tags          looping over many elements
#   select(css_selector)                list of matches (CSS-style)        when you know CSS selectors
#   select_one(css_selector)             first match (CSS-style)             like find(), CSS-style
#   get_text()                            visible text, no HTML tags          reading content
#   get(attr) / tag['attr']                 a specific attribute's value        reading href, class, src, etc.