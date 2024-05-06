# SEO Outline Creation Process
My current, personal system and process for creating an article or content outline with SEO in mind. This process aims to gather all of the relevant technical information, as well as provide a repeatable and efficient system for creating blog outlines to save time across content creation. 

[See More Of My SEO Related Work](https://rkseo.xyz)

## Context
This process is built off of a few other pieces of my process. In an attempt to make this information more relevant, I want to outline a few short pieces of context that relate to how I get to this point, and how I've gathered some of the information mentioned here. 

My content planning all begins with cluster research and creation. I have a full repository I'm working on to fully map this process out, but for now just know that the cluster ends with a list of articles, each which has anywhere from one to several hundred keywords. This list of grouped keywords is what I'm using to select my primary and secondary keywords as mentioned below. This also allows me to plan out internal linking structure and topical coverage before writing the articles. 

**Relevant Repos:** 
- Cluster Creation Process (Coming Soon)
- Authority Tiers: My Implementation of the Avalanche theory / process (Coming Soon)
### Process Overview
The process is based into two primary phases of information gathering: SEO Information and "Idea" or "Content" information. I've gone into great detail below as to how I gather the relevant information from each of the below sections. For now here is an outline or overview of the process. 

- **SEO Information**: This is the essential information you'll want to gather to make sure an article has as much of the relevant SEO optimization baked into the first draft. 
	- Primary Keyword: Selection of the primary keyword based on the cluster creation and website's current authority tier. 
	- Secondary Keywords: Secondary or keyword variations. Effectively, keywords that can rank with the same page as your primary keyword. 
	- Semantic Keywords: Semantic terminology we'd like to mention on the page alongside the keywords.
	- URL Slug: Simply put set it to your primary keyword. 
	- Word Count: Average the top 3-5 articles. 
	- Internal Links: Other pages on your website you want to link this page to. 
	- External Links: Exactly like internal, but external - who would have guessed?
- **"Content" Information Gathering**
	- Search Intent: What is the user searching for? 
	- Thesis: What's the main point of your article?
	- Core Ideas: The most important ideas or information you need to include. 
## SEO Information
This is the part of my workflow that covers the more mathematical parts of SEO. Keyword optimization, semantics, internal linking, word count, URL slug, and so on. 
### 1. Primary Keyword
This covers the identification and implementation of primary and secondary keywords. These are the keywords that most directly reflect the topic and search intent for the article you are writing, and are the main keywords you are aiming to rank the content on. 

I typically will select the primary keyword based on my website's authority tier. This tier is based on calculations I run, built off of the [SEO Avalanche Theory](https://www.buildersociety.com/threads/seo-avalanche-technique-ranking-with-no-resources.5114/). I am working on a full repo about my approach to this topic, but for now just know that I'm aiming to select a primary keyword my website should be able to rank on with this idea in mind. 
### 2. Secondary Keywords

Secondary keywords (or keyword variations) for me are simply terms that can rank with the same page due to search intent overlap. How do you know if a keyword should be a secondary keyword or if it should get it's own article?  Look to the Google results and compare search intents. 

If the search results are showing the same pages generally on both queries, you're likely safe to target them both on the same page. Additionally look at search intent. If they have the same intent great. But look past the basic informational, commercial, etc. Are they the same style or type of information.

For example, the keyword "EHR definition" and "what is an EHR" both have the same search results, despite being different queries with different search volumes. If I'm writing an article targeting "what is an EHR," odds are "EHR definition" will be one of the secondary keywords. 
### 3. Semantic Terms 
Semantic terminology is basically: what words would you typically also mention if you were discussing your primary keyword? For example if you're talking about orthopedic surgery, odds are you'd also mention joint replacement, recovery, etc. (pull semrush). 

There's a handful of ways to pull these. The easiest is something like semrush's content tool. 

The way search engines are analyzing these semantic terms are through nlp algorithms. If you really want you can run a vector analysis with something like Google's BERT. Which is open source. (I need to make an analysis tool with BERT )
### 4. URL Slug
Choosing your URL, I try to incorporate the broadest / highest rank keyword into the slug, along with the current tier you're targeting. This means that if you need to come back and refresh your page to rank on that keyword, you don't need to change your URL slug. Plus, URL slug length can be pretty long and it doesn't affect anything. 

Nobody is typing in your URL, and if you really need a simple type-able URL for another reason, use a redirect

(Content targeting both keywords can I crawl top 3 from all the keywords to extract ideas and get the best outline?)
### 5. Word Count
Despite what I've still heard people say in 2023, there is *not* a magic word count to that Google or other search engines are looking for with your content. 

No - it's not 800 words because that's what Forbes Agency Council limits their posts to, those rank well because it's Forbes, not because of the word count. (Yes, I've heard this...)

The word count of your article should depend on - like everything else here - what the top ranking articles in the space look like. Google understands that not all queries need the same amount of content to answer the question. "What color is an apple" likely needs fewer words to answer the query than "Steps to grow an apple tree." As a result, the top ranking pages for queries will likely be different. 

I like to go based off of the average word count of the top 3-5 *relevant* articles. This means I'm looking at the word counts of articles that are ranking based on their content and relevance to the term, and I try to weed out either odd search results, or domains that have an overly high authority. 

Sometimes a search result has scattered results. Take "MIPS" for example. MIPS has a variety of meanings, and depending on if you're talking about a bike helmet or healthcare, you'll have different content needs. If you're writing about the bike helmet, I'd take the top 3 articles about MIPS helmets. 

In other cases, you'll find that there's a very high-ranking domain with a very low word count. If the CMS is ranking in the top 5 with ~300 words, but all the other pages are ranking with 1200 - 1400 words, I'd aim to average the pages excluding the CMS. The CMS page is likely ranking *despite* the lack of content, and the authority the site has is carrying it. Unless your site has CMS level authority, it's best to provide more information than the CMS. 

But overall I take this average, and stick to it as a general rule, not a hard and fast one. I tell my writers +/- 12% and don't overthink it. I don't quite remember where I heard that 12% but it's been a decent number to go with so I'm sticking with it for now. 
### 6. Internal Links
Internal linking is something that I'll sometimes plan in an outline. Admittedly however, the workflow often makes more sense to manually do this after the fact, but if all your pages are going live at once within your cluster, great go for it. 

I'm generally linking based on a silo structure, with 3 tiers, and building them up to the target term. I've got a whole repo / article on my clustering approach so go check that out for more info. 
### 7. External (Outbound) Links
Often times a relevant and authoritative website will link out to other relevant and authoritative websites, and Google understands that and to some extent wants to see that. Or at least that seems to be the going theory / best practice in the SEO community. 

Admittedly, this is a test I want to devise in the future to see how much an impact outbound links have on a page's ranking power, and whether or not the end-destination of those links even matters. For all I know at the moment the sheer existence of outbound links could be all that matters. But I just haven't had the time to run that test properly. (Maybe I'll come back to this and link to the test if I ever do that...)

Typically I'm gathering these links as I do content research. As I find sources or other pieces of information that would be valuable to link out to, I'm adding them in the outline with notes for the writers. 

---
## Content / Idea Information Gathering
Before I even start thinking about headings and an outline, I like to start with information foraging. I think it's important to think about the information and value you want to provide as a fully separate step from organizing it, rather than trying to gather and organize it all at once. 

Information foraging is the process of gathering all the core ideas from competitive articles. The simplest way to do this is to run through the article yourself and create a bullet point list of every relevant or important idea you come across. 

This information foraging phase is also a great way to utilize an LLM such as GPT 3.5. Below is an agent or system prompt, based on [David Shapiro's Sparse Priming Representations](https://github.com/daveshap/SparsePrimingRepresentations), that aims to accomplish just this. 

[Article Condenser ("SPR" Creator)](https://github.com/krutzar/seo-outline-creation-process/blob/main/article-condenser-spr-creator.md)

My recommendation would be to use this AI agent's output, paired with your own, to create a comprehensive information foraging output. If you're analyzing 3 competitor articles, you should have 4 sections in your Information Foraging document. One AI output for each article, and a Fourth "human notes" for extra findings you gleam from all the articles.
### Search Intent & Thesis
These are relatively straightforward, but important to making sure your article is focused on the right information. 

Search intent is simply answering "what informatoin is the user looking for when they search this query in a search engine." This can be implied through the keyword, as well as by checking search results. Making sure search intent is aligned when putting together your article is maybe the most important piece, as if the search intent is misaligned it'll be an uphill battle to get your content ranking well. 

Thesis is effectilvy the most central and distilled answer to your search intent. What your main point for the article is, and ensuring that it addresses what the user is looking for. 
## Extracting Core Ideas
This is the fundamentals of structuring the ideas in the blog. I start this out by simply running through the top competition blogs and noting all the unique ideas with bullet points. From there you can start to get an idea around what the most important ideas are. 

You can then go and do this for the other top ranking blogs. I tend to do the top 3-5, but you can also extract ideas from further down the list, or even from secondary keywords. 

I've also automated this part of the process with a series of scraping requests and GPT3.5 API calls. Though this often does a pretty good job, I always make a point to trim information from the output, as well as check to make sure there's no extra info I'd like to add in order to make the article better or more unique. 
## Outline & Headings
Once you're done trimming and refining your content brief you can start mapping things into headings. 

Generally I'll want to address the search intent and thesis up top as early in the article as possible. Keep this concise and be valuable to the user.  

Then you can start mapping core ideas to H2 and H3 headings. To get a starting point, I've also got an AI/LLM agent that does this for you. That being said it fairly strictly will map core ideas and subpoints to H2s and H3s respectively, so spend some time sorting through all this. 

This is the part you'll probably want the most human intervention with as it's the part that's the most "creative" so to speak. Make sure you're organizing info in ways that make the most sense, and make sure your writing points make sense. 

### Creating Your H1
I'm not going to go super into detail as there's plenty on H1 best practices out there, but you'll likely want to create your H1 heading as it's own task, as it's one of the 4 most important keyword optimization elements (alongside your URL slug, meta title, and mentioning the KW throughout the body)

Here's some guidelines
- Put the keyword in the H1 title. Ideally up front. 
- Keep it around 55 characters so it shows fully in the SERP
- Make it engaging / clickable, look at competition. 

Often I'll use this tool to compare title ideas: [IsItWP Headline Analyzer](https://www.isitwp.com/headline-analyzer/)

---
### Examples, Templates, Outputs
- [Outline Template](https://github.com/krutzar/seo-outline-creation-process/blob/main/Blog%20Outline%20Template.docx)
- [Outline Example](https://github.com/krutzar/seo-outline-creation-process/blob/main/Finished%20Outline%20Example.docx)

#### Links to Resources Mentioned
- [Scraper & Compiler Program](https://github.com/krutzar/seo-outline-creation-process/blob/main/article-scraper-and-compiler-program.py)
- [Article Condenser ("SPR" Creator)](https://github.com/krutzar/seo-outline-creation-process/blob/main/article-condenser-spr-creator.md)
- [Research Brief Creator Agent](https://github.com/krutzar/seo-outline-creation-process/blob/main/research-brief-creator.md)
- [Outline Creator Agent](https://github.com/krutzar/seo-outline-creation-process/blob/main/outline-creator.md)
- [IsItWP Headline Analyzer](https://www.isitwp.com/headline-analyzer/)
- [Google Search API](https://developers.google.com/custom-search/v1/overview)
- [OpenAI API](https://openai.com/index/openai-api)
