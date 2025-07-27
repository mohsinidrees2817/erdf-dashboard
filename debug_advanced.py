"""
Advanced RAG debugging to understand the search issue
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

print('=== Advanced RAG Debug ===')
rag = DocumentRAG()

# Test 1: Check individual namespace searches
print('\n1. Testing searches in each namespace individually...')
namespaces = rag.get_namespaces()
test_queries = [
    'project activities deliverables timeline budget',
    'arbetspaket aktiviteter leverabler tidplan budget',
    'work package activities deliverables'
]

for query in test_queries:
    print(f'\n--- Testing query: "{query}" ---')
    for namespace in namespaces:
        try:
            results = rag.search_documents(
                query=query,
                namespace=namespace,
                top_k=3
            )
            print(f'{namespace}: {len(results)} results')
            if results:
                print(f'  Best match score: {results[0]["score"]:.4f}')
                print(f'  Text preview: {results[0]["text"][:100]}...')
        except Exception as e:
            print(f'{namespace}: ERROR - {e}')

# Test 2: Check what happens with no namespace (cross-namespace search)
print('\n\n2. Testing cross-namespace search with different queries...')
test_queries_broad = [
    'project',
    'activities', 
    'deliverables',
    'budget',
    'arbetspaket',
    'projektledning',
    'aktiviteter'
]

for query in test_queries_broad:
    try:
        results = rag.search_documents(
            query=query,
            namespace=None,  # Explicitly set to None for cross-namespace
            top_k=5
        )
        print(f'Query "{query}": {len(results)} results')
        if results:
            print(f'  Best score: {results[0]["score"]:.4f} from {results[0]["namespace"]}')
    except Exception as e:
        print(f'Query "{query}": ERROR - {e}')

# Test 3: Let's check the Pinecone index directly
print('\n\n3. Checking Pinecone index stats...')
try:
    stats = rag.index.describe_index_stats()
    print(f'Total vectors: {stats.total_vector_count}')
    print(f'Index dimension: {stats.dimension}')
    if stats.namespaces:
        print('Namespace details:')
        for ns_name, ns_stats in stats.namespaces.items():
            print(f'  {ns_name}: {ns_stats.vector_count} vectors')
    else:
        print('No namespace stats available')
except Exception as e:
    print(f'Error getting index stats: {e}')

# Test 4: Try a raw Pinecone query without our wrapper
print('\n\n4. Testing raw Pinecone query...')
try:
    # Get a simple embedding for testing
    test_embedding = rag.get_embedding('project activities')
    
    # Try raw query without namespace
    raw_results = rag.index.query(
        vector=test_embedding,
        top_k=5,
        include_metadata=True
    )
    print(f'Raw query results: {len(raw_results.matches)} matches')
    for i, match in enumerate(raw_results.matches):
        print(f'  Match {i+1}: Score {match.score:.4f}, ID: {match.id}')
        if hasattr(match, 'metadata') and match.metadata:
            print(f'    Namespace: {match.metadata.get("namespace", "unknown")}')
            print(f'    Text: {match.metadata.get("chunk_text", "no text")[:100]}...')

except Exception as e:
    print(f'Error with raw query: {e}')
