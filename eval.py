import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# ==================== CONFIGURABLE SYSTEM PROMPT ====================
SYSTEM_PROMPT = """You are an expert medical scribe. 
Convert the clinician's raw spoken dictation into a clean, professional, structured medical note.
Use standard **SOAP format** (Subjective, Objective, Assessment, Plan).
Rules:
- Remove all filler words (um, uh, like, you know, etc.)
- Use proper medical terminology and abbreviations where appropriate
- Be concise, clear, and clinically accurate
- Never add information that was not in the dictation
- Output ONLY the structured Markdown note. No explanations."""

# Test cases (using the 3 we have in app.py)
TEST_CASES = {
    1: "Patient is a 62 year old male here for follow-up of type 2 diabetes. He says his sugars have been running between 110 and 140. He's compliant with metformin 1000 mg twice daily. No hypoglycemia. No neuropathy symptoms. A1c last month was 6.8. Exam shows normal foot exam. Assessment: type 2 diabetes mellitus well controlled. Plan: continue current meds, recheck A1c in three months, continue lifestyle modifications.",
    4: "Um so this is Mrs. Patel uh 55 year old female here for uh follow-up of hypertension and also she had some knee pain last time wait no that was two visits ago. Blood pressure today is 142 over 88. She's taking lisinopril. Actually make that 132 over 88 I misread it. No chest pain. Um plan is increase lisinopril to 20 mg and recheck in four weeks.",
    5: "Mr. Thompson 48 year old male with chest pain last week. EKG normal. Troponin negative. Family history of heart disease in father at age 50. Could be cardiac or maybe just musculoskeletal. Assessment hmm probably rule out ACS. Plan stress test and continue aspirin."
}

def generate_medical_note(dictation: str):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=SYSTEM_PROMPT
    )
    response = model.generate_content(f"Convert this dictation into a structured medical note:\n\n{dictation}")
    return response.text.strip()

print("🚀 Running Full Evaluation...\n")

for case_id, dictation in TEST_CASES.items():
    print(f"📋 Processing Test Case {case_id}...")
    note = generate_medical_note(dictation)
    
    filename = f"eval_output_testcase_{case_id}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Evaluation Output - Test Case {case_id}\n\n")
        f.write(note)
    
    print(f"   ✅ Saved → {filename}\n")

print("🎉 Full evaluation complete! Check the new eval_output_testcase_*.md files.")
