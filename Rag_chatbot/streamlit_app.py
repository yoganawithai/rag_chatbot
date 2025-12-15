#!/usr/bin/env python3
"""
Streamlit Frontend for RAG Chatbot System
Clean web interface for document search and API calculations
"""

import streamlit as st
import requests
import json
import time
from typing import Dict, Any
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from rag_pdf import RAGSystem
except ImportError:
    st.error("Error importing RAG system. Make sure all dependencies are installed.")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="🤖 RAG Chatbot",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
        background-color: #f0f8ff;
    }
    .api-response {
        background-color: #e8f5e8;
        border-left: 5px solid #28a745;
    }
    .document-response {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
    }
    .not-found {
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
    }
    .sidebar-info {
        background-color: #e7f3ff;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def initialize_rag_system():
    """Initialize the RAG system (cached for performance)"""
    try:
        return RAGSystem()
    except Exception as e:
        st.error(f"Failed to initialize RAG system: {e}")
        return None

def format_response(result: Dict[Any, Any]) -> tuple:
    """Format the response based on source type"""
    answer = result.get('answer', 'No answer available')
    sources = result.get('sources', [])
    found_in = result.get('found_in', 'unknown')
    execution_time = result.get('execution_time', 0)
    
    # Format source display
    if found_in == 'api':
        source_type = "🔢 API"
        css_class = "api-response"
        source_text = f"**Source:** {', '.join(sources)}"
    elif found_in == 'documents':
        source_type = "📄 Documents"
        css_class = "document-response"
        source_text = f"**Sources:** {', '.join(sources)}"
    else:
        source_type = "❌ Not Found"
        css_class = "not-found"
        source_text = "**Sources:** None"
    
    return answer, source_text, source_type, css_class, execution_time

def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 RAG Chatbot</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🔧 System Info")
        
        # Initialize RAG system
        rag_system = initialize_rag_system()
        
        if rag_system:
            # Document info
            doc_count = len(rag_system.kb_manager.documents)
            st.markdown(f"""
            <div class="sidebar-info">
            <strong>📚 Documents Loaded:</strong> {doc_count}<br>
            <strong>🌐 APIs Available:</strong> Math + Factorization<br>
            <strong>🔍 Search Flow:</strong> Documents → APIs → Not Found<br>
            <strong>📄 Supported Files:</strong> PDF, TXT, CSV, Excel (XLSX/XLS)
            </div>
            """, unsafe_allow_html=True)
            

        else:
            st.error("❌ RAG System not initialized")
            st.stop()
    
    # Main chat interface
    st.markdown("### 💬 Ask Your Question")
    

    
    # Initialize clear state if not exists
    if 'clear_clicked' not in st.session_state:
        st.session_state.clear_clicked = False
    
    # Question input
    question = st.text_input(
        "Type your question here:",
        value="" if st.session_state.clear_clicked else st.session_state.get("question_value", ""),
        placeholder="e.g., What is diabetes? or fibonacci 5 or Ask about Excel/CSV data",
        key="question_input"
    )
    
    # Store current question value
    st.session_state.question_value = question
    
    # Create two columns for buttons
    col1, col2, col3 = st.columns([1, 1, 4])
    
    with col1:
        ask_button = st.button("🚀 Ask Question", type="primary")
    
    with col2:
        clear_button = st.button("🧹 Clear")
    
    if clear_button:
        st.session_state.clear_clicked = True
        st.session_state.question_value = ""
        st.rerun()
    else:
        st.session_state.clear_clicked = False
    
    # Process question
    if ask_button and question.strip():
        st.markdown("---")
        
        # Show question
        st.markdown(f"**❓ Your Question:** {question}")
        
        # Show loading spinner
        with st.spinner("🔍 Searching documents and APIs..."):
            try:
                # Get answer from RAG system
                start_time = time.time()
                result = rag_system.ask_question(question, use_cache=True)
                
                # Format response
                answer, source_text, source_type, css_class, execution_time = format_response(result)
                
                # Display response
                st.markdown(f"""
                <div class="chat-message {css_class}">
                    <h4>{source_type} Response</h4>
                    <p><strong>Answer:</strong> {answer}</p>
                    <p>{source_text}</p>
                    <p><strong>⏱️ Response Time:</strong> {execution_time:.2f}s</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Show additional info based on source
                if result.get('found_in') == 'api':
                    api_type = result.get('api_type', 'Unknown')
                    st.info(f"🎯 This question was answered by the {api_type.title()} API")
                elif result.get('found_in') == 'documents':
                    st.info("📚 This answer was found in your knowledge base documents")
                else:
                    st.warning("🚫 Not Found in Knowledge Base - Information not explicitly available")
                
                # Cache info
                if result.get('cached', False):
                    st.success("💾 This answer was retrieved from cache for faster response")
                    
            except Exception as e:
                st.error(f"❌ Error processing question: {e}")
                st.exception(e)
    
    elif ask_button:
        st.warning("⚠️ Please enter a question")
    


if __name__ == "__main__":
    main()