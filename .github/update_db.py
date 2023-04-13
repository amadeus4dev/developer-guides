import os
import logging
import tiktoken
import hashlib
from tqdm.auto import tqdm
import requests
from requests.adapters import HTTPAdapter, Retry
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

docs_dir = './docs'
endpoint_url = os.environ['ENDPOINT_URL']
logging.basicConfig(level=logging.INFO)

all_docs = []

# Loop through all files in the directory and subdirectories and load markdown files
for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            loader = UnstructuredMarkdownLoader(file_path)
            docs = loader.load()
            logging.info(f'Loaded {len(docs)} document(s) from {file_path}')

            # Append the loaded documents to the all_docs list
            all_docs.extend(docs)

logging.info(f'Total documents loaded: {len(all_docs)}')

# Chunking
tokenizer = tiktoken.get_encoding('cl100k_base')


def tiktoken_len(text):
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=20,  # number of tokens overlap between chunks
    length_function=tiktoken_len,
    separators=['\n\n', '\n', ' ', '']
)
chunks = text_splitter.split_text(all_docs[5].page_content)

m = hashlib.md5()  # this will convert URL into unique ID

documents = []

# Delete the existing documents, so we can update them later
del_session = requests.Session()
del_session.delete(
    f'{endpoint_url}/delete',
    json={
        'delete_all': 'true'
    }
)

for doc in tqdm(all_docs):
    url = doc.metadata['source'].replace(
        './docs/', 'https://amadeus4dev.github.io/developer-guides/').replace('.md', '')
    m.update(url.encode('utf-8'))
    uid = m.hexdigest()[:12]
    chunks = text_splitter.split_text(doc.page_content)
    for i, chunk in enumerate(chunks):
        documents.append({
            'id': f'{uid}-{i}',
            'text': chunk,
            'metadata': {'url': url}
        })

batch_size = 100
s = requests.Session()

# we setup a retry strategy to retry on 5xx errors
retries = Retry(
    total=5,
    backoff_factor=0.1,
    status_forcelist=[500, 502, 503, 504]
)
s.mount('http://', HTTPAdapter(max_retries=retries))

for i in tqdm(range(0, len(documents), batch_size)):
    i_end = min(len(documents), i+batch_size)
    res = s.post(
        f'{endpoint_url}/upsert',
        json={

            'documents': documents[i:i_end]
        }
    )
    logging.info(res.status_code)
