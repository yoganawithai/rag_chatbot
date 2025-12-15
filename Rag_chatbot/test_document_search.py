#!/usr/bin/env python3
"""
Test document search improvements
"""

import sys
import os
sys.path.append('.')
from rag_pdf import RAGSystem

def test_document_search():
    """Test document search with better similarity and prompting"""
    print("🧪 Testing Document Search Improvements")
    print("=" * 50)
    
    try:
        # Initialize RAG system
        rag = RAGSystem()
        
        # Test document questions
        document_questions = [
            "what is health",
            "diabetes information", 
            "symptoms of disease",
            "medical advice",
            "treatment options"
        ]
        
        for question in document_questions:
            print(f"\n🔍 Testing: '{question}'")
            print("-" * 40)
            
            try:
                result = rag.ask_question(question, use_cache=False)
                answer = result.get('answer', 'No answer')
                sources = result.get('sources', [])
                found_in = result.get('found_in', 'unknown')
                
                print(f"📍 Found in: {found_in}")
                print(f"📄 Sources: {sources}")
                print(f"🤖 Answer: {answer[:200]}...")
                
                if found_in == 'documents':
                    print("✅ SUCCESS: Found in documents")
                else:
                    print("❌ ISSUE: Should have found in documents")
                    
            except Exception as e:
                print(f"❌ ERROR: {e}")
        
        print(f"\n{'=' * 50}")
        print("🎯 Document search test completed!")
        
    except Exception as e:
        print(f"❌ SETUP ERROR: {e}")

if __name__ == "__main__":
    test_document_search()