from llama_cloud_services import LlamaParse



parser = LlamaParse(
    api_key="llx-fJ72db0OfAP40j8AnxnvioxqXqNPsHySjMhAAX7mKx244OZw",  # Your API Key
    result_type="markdown",
    base_url='https://api.cloud.eu.llamaindex.ai'
)

result = parser.parse("documentsPDF/Le-travail-et-la-technique-cours.pdf")

# get the llama-index markdown documents
markdown_documents = result.get_markdown_documents(split_by_page=True)

# get the llama-index text documents
text_documents = result.get_text_documents(split_by_page=False)

# get the image documents
image_documents = result.get_image_documents(
    include_screenshot_images=True,
    include_object_images=False,
    # Optional: download the images to a directory
    # (default is to return the image bytes in ImageDocument objects)
    image_download_dir="./images",
)

# access the raw job result
# Items will vary based on the parser configuration
for page in result.pages:
    print(page.text)
    print(page.md)
    print(page.images)
    print(page.layout)
    print(page.structuredData)