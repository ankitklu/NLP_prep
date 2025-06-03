import json

from llm_helper import llm

def process_post(raw_file_path, processed_file_path="data/processed_posts.json"):
    enriched_posts = []
    with open(raw_file_path,encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

            # post= {'text':'abc', 'engagement':345}
            # metadata = {'line_count': 10, 'language': 'en', 'tags': ['Mental Health', 'Motivation']}
    
    unified_tags = get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags[tag] for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processed_file_path,encoding='utf-8', mode="w") as outfile:
        json.dump(enriched_posts, outfile, indent=4)




def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])

    unique_tags_list = ', '.join(unique_tags)
    "Job Search, Mental Health, Scams"

def extract_metadata(post):
    TEMPLATE = '''
    You are given a LinkedIn post. You need to extract number of line, language of the post and tags.
    1. Return a valid JSON. NO preamble
    2. JSON obkext should have exactly three keys: line_count, language and tags.
    3. tags is an array of text tags. Extract maximum two tags.
    4. Language should be English or Hinglish(hindi + english).

    Here is the actual post on which you need to perform this task:
    {post}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'post': post})
    try:
        json_parser = JsonOutputParser()
        json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Invalid JSON format returned by the LLM.")
    return res

    return {
        'line_count': 10,
        'language': 'en',
        'tags': ['Mental Healt', 'Motivation'],
    }

if __name__ == "__main__":
    process_post("data/raw_posts.json", "data/processed_posts.json")