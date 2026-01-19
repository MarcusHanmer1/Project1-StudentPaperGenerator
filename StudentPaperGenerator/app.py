# Cplt and web help used

import streamlit as st
import re
import logic

st.set_page_config(page_title="Exam Question Generator", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap');
.title-font {
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    font-size: 3.5rem;
    padding-bottom: 0rem;
}
.subheader-font {
    font-family: 'Lato', sans-serif;
    font-weight: 400;
    font-size: 1.25rem;
    color: #888888;
    padding-top: 0rem;
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title-font">Welcome</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader-font">The AI Maths Exam Question Generator</p>', unsafe_allow_html=True)

with st.sidebar:
    st.header("Your Inputs")
    pdf_file = st.file_uploader("Upload your Course PDF (Optional)", type="pdf")
    example_file = st.file_uploader("Upload Example Questions (Optional)", type=["pdf", "txt"])
    
    st.header("Options")
    include_answer_key = st.checkbox("Include Answer Key", value=True)

output_container = st.container()

def display_final_output(final_content):
    """Display the final output with proper formatting and error handling."""
    
    if final_content.startswith("An error occurred:"):
        output_container.error(final_content)
        return
    
    if "🚫 Request Denied" in final_content or "Request Denied" in final_content:
        output_container.error(final_content)
        st.info("💡 **Tip**: This tool is specifically designed for mathematics questions. Try asking for:\n"
                "- Algebra problems\n"
                "- Calculus questions\n"
                "- Geometry exercises\n"
                "- Statistics problems\n"
                "- Logic puzzles")
        return
    
    parts = re.split(r'\s*---ANSWER KEY---\s*', final_content, maxsplit=1, flags=re.IGNORECASE)
    questions = parts[0]
    
    with output_container:
        st.success("✅ Generation Complete")
        st.markdown(questions)
        
        if len(parts) > 1 and parts[1].strip():
            answers = parts[1]
            with st.expander("📝 Click to see Answer Key"):
                st.markdown(answers)
        elif include_answer_key:
            st.warning("⚠️ The AI was asked for an answer key but didn't provide one. Try re-phrasing your prompt.")

if user_prompt := st.chat_input("e.g., 'Generate 5 multiple-choice questions on Solving Equations.'"):
    
    output_container.empty()
    
    if pdf_file:
        
        if 'vector_store' not in st.session_state or \
           'processed_pdf_name' not in st.session_state or \
           st.session_state.processed_pdf_name != pdf_file.name:
            
            st.toast(f"📄 Processing '{pdf_file.name}'...")
            st.session_state.vector_store = logic.get_vector_store_from_pdf(pdf_file)
            st.session_state.processed_pdf_name = pdf_file.name
        
        vector_store = st.session_state.vector_store
        
        if vector_store is None:
            output_container.error("❌ Failed to process the PDF file. Please check the file and try again.")
            st.stop()

        if 'example_text' not in st.session_state or \
           'processed_example_name' not in st.session_state or \
           (example_file and st.session_state.processed_example_name != example_file.name) or \
           (not example_file and st.session_state.processed_example_name is not None):
            
            if example_file:
                st.toast(f"📋 Processing '{example_file.name}'...")
            st.session_state.example_text = logic.get_text_from_file(example_file)
            st.session_state.processed_example_name = example_file.name if example_file else None

        example_text = st.session_state.example_text
        if not example_text:
            example_text = "No examples provided."
        
        final_output_stream = logic.run_pdf_mode_pipeline(
            user_prompt, vector_store, example_text, include_answer_key
        )
            
        with output_container:
            with st.spinner("🤔 Generating your math questions..."):
                placeholder = st.empty()
                full_content = ""
                
                for chunk in final_output_stream:
                    if chunk.content:
                        full_content += chunk.content
                        placeholder.markdown(full_content + " ▌")
        
        placeholder.empty()
        
        display_final_output(full_content)

    else:
        
        if 'example_text' not in st.session_state or \
           'processed_example_name' not in st.session_state or \
           (example_file and st.session_state.processed_example_name != example_file.name) or \
           (not example_file and st.session_state.processed_example_name is not None):
            
            if example_file:
                st.toast(f"📋 Processing '{example_file.name}'...")
            st.session_state.example_text = logic.get_text_from_file(example_file)
            st.session_state.processed_example_name = example_file.name if example_file else None

        example_text = st.session_state.example_text
        if not example_text:
            example_text = "No examples provided."

        final_output_stream = logic.run_general_mode_pipeline(
            user_prompt, example_text, include_answer_key
        )
            
        with output_container:
            with st.spinner("🤔 Generating your math questions..."):
                placeholder = st.empty()
                full_content = ""
                
                for chunk in final_output_stream:
                    if chunk.content:
                        full_content += chunk.content
                        placeholder.markdown(full_content + " ▌")
        
        placeholder.empty()
        
        display_final_output(full_content)