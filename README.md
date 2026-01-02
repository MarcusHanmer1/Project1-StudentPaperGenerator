# PRD and Ethics #
## Exam Question Generator ##

[Here is the link!](https://project1-studentpapergenerator-m5yyqmcvycecjkzr3fayju.streamlit.app/)

**Product name:** Exam Question Generator  
**Date:** 2/01/2026  
**Owner:** Marcus Hanmer  
**Type:** RAG Agent  

### 1. The Problem ###

**User problem**
Many students get a limited number of past paper questions to use for their revision for exams, and this can cause stress and a lack of confidence when going into an exam scenario.

**Why AI?**
This problem is solvable using AI and would be difficult for a human to solve as well, since universities and schools often times will not make new past paper materials for students to practice other than the ones they've already made. AI can help automate this especially with the assistance of RAG, since we can use it to 'train' the model on the specific notes and or example questions which the user wants to practice more of.

**Success metric**
To measure success on this task, we can measure many things, but here we will mainly focus on the correctness of the questions provided (they can be answered) and also the following of difficulty and style of the question types provided.

### 2. The UX ###

**Input**
The user can input a prompt to the agent asking for a particular type of question or question topic.
The user can input a PDF of their course notes, and also a PDF or TXT document of example questions which they may have at hand.
The user can input whether or not they would like a mark-scheme for the questions asked attached or not.

**Process**
The inputs are then passed into the agent, whereby the documents provided are fed into the RAG system and embedded etc.
The agents then begin, first of all the first draft (of questions) is created by an LLM, then that is sent to a marker agent which checks if the drafts are firstly doable, and secondly related heavily to the documents provided, then the marker agent passes this onto a refiner agent in order to take the instructions given by the marker agent on how to improve the first draft of questions, and then the refiner agent returns these questions to the user.

**Output**
The agent will output a number of Exam style questions on what the user has asked for, and the agent will provide answers if answers are asked for.

### 3. Possible Failures of Product ###

- Slowness of loading
- incorrectness of questions
- inefficient use of agents
- hallucinations

**Fixes**
The slowness of loading has been looked at in many ways, but just as other companies have done as well, we will stream the tokens as they are generated so that the user sees something happen earlier than if not, and also funny comments are printed when the question is immediately transferred through the system, so that the user has something to look at and see that it is loading.

The incorrectness of questions has been partially looked at by having this Generator-Marker-Refiner pattern in place.

The inefficient use of agents is being fixed by implementing checks to see whether or not the user has inputted something that is worthy of generating questions about (ensuring that the user hasn't accidentally clicked the button and then ran the process unnecessarily)

The hallucinations of the models is focused on by ensuring that the model can ONLY really generate questions which link directly to the documents provided (when they are provided).

### 4. System specs ###

As documented within the changes log, we see that each model is engineered with a particular persona, whereby the Generator model is a professional university exam question maker, the Marker model is a professional university exam question marker and the Refiner model is a professional university exam question refiner. Of course these will be adjusted and tweaked to see what works best, and those changes will be in the changes log.

The tone and constraints of the model follow closely to the personas given, whereby the 3 models are all very serious and strict, and since the marker model is never seen by the user it is very blunt and focused on providing harsh criticism to the questions that it is given.

### 5. Evaluation ###

We will test on 3 diverse PDFs: one History (text heavy), one Math (formula heavy), one Biology (image heavy). We will check the answers against actual exam question papers and possibly give questions out to students or even LLMs to measure how differnt the questions feel in both style and difficulty. 

The models questions pass if they get a 50% preffered by student rate, or a 90% rate of where students cannot tell the difference between the two.

### 6. Out of Scope ###

N/A at the moment

### 7. Ethics ###

- People who write exam questions jobs may be taken.
- If the model is too repetitive the questions may not be of use anymore.
- If the questions don't provide realistic practice for students then students risk practicing the generated questions which may not actually help for the actual exam.

**How to help these?**

To help with jobs and integration, ensure the model is used to aid exam question makers work instead of replace it.
If questions are too repetitive, we must evaluate this and then find a way to make more creativity (raise temp etc).
If the questions aren't providing real value, we must evaluate this and we must look more into the product itself to see why the questions are different from the actual questions that students need to practice.