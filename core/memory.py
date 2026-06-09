import os
import json
from datetime import datetime

# Try importing heavy dependencies
try:
    import chromadb
    from sentence_transformers import SentenceTransformer
    MEMORY_ENABLED = True
except ImportError:
    MEMORY_ENABLED = False
    print("Memory dependencies not available — memory disabled")

_embedding_model = None
_chroma_client = None


def get_embedding_model():
    global _embedding_model
    if _embedding_model is None and MEMORY_ENABLED:
        try:
            _embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        except Exception as e:
            print(f"Embedding model error: {e}")
    return _embedding_model


def get_chroma_client():
    global _chroma_client
    if _chroma_client is None and MEMORY_ENABLED:
        try:
            db_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'data', 'memory_db'
            )
            os.makedirs(db_path, exist_ok=True)
            _chroma_client = chromadb.PersistentClient(path=db_path)
        except Exception as e:
            print(f"ChromaDB error: {e}")
    return _chroma_client


def get_vendor_collection(vendor_name):
    client = get_chroma_client()
    if not client:
        return None
    try:
        safe_name = vendor_name.replace(" ", "_").lower().strip()
        return client.get_or_create_collection(
            name=f"vendor_{safe_name}",
            metadata={"vendor": vendor_name}
        )
    except Exception as e:
        print(f"Collection error: {e}")
        return None


def save_analysis_to_memory(vendor_name, business, city, insights):
    if not MEMORY_ENABLED:
        return False
    try:
        collection = get_vendor_collection(vendor_name)
        model = get_embedding_model()
        if not collection or not model:
            return False

        date_str = datetime.now().strftime("%d %B %Y")
        text = f"""
Analysis Date: {date_str}
Business: {business} in {city}
Total Revenue: Rs {insights.get('total_revenue',0):,.0f}
Total Profit: Rs {insights.get('total_profit',0):,.0f}
Profit Margin: {insights.get('profit_margin',0)}%
Best Product: {insights.get('best_product','N/A')}
Best Product Profit: Rs {insights.get('best_product_profit',0):,.0f}
Worst Product: {insights.get('worst_product','N/A')}
Best Day: {insights.get('best_day','N/A')}
Worst Day: {insights.get('worst_day','N/A')}
Loss Orders: {insights.get('loss_orders',0)}
Total Orders: {insights.get('total_orders',0)}
"""
        embedding = model.encode(text).tolist()
        doc_id = f"{vendor_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[doc_id],
            metadatas=[{
                "vendor": vendor_name,
                "business": business,
                "city": city,
                "date": date_str,
                "profit": str(insights.get('total_profit', 0)),
                "margin": str(insights.get('profit_margin', 0))
            }]
        )
        return True
    except Exception as e:
        print(f"Save memory error: {e}")
        return False


def save_question_to_memory(vendor_name, question, answer):
    if not MEMORY_ENABLED:
        return False
    try:
        collection = get_vendor_collection(vendor_name)
        model = get_embedding_model()
        if not collection or not model:
            return False

        date_str = datetime.now().strftime("%d %B %Y %H:%M")
        text = f"Date: {date_str}\nQuestion: {question}\nAnswer: {answer}"
        embedding = model.encode(text).tolist()
        doc_id = f"qa_{vendor_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[doc_id],
            metadatas=[{"vendor": vendor_name, "type": "qa", "date": date_str}]
        )
        return True
    except Exception as e:
        print(f"Save QA error: {e}")
        return False


def get_relevant_memories(vendor_name, query, n=3):
    if not MEMORY_ENABLED:
        return []
    try:
        collection = get_vendor_collection(vendor_name)
        model = get_embedding_model()
        if not collection or not model:
            return []

        count = collection.count()
        if count == 0:
            return []

        query_embedding = model.encode(query).tolist()
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=min(n, count)
        )

        memories = []
        if results and results['documents']:
            for doc in results['documents'][0]:
                memories.append(doc.strip())
        return memories
    except Exception as e:
        print(f"Retrieve memory error: {e}")
        return []


def get_vendor_memory_summary(vendor_name):
    if not MEMORY_ENABLED:
        return None
    try:
        collection = get_vendor_collection(vendor_name)
        if not collection:
            return None

        count = collection.count()
        if count == 0:
            return None

        results = collection.get()
        if not results or not results['documents']:
            return None

        metadatas = results.get('metadatas', [])
        analysis_entries = [m for m in metadatas if m.get('type') != 'qa']

        return {
            "total_memories": count,
            "analysis_count": len(analysis_entries),
            "entries": analysis_entries
        }
    except Exception as e:
        print(f"Memory summary error: {e}")
        return None


def clear_vendor_memory(vendor_name):
    if not MEMORY_ENABLED:
        return False
    try:
        client = get_chroma_client()
        if not client:
            return False
        safe_name = vendor_name.replace(" ", "_").lower().strip()
        client.delete_collection(f"vendor_{safe_name}")
        return True
    except Exception as e:
        print(f"Clear memory error: {e}")
        return False