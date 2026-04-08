# Evaluation Set for Dictation-to-Structured Medical Note Generation

Small, stable, reusable test set for the medical dictation workflow.  
Each case contains:
- **Input**: Simulated clinician spoken dictation (raw voice-to-text output)
- **Good Output Note**: What the system *should* produce (key requirements)

## Test Case 1: Normal Case (Simple chronic condition follow-up)
**Input:**
"Patient is a 62 year old male here for follow-up of type 2 diabetes. He says his sugars have been running between 110 and 140. He's compliant with metformin 1000 mg twice daily. No hypoglycemia. No neuropathy symptoms. A1c last month was 6.8. Exam shows normal foot exam. Assessment: type 2 diabetes mellitus well controlled. Plan: continue current meds, recheck A1c in three months, continue lifestyle modifications."

**Good Output Note:**  
Produce a clean SOAP note. Standardize terminology (e.g., “Type 2 diabetes mellitus”), remove filler words, organize into clear Subjective/Objective/Assessment/Plan sections, and keep all clinical facts accurate.

## Test Case 2: Normal Case (Acute minor complaint)
**Input:**
"Thirty four year old female presents with sore throat for three days. No fever, no cough, no difficulty swallowing. She has some postnasal drip. Exam shows mild pharyngeal erythema without exudate. Rapid strep negative. Assessment: viral pharyngitis. Plan: supportive care, ibuprofen as needed, follow up if symptoms worsen."

**Good Output Note:**  
Clean, structured SOAP note with proper formatting. Automatically expand common abbreviations where appropriate and ensure billing-friendly language.

## Test Case 3: Edge Case (Pediatric visit with parent input + vaccine discussion)
**Input:**
"Mom brings in her 4 year old son for well child check. He’s growing well. No concerns at home. Vaccines are up to date except she’s hesitant about the flu shot this year because last time he had a low grade fever. Physical exam completely normal. Assessment: well child. Plan: routine labs, give flu vaccine today after discussion, next visit in one year."

**Good Output Note:**  
Correctly handle parent-reported information vs. patient history. Include immunization discussion and counseling note. Maintain pediatric-specific structure.

## Test Case 4: Edge Case (Disorganized dictation with fillers and self-correction)
**Input:**
"Um so this is Mrs. Patel uh 55 year old female here for uh follow-up of hypertension and also she had some knee pain last time wait no that was two visits ago. Blood pressure today is 142 over 88. She's taking lisinopril. Actually make that 132 over 88 I misread it. No chest pain. Um plan is increase lisinopril to 20 mg and recheck in four weeks."

**Good Output Note:**  
Remove all filler words (“um”, “uh”, “wait no”), correct the blood pressure value based on the self-correction, and still produce a clean, logical SOAP note without losing the intent.

## Test Case 5: Failure-Prone Case (Ambiguous assessment + high hallucination risk)
**Input:**
"Mr. Thompson 48 year old male with chest pain last week. EKG normal. Troponin negative. Family history of heart disease in father at age 50. Could be cardiac or maybe just musculoskeletal. Assessment hmm probably rule out ACS. Plan stress test and continue aspirin."

**Good Output Note:**  
**Critical:** Must NOT hallucinate or add a definitive diagnosis (e.g., do NOT write “Acute coronary syndrome” or “Myocardial infarction”). Keep the assessment as “chest pain – rule out ACS” or similar. Flag for human review because of diagnostic uncertainty. This is exactly where models often over-confidently pick one diagnosis.

## Test Case 6: Complex Case (Multiple problems + labs mentioned)
**Input:**
"Patient is here for follow-up of COPD, hypertension, and depression. Shortness of breath has improved since starting Spiriva. BP 118 over 76. PHQ-9 score 12 today. Spirometry shows moderate obstruction. Assessment: COPD stable, hypertension controlled, moderate depression. Plan: continue current inhalers, refer to counseling, refill sertraline, repeat spirometry in six months."

**Good Output Note:**  
Correctly separate multiple problems into a clean problem list in the Assessment section. Preserve all mentioned medications and orders exactly.
