#!/usr/bin/env python3
"""
Enhanced Start Script - Choose between Terminal or Streamlit Interface
"""

import subprocess
import time
import threading
import sys
import os

def start_api_servers():
    """Start both API servers in background"""
    print("🌐 Starting API servers...")
    
    # Start Factorization API
    print("🚀 Starting Factorization API (Port 8003)...")
    factorization_process = subprocess.Popen(
        [sys.executable, "apis/factorization_api.py"],
        cwd=os.getcwd(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Start Math API  
    print("🚀 Starting Math API (Port 8002)...")
    math_process = subprocess.Popen(
        [sys.executable, "apis/math_api.py"],
        cwd=os.getcwd(),
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    )
    
    print("⏳ Waiting for APIs to initialize...")
    time.sleep(5)
    print("✅ APIs started!")
    
    return factorization_process, math_process

def start_terminal_mode():
    """Start RAG system in terminal mode"""
    print("\n" + "="*50)
    print("🤖 Starting RAG System - Terminal Mode")
    print("="*50)
    
    try:
        from rag_pdf import RAGSystem, interactive_mode
        
        # Initialize RAG system
        rag = RAGSystem()
        
        # Start interactive mode
        interactive_mode(rag)
        
    except Exception as e:
        print(f"❌ Error starting RAG system: {e}")

def start_streamlit_mode():
    """Start RAG system with Streamlit web interface"""
    print("\n" + "="*50)
    print("🌐 Starting RAG System - Streamlit Web Interface")
    print("="*50)
    
    try:
        # Start Streamlit app
        print("🚀 Launching Streamlit app...")
        print("🌐 Web interface will open at: http://localhost:8501")
        
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.headless", "false"
        ])
        
    except Exception as e:
        print(f"❌ Error starting Streamlit: {e}")
        print("💡 Try: pip install streamlit")

def main():
    """Main startup function with interface choice"""
    print("🎯 RAG Chatbot System Launcher")
    print("="*50)
    
    # Start API servers first
    try:
        factorization_process, math_process = start_api_servers()
    except Exception as e:
        print(f"❌ Error starting APIs: {e}")
        return
    
    # Choose interface
    print("\n🎛️  Choose Interface:")
    print("1. 💻 Terminal Mode (Command Line)")
    print("2. 🌐 Streamlit Web Interface") 
    print("3. ❌ Exit")
    
    while True:
        choice = input("\n👉 Enter choice (1/2/3): ").strip()
        
        if choice == "1":
            start_terminal_mode()
            break
        elif choice == "2":
            start_streamlit_mode()
            break
        elif choice == "3":
            print("👋 Goodbye!")
            # Clean up processes
            try:
                factorization_process.terminate()
                math_process.terminate()
            except:
                pass
            break
        else:
            print("⚠️  Invalid choice. Please enter 1, 2, or 3")

if __name__ == "__main__":
    main()