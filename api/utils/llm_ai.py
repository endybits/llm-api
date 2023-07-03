import os
#import logging as log

from api.core.config import get_config_values

config = get_config_values()
OPENAI_API_KEY = config["openai_api_key"]
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

from langchain import OpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader, PromptHelper, LLMPredictor, ServiceContext, StorageContext

def createVectorIndex():
    #log.info('Loading Vector Index...')
    print('Loading Vector Index...')
    max_input = 4096
    tokens = 256
    chunk_size = 600
    max_chunk_overlap = 20

    # load data
    path_data = '../llm-api/.data'
    if not os.path.exists(path_data):
        raise FileNotFoundError(f"Unable loda the data: {path_data} does not exist")
    documents = SimpleDirectoryReader(path_data).load_data()

    # Prompt helper
    prompt_helper = PromptHelper(max_input_size=max_input, max_chunk_overlap=max_chunk_overlap, chunk_size_limit=chunk_size)

    # Define llm predictor
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, max_tokens=tokens, model="text-davinci-003"))

    # Service context configuration
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    storage_context = StorageContext.from_defaults()

    # build index
    index = VectorStoreIndex.from_documents(
        documents=documents,
        service_context=service_context,
        storage_context=storage_context
        )
    index.storage_context.persist()

    return index


index = createVectorIndex()
query_engine = index.as_query_engine()
response = query_engine.query(input('Ask me a question: '))
print(response)