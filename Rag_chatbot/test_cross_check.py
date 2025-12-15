#!/usr/bin/env python3
"""
Test API vs Document Cross-checking
"""

def test_cases():
    """Show test cases to verify API vs Document routing"""
    print("🧪 API vs Document Cross-checking Test Cases")
    print("=" * 55)
    
    print("\n🔢 SHOULD GO TO APIs (Math/Calculation Questions):")
    print("-" * 45)
    api_questions = [
        "fibonacci 5",
        "fib 10", 
        "factors of 9",
        "what is factor of 46",
        "find factors of 64",
        "factorize 25",
        "5+7",
        "10*3",
        "calculate fibonacci 8"
    ]
    
    for q in api_questions:
        print(f"   ❓ '{q}' → Should use Factorization/Math API")
    
    print("\n📄 SHOULD GO TO DOCUMENTS (Health/General Questions):")
    print("-" * 50)
    doc_questions = [
        "what is illness",
        "what is health", 
        "diabetes symptoms",
        "disease information",
        "medical advice",
        "treatment options"
    ]
    
    for q in doc_questions:
        print(f"   ❓ '{q}' → Should use Documents")
    
    print("\n🔍 CROSS-CHECK IMPROVEMENTS MADE:")
    print("-" * 35)
    improvements = [
        "✅ Better math keyword detection (fibonacci, factor, calculate, etc.)",
        "✅ Improved math pattern matching for numbers and operations", 
        "✅ Cross-validation: Math questions → Verify document answers contain math",
        "✅ Fallback: If document answer doesn't match math question → Check APIs",
        "✅ Enhanced logging to show which step finds the answer",
        "✅ API answer preview to verify correct API response"
    ]
    
    for improvement in improvements:
        print(f"   {improvement}")
    
    print(f"\n{'=' * 55}")
    print("🎯 Test with your running system:")
    print("   Try: 'fibonacci 5' → Should show Math API result")
    print("   Try: 'what is illness' → Should show Document result") 
    print("   Try: 'factors of 9' → Should show Factorization API result")

if __name__ == "__main__":
    test_cases()