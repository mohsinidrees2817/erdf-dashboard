"""
Debug script to process and test RAG documents
"""
import sys
import os
sys.path.append(os.getcwd())

# Load environment variables from .streamlit/secrets.toml
import toml
secrets_path = '.streamlit/secrets.toml'
if os.path.exists(secrets_path):
    with open(secrets_path, 'r') as f:
        secrets = toml.load(f)
        for key, value in secrets.items():
            os.environ[key.upper()] = str(value)

# Mock streamlit secrets
class MockSecrets:
    def __getitem__(self, key):
        return os.environ.get(key)

# Create a minimal streamlit module
class MockStreamlit:
    secrets = MockSecrets()

sys.modules['streamlit'] = MockStreamlit()

# Now import and test RAG
from rag import DocumentRAG
from pathlib import Path

print('=== RAG Debug Script ===')
print('Initializing RAG system...')
rag = DocumentRAG()

print('\n1. Checking available documents...')
docs_folder = Path('classification_documents')
if docs_folder.exists():
    docx_files = list(docs_folder.glob('*.docx'))
    print(f'Found {len(docx_files)} .docx files:')
    for file in docx_files:
        print(f'  - {file.name}')
else:
    print('classification_documents folder not found!')

print('\n2. Processing all documents...')
results = rag.process_all_documents('classification_documents')
print(f'Processing results:')
for i, result in enumerate(results):
    print(f'  Document {i+1}: {result}')

print('\n3. Checking namespaces after processing...')
namespaces = rag.get_namespaces()
print(f'Available namespaces: {namespaces}')

print('\n4. Testing search in examples_work_packages namespace...')
search_results = rag.search_documents(
    query='work package example project management activities',
    namespace='examples_work_packages',
    top_k=5
)
print(f'Search results: {len(search_results)} found')
for i, result in enumerate(search_results):
    print(f'Result {i+1}:')
    print(f'  Score: {result["score"]}')
    print(f'  Text: {result["text"][:200]}...')
    print()

print('\n5. Testing broader search...')
search_results = rag.search_documents(
    query='project activities deliverables timeline budget',
    top_k=10
)
print(f'Broader search results: {len(search_results)} found')
for i, result in enumerate(search_results):
    print(f'Result {i+1}: {result["namespace"]} - Score: {result["score"]}')
    print(f'  Text: {result["text"][:150]}...')
    print()
