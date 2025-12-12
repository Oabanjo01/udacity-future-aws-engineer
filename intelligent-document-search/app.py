import streamlit as st
import boto3
from botocore.exceptions import ClientError
import json
from bedrock_utils import query_knowledge_base, generate_response, valid_prompt


# Streamlit UI
st.title("Bedrock Chat Application")

# Sidebar for configurations
st.sidebar.header("Configuration")
model_id = st.sidebar.selectbox("Select LLM Model", ["anthropic.claude-3-haiku-20240307-v1:0", "anthropic.claude-3-5-sonnet-20240620-v1:0"])
kb_id = st.sidebar.text_input("Knowledge Base ID", "CE8HQYERBM")
temperature = st.sidebar.select_slider("Temperature", [i/10 for i in range(0,11)],1)
top_p = st.sidebar.select_slider("Top_P", [i/1000 for i in range(0,1001)], 1)
enable_validation = st.sidebar.checkbox("Enable Prompt Validation", value=False, help="Requires bedrock:InvokeModel permission")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Validate prompt
    if enable_validation:
        with st.spinner("Validating prompt..."):
            is_valid = valid_prompt(prompt, model_id, enable_validation=True)
    else:
        is_valid = valid_prompt(prompt, model_id, enable_validation=False)
    
    if is_valid:
        # Query Knowledge Base
        with st.spinner("Searching knowledge base..."):
            kb_results = query_knowledge_base(prompt, kb_id)
        
        if kb_results:
            # Prepare context from Knowledge Base results
            context = "\n".join([result['content']['text'] for result in kb_results])
            
            # Generate response using LLM
            full_prompt = f"Context: {context}\n\nUser: {prompt}\n\nAssistant:"
            with st.spinner("Generating response..."):
                response = generate_response(full_prompt, model_id, temperature, top_p)
            
            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(response)
                
                # Display sources
                with st.expander("📚 View Sources"):
                    for idx, result in enumerate(kb_results, 1):
                        source_location = result.get('location', {})
                        s3_location = source_location.get('s3Location', {})
                        uri = s3_location.get('uri', 'Unknown source')
                        score = result.get('score', 0)
                        
                        st.markdown(f"**Source {idx}** (Relevance: {score:.2f})")
                        st.markdown(f"📄 `{uri}`")
                        st.markdown(f"_{result['content']['text'][:200]}..._")
                        st.divider()
        else:
            response = "I couldn't find relevant information in the knowledge base. Please try rephrasing your question."
            with st.chat_message("assistant"):
                st.markdown(response)
    else:
        response = "⚠️ I'm unable to answer this question. Please ensure your question is related to heavy machinery and try again."
        with st.chat_message("assistant"):
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})