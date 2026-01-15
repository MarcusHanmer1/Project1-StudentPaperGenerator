# Yichun - Ethics Assessment

**Status:** Active  
**Owner:** Marcus Hanmer, PM  
**Last updated:** 15/01/2026  
**Applicable Regulations:** UK Online Safety Act

## 1. Core principles

**Mission Statement:**  
To provide accessible and math revision help while prioritizing student safety and academic integrity.  

**The Pillars:**  
- Safety first: We never output harmful or age inappropriate content.  
- Pedagogical integrity: We value correctly generated questions over fast but wrong.  
- Anti dependency: We build tools to help students learn, not to do the work for them.

## 2. Risk Assessment

**Risk: Hallucinations**  
Description: Model produces mathematically incorrect formulas and or information.  
Severity: Critical  
Likelihood: Rare   
Mitigation: Use low temperature (0.2), implement RAG, strictly prompt engineer not to answer when not confident.  

**Risk: Tone policing:**   
Description: The bot becoming aggressive or inappropriate.  
Severity: High  
Likelihood: Rare   
Mitigation: Choose a model which already has the mitigating behaviour built in.  

**Risk: Prompt injection**  
Description: Users tricking the bot into ignoring its rules.  
Severity: Critical  
Likelihood: Rare  
Mitigation: Choose a model which already has the mitigating behaviour built in.

## 3. Operational Guardrails

**Input Filter:**  
- Scan the input for particular keywords related to undesirable prompts (hate-speech, self-harm, sexual, prompt injections etc).  

**Systen Prompt Constraints:**  
- The model is strictly instructed via the system prompt to refuse requests unrelated to Maths question generation.  

**Output Filter:**  
- Check output for banned keywords before displaying to the student.

## 4. Data Governance and Privacy

- Retention policy: Chat logs are not recorded and the Agent is given a new conversation ID every time the page is loaded (So can only have a conversation in one singular session).  
- Training data: No user data is collected at all as shown in the privacy policy, and so no training data is collected either!

## 5. Incidence Response

**The flagging mechanism:** The flagging mechanism will be implemented.  

**The kill switch:** In the event of a critical safety failure (e.g., the bot starts swearing), we will review the issue and immediately review it, take down the issue for production, then evaluate and re-release after the fix.

## 6. Transparency and User Disclosure

**Identity:** The product storeface clearly labels Yichun as an 'AI helper' and not a real person.  

**Limitations:** We explicitly inform users that Yichun is just a messanger agent that can only interact via message.

## 7. Other considerations

- People who write exam questions jobs may be taken.
- If the model is too repetitive the questions may not be of use anymore.
- If the questions don't provide realistic practice for students then students risk practicing the generated questions which may not actually help for the actual exam.

**How to help these?**  
To help with jobs and integration, ensure the model is used to aid exam question makers work instead of replace it.
If questions are too repetitive, we must evaluate this and then find a way to make more creativity (raise temp etc).
If the questions aren't providing real value, we must evaluate this and we must look more into the product itself to see why the questions are different from the actual questions that students need to practice.