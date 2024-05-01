# Article Scraper and Compiler Program
## This program is designed to run in google colab and scrape / condense content from articles into a condensed version of notes. 
## These notes can be fed into the Info Brief Creator Agent to create a strcutured information brief for outline creation (See other files / readme)
## If URLs left blank, it uses the Google API to pull the top 3 organic results of the primary KW. 

### WARNING - I'm no dev. This code is an abolute mess. It's also got some legacy stuff I don't use anymore and still need to remove, like the FAQ thing... 

###### Setup
## Fill out this info.

primary_keyword = "patient retention strategies" # @param {type:"string"}
context = "This is an informational blog aiming to teach users about the primary keyword. " # @param {type:"string"}
numberOfResults = 3 # @param {type:"number"}
audience = "The audience is medical professionals. " # @param {type:"string"}
url1 = "https://www.sermo.com/resources/patient-retention-strategies/" # @param {type:"string"}
url2 = "https://www.getweave.com/patient-retention/" # @param {type:"string"}
url3 = "https://healthcaresuccess.com/blog/medical-marketing-advertising/the-9-essentials-of-improving-patient-retention.html" # @param {type:"string"}

###### Libraries, Google and OpenAI APIs

!pip install selenium
!pip install openai
!apt-get update
!apt-get install chromium chromium-driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import openai
from openai import OpenAI
import requests
from bs4 import BeautifulSoup
import re
import time
from IPython.display import Javascript
import json

# Google Search API
api_key = "insert your api key here"
search_engine = "custom search engine key here"

#OpenAI
client = OpenAI(
    api_key = 'openai api key',
)

###### Scraping and other stuff

# SCRAPING
def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

def fetch_or_use_provided_urls(primary_keyword, manual_urls=None):
    if manual_urls and len(manual_urls) > 0:
        # Manual URLs provided, convert them to the expected format
        return [{'title': 'Manual Entry', 'url': url} for url in manual_urls]
    else:
        # No manual URLs provided, fetch them
        return parse_results(primary_keyword)

def parse_results(primary_keyword):
    api_endpoint = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine}&q={primary_keyword}&num={numberOfResults}&gl=US"
    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()

        results = []
        search_results = response.json().get('items', [])
        for item in search_results:
            title = item.get('title')
            link = item.get('link')
            results.append({'title': title, 'url': link})

        return results

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def scrape_content(driver, url):
    try:
        driver.get(url)
        time.sleep(2)  # Wait for the page to load

        content_elements = driver.find_elements(By.XPATH, "//h1|//h2|//h3|//h4|//h5|//h6|//p")
        content = f"URL: {url}\n\n"

        for element in content_elements:
            tag_name = element.tag_name
            element_text = element.text.strip()

            if tag_name in ["h1", "h2", "h3", "h4", "h5", "h6"] and not element_text:
                continue

            if tag_name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                content += f"\n{tag_name.upper()}: {element_text}\n"
            else:
                content += f"{element_text} "

        return content.strip()
    except Exception as e:
        print(f"Error occurred while scraping {url}: {e}")
        return f"Error occurred while scraping {url}: {e}"
def extract_headings(article):
    # Assuming the article content is structured with headings marked as 'H1:', 'H2:', etc.
    lines = article.split('\n')
    headings = [line for line in lines if line.startswith(('H1:', 'H2:', 'H3:', 'H4:', 'H5:', 'H6:'))]
    return '\n'.join(headings)

def save_headings_to_file(*articles):
    with open('headings.txt', 'w') as file:
        for article in articles:
            headings = extract_headings(article)
            file.write(headings + '\n\n')

# CHUNK AND PROCESS
def split_into_chunks(text, chunk_size=25000):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def process_articles(article1, article2, article3):
    all_chunks = split_into_chunks(article1) + split_into_chunks(article2) + split_into_chunks(article3)

    with open('information_foraging_document.txt', 'a') as file:
        for chunk in all_chunks:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo-16k",
                temperature=0.0,
                max_tokens=4000,
                messages=[
                    {"role": "system", "content": spr_generator},
                    {"role": "user", "content": chunk}
                ]
            )

            # Extract the message as a string
            message = completion.choices[0].message.content

            # Write the completion message to the file
            file.write(message)
            file.write("\n\n--- END OF COMPLETION ---\n\n")


def secondary_keyword_faqs(secondary_keywords):
    # Generate FAQs
    faq_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": faq_creator},
            {"role": "user", "content": f"Please create an FAQ from this list of keywords, answering every unique search intent found in this list of keywords: {secondary_keywords}"}
        ],
        temperature=0.0,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    generated_faqs = faq_completion.choices[0].message.content

    # Generate SPR based on the FAQs
    spr_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": spr_generator},
            {"role": "user", "content": generated_faqs}
        ],
        temperature=0.0,
        max_tokens=4000
    )
    spr_message = spr_completion.choices[0].message.content

    # Append FAQs and SPR to the document
    with open('information_foraging_document.txt', 'a') as file:
        file.write(spr_message)
        file.write("\n\n--- END OF FAQs SPR ---\n\n")

    return generated_faqs

def create_info_brief():
  with open('information_foraging_document.txt', 'r') as file:
      info_doc = file.read()

      completion = client.chat.completions.create(
          model="gpt-4",
          temperature=0.7,
          max_tokens=4000,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          messages=[
              {"role": "system", "content": info_brief_creator},
              {"role": "user", "content": info_doc}
          ]
      )

      api_output = completion.choices[0].message.content
      with open('info_brief.txt', 'w') as output_file:
          output_file.write(api_output)

def create_outline(primary_keyword):  # Add primary_keyword as a parameter
    with open('info_brief.txt', 'r') as file:
        info_brief = file.read()

        completion = client.chat.completions.create(
            model="gpt-4",
            temperature=0.7,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            messages=[
                {"role": "system", "content": outline_creator},
                {"role": "user", "content": f"# Context\n{context}\n\n# Audience\n{audience}. Please keep this audience in mind throughout the blog outline and writing points.\n{info_brief}"}
            ]
        )

        api_output = completion.choices[0].message.content
        # Use primary_keyword in the filename
        filename = f'{primary_keyword}_outline.txt'
        with open(filename, 'w') as output_file:
            output_file.write(api_output)

def delete_files(file_paths):
    deleted_files = []
    errors = []

    for path in file_paths:
        try:
            os.remove(path)
            deleted_files.append(path)
        except Exception as e:
            errors.append((path, str(e)))

    return deleted_files, errors


# AGENTS
spr_generator = "# MISSION\nYou are an Article Content Analysis Agent, specialized in dissecting articles and presenting their contents as Sparse Priming Representations (SPRs). Your primary mission is to analyze any given article, extract each unique piece of information, idea, fact, or concept, and present them in clear, concise SPR bullet points.\n\n## Sparse Priming Representations (SPR)\nLLMs are a kind of deep neural network. They have been demonstrated to embed knowledge, abilities, and concepts, ranging from reasoning to planning, and even to theory of mind. These are called latent abilities and latent content, collectively referred to as latent space. The latent space of an LLM can be activated with the correct series of words as inputs, which will create a useful internal state of the neural network. This is not unlike how the right shorthand cues can prime a human mind to think in a certain way. Like human minds, LLMs are associative, meaning you only need to use the correct associations to \"prime\" another model to think in the same way.\n\n## Methodology\nRender the input as a distilled list of succinct statements, assertions, associations, concepts, analogies, and metaphors. The idea is to capture as much, conceptually, as possible but with as few words as possible. Write it in a way that makes sense to you, as the future audience will be another language model, not a human. Use complete sentences.\n\n## RULES\n- Focus on extracting unique and relevant information from articles.\n- Convert complex ideas into succinct SPRs.\n- Do not alter the factual content or introduce personal interpretations.\n- Do not include information about the author or company who wrote it, or related resources.\n\n## EXPECTED INPUT\nYou will receive a scraped article output, consisting of headings and body text.\n\n## Expected Output\nSimply output the SPR. The output will be a list of bullet points, each a Sparse Priming Representation of a distinct piece of information, idea, fact, or concept extracted from the article.\n## Output Template\n(Article Title): (Article URL)\n(Content SPR)"
faq_creator = "# MISSION\nYou are an AI agent designed to interpret a list of keywords and generate a list of ideas that address every unique implied search intent associated with those keywords. Your primary mission is to understand the underlying questions or needs that each keyword suggests, particularly in the context of SEO, and to provide creative, relevant ideas that fulfill these intents.\n\n## RULES\n- Analyze the given keywords to discern their implied search intents.\n- Generate creative and relevant ideas that address these intents, not just restate the keywords.\n- Avoid redundancy: if multiple keywords imply the same intent, provide a single set of ideas for that intent.\n- Do not group ideas by keyword, search intent, indent or hierarchy bullet points, or categorize the ideas in any way, simply list them like the output format template\n- Keep your responses concise, utilizing succinct statements and analogies.\n\n## EXPECTED INPUT\nExpect a list of keywords. These keywords may vary in length and complexity and can include multiple keywords with the same implied search intent.\n\n## Expected Output\nA list of ideas, each addressing a unique implied search intent derived from the provided keywords. The output should be concise, utilizing the principles of SPR to ensure brevity and relevance.\n\n## METHODOLOGY\n- Apply SPR techniques to understand and distill the essence of each keyword's implied search intent.\n- Render the interpretation of each keyword as a distilled list of ideas, employing succinct statements, analogies, and metaphors.\n- Ensure the output is tailored for interpretation by another language model, focusing on clarity and conceptual richness.\n## Output Format Template\n- (succinct idea)\n- (succinct idea)\n- (succinct idea)\n- (continued)"
info_brief_creator = "# MISSION\nYou are an AI agent designed to convert unorganized notes into detailed, structured, SEO-optimized information briefs. Your primary mission is to identify the search intent for a topic, create a thesis statement, and elaborate on core ideas with comprehensive details, ensuring a clear, in-depth understanding.\n\n## RULES\n- Identify a 1 sentence search intent for the given topic to align the brief with what users are likely searching for.\n- Create a concise 1-2 sentence thesis statement that encapsulates the main argument or perspective of the brief.\n- Organize the brief into core ideas, thoroughly explaining and articulating each.\n- Structure the brief by listing core ideas and aligning relevant sub-ideas under each core idea.\n- Include as much relevant detail as possible under each core idea to provide depth.\n- Arrange related sub-ideas under their respective core ideas without redundancy.\n- Maintain the original meaning of the notes, using your own words for explanation.\n- Do not add unrelated content or external context beyond the original notes.\n- Rephrase ideas using your own words to maintain originality and avoid plagiarism.\n\n## EXPECTED INPUT\n- Unorganized, potentially detailed notes on a specific topic.\n- Notes may contain repetitive themes or ideas.\n\n## EXPECTED OUTPUT\n- A detailed and structured information brief that follows the output format below strictly without adding or skipping any sections\n- Do not **bold** any text, keep it plain other than the headings.\n\n## Output Format\n## Information Brief \n### Search Intent:  \n(search intent, what the user searching the keyword is looking for)\n\n### Thesis: \n(thesis statement)\n\n### Core Ideas:  \n1.\t(Core Idea Name): (idea explanation)\n    1.1. (Sub-Idea Name): (Sub-idea explanation)\n    1.2. (Sub-Idea Name): (Sub-idea explanation)\n(continued for all core ideas and their sub ideas)\n\n### Sources: \n(print sources' URLs here)"
outline_creator = "# MISSION\\nYour mission is to create structured, informative article summaries based on an information brief. You are to address the search intent at the top, incorporate the thesis statement as the main point, and elaborate on the core ideas and sub-ideas provided. Your summaries should be explanatory, and include practical examples, applications, or methods that align with the thesis.\\n\\n## RULES\\n- All information should be explained as if you are explaining these ideas to the user.\\n- Fully elaborate on core ideas and sub-ideas using direct, explanatory language. Core ideas often (but not always) are H2's, whereas sub points often (but not always) can be placed as H3s.\\n- Avoid general statements, focusing on detailed and fully constructed information.\\n- Headings should have between 2 and 4 short writing points. Choose the best number of writing points to explain the information fully.\\n- Strictly follow an output format, indicating headings with H tags, and writing points with \"-\"s\\n\\n## Section Information\\n- The information in each section should NOT be instructional in any manner. It should always fully explain the information to the reader in its fullest.\\n- Format the section information in multiple bullet points, using as many bullet points needed to fully explain the information. Do not indent bullet points.\\n- Points in the section information should aim to explain and expand upon information in the brief, filling in the gaps to fully and comprehensively explain the information.\\n- Points should be written with shorter, direct, and efficient, and do not need to be complete sentences, just outline the information.\\n\\n### Output Format Example\\nBelow is a sample output for an article summary in your format. You should follow this format and style closely when crafting your own unique outline.\\n\\nH1: Title\\n\\nH2: Heading \\n- Writing point\\n- Writing Point\\n- Writing point\\n- Writing Point\\n\\nH3: Subheading\\n- Writing point\\n- Writing Point\\n- Writing point\\n\\nH2: Heading\\n- Writing point\\n- Writing Point\\n\\n(continued for all sections)"

###### Deleting Old Files Each New Run

# Deletes Files
files_to_delete = ['headings.txt', 'info_brief.txt', 'information_foraging_document.txt']
deleted_files, errors = delete_files(files_to_delete)

print("Deleted files:", deleted_files)
if errors:
    print("Errors encountered:")
    for error in errors:
        print(f"File: {error[0]}, Error: {error[1]}")



###### Processing 

manual_urls = None if not any([url1, url2, url3]) else [url for url in [url1, url2, url3] if url]
results = fetch_or_use_provided_urls(primary_keyword, manual_urls)
urls = [result['url'] for result in results[:3]]  # Ensuring only top 3 URLs are used


# Scrape content from each URL and store in unique variables
driver = web_driver()
Article1 = scrape_content(driver, urls[0]) if len(urls) > 0 else ""
Article2 = scrape_content(driver, urls[1]) if len(urls) > 1 else ""
Article3 = scrape_content(driver, urls[2]) if len(urls) > 2 else ""
driver.quit()  # Close the browser

# Process with GPTs
process_articles(Article1, Article2, Article3)
save_headings_to_file(Article1, Article2, Article3)
#generated_faqs = secondary_keyword_faqs(secondary_keywords)
#create_info_brief()
#create_outline(primary_keyword)
