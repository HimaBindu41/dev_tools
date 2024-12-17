# import streamlit as st
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_ollama.llms import OllamaLLM
# from chat_history import ChatHistory
# from snow_db import create_table_if_not_exists
# import time
# from datetime import datetime, timedelta

# create_table_if_not_exists()

# chat_history = ChatHistory()

# # Available models
# available_models = {
#     "Llama 3": "llama3",
#     "Llama 3.2": "llama3.2",
# }

# def get_prompt_template():
#     return """Question: {question}

# Answer: Let's think step by step."""

# def load_model(model_name):
#     if 'loaded_model' not in st.session_state or st.session_state.loaded_model_name != model_name:
#         try:
#             st.session_state.loaded_model = OllamaLLM(model=model_name)
#             st.session_state.loaded_model_name = model_name
#         except Exception as e:
#             st.error(f"Error: Model '{model_name}' not found.")
#             return None
#     return st.session_state.loaded_model

# def format_date_label(entry_date):
#     today = datetime.now().date()
#     yesterday = today - timedelta(days=1)
#     if entry_date.date() == today:
#         return "Today"
#     elif entry_date.date() == yesterday:
#         return "Yesterday"
#     else:
#         return entry_date.strftime("%Y-%m-%d")

# def get_response_with_retries(chain, question, chat_context, retries=3, delay=2):
#     for attempt in range(retries):
#         try:
#             full_input = {"question": f"{chat_context}\nQuestion: {question}"}
#             response = chain.invoke(full_input)
#             if response:
#                 return response
#             else:
#                 st.error("Received an empty response.")
#                 return None
#         except Exception as e:
#             if attempt < retries - 1:
#                 time.sleep(delay)
#             else:
#                 st.error(f"Error getting response: {str(e)}")
#     return None

# def main():
#     if 'on_email_page' not in st.session_state:
#         st.session_state.on_email_page = False
#     if 'selected_session_id' not in st.session_state:
#         st.session_state.selected_session_id = None
#     if 'chat_histories' not in st.session_state:
#         st.session_state.chat_histories = {}
#     if 'selected_model' not in st.session_state:
#         st.session_state.selected_model = list(available_models.keys())[0]

#     st.sidebar.title("Navigation")
#     # When the "Automated Professional Communication" button is clicked in the sidebar
#     if st.sidebar.button("Automated Professional Communication", key="communication_page"):
#         st.session_state.on_email_page = True
#         st.session_state.is_email_draft_generated = False
#         st.session_state.current_email_draft_id = None 
#         st.rerun()  # Ensures page refresh to apply the on_email_page state

#     if st.session_state.on_email_page:
#         show_email_drafting_page()
#     else:
#         st.title("Chatbot")

#         with st.sidebar:
#             new_model = st.selectbox("Choose a model:", list(available_models.keys()), key="model_select")
#             if new_model != st.session_state.selected_model:
#                 st.session_state.selected_model = new_model

#             if st.button("Start New Chat"):
#                 session_name = "New Chat"
#                 session_id = chat_history.create_chat_session(session_name)
#                 if session_id:
#                     st.session_state.selected_session_id = session_id
#                     st.session_state.chat_histories[session_id] = []
#             st.header("Chat Sessions")
#             sessions = chat_history.load_sessions()

#             # Iterate over sessions and display session button with delete and edit options beside it
#             for session_id, session_name, created_at in sessions:
#                 created_date = format_date_label(datetime.fromisoformat(created_at))
                
#                 # Create columns for the session button and action buttons (Delete/Edit)
#                 col1, col2, col3 = st.columns([4, 1, 1])  # Adjust the column width as needed
                
#                 with col1:
#                     # Session name button
#                     if st.button(f"{session_name} - {created_date}", key=f"session_{session_id}"):
#                         st.session_state.selected_session_id = session_id
#                         chat_history.current_session_id = session_id
                        
#                         # Load chat history if not already loaded
#                         if session_id not in st.session_state.chat_histories:
#                             st.session_state.chat_histories[session_id] = chat_history.load_history(session_id) or []
                        
#                         # Rerun to reflect the selected session
#                         st.rerun()

#                 with col2:
#                     # Delete button beside the session
#                     if st.button(f"🗑️", key=f"delete_{session_id}"):
#                         # Call your method to delete the session from Snowflake
#                         chat_history.delete_session(session_id)
                        
#                         # Remove from session history in the state
#                         if session_id in st.session_state.chat_histories:
#                             del st.session_state.chat_histories[session_id]
                        
#                         # Rerun to update the session list
#                         st.rerun()

#                 with col3:
#                     # Edit button beside the session
#                     if st.button(f"🖊️", key=f"edit_{session_id}"):
#                         # Input field to update session name
#                         new_session_name = st.text_input(f"Edit session name for {session_name}", value=session_name)
                        
#                         # Button to save the new session name
#                         if st.button(f"Save Changes", key=f"save_{session_id}"):
#                             # Update session name in Snowflake
#                             chat_history.update_session_name(session_id, new_session_name)
                            
#                             # Update session name in session state
#                             if session_id in st.session_state.chat_histories:
#                                 st.session_state.chat_histories[session_id] = [history for history in st.session_state.chat_histories[session_id]]
                            
#                             # Rerun to reflect changes
#                             st.rerun()
#         model_name = available_models[st.session_state.selected_model]
#         model = load_model(model_name)
#         if model is None:
#             st.stop()

#         prompt_template = get_prompt_template()
#         prompt = ChatPromptTemplate.from_template(prompt_template)
#         chain = prompt | model

#         current_session_id = st.session_state.selected_session_id
#         if current_session_id not in st.session_state.chat_histories:
#             st.session_state.chat_histories[current_session_id] = []

#         current_chat_history = st.session_state.chat_histories.get(current_session_id, [])
#         user_avatar_url = "https://www.w3schools.com/w3images/avatar5.png"
#         assistant_avatar_url = "https://as1.ftcdn.net/v2/jpg/05/88/95/30/1000_F_588953042_01Hrsog5OuZobKdMXf9GVpB6e6XiIhBa.webp"

#         if current_chat_history:
#             for entry in current_chat_history:
#                 with st.chat_message("user", avatar=user_avatar_url):
#                     st.write(entry['question'])
#                 with st.chat_message("assistant", avatar=assistant_avatar_url):
#                     st.write(entry['answer'])
#                     st.write(f"*Response generated using model: {entry['model_name']}*")  


                    

#         input_placeholder = st.empty()
#         user_input = input_placeholder.chat_input("Type your question here...", key="user_input")

#         chat_context = "\n".join([f"Q: {entry['question']}\nA: {entry['answer']}" for entry in current_chat_history])

#         if user_input and current_session_id is not None:
#             with st.spinner("Getting response..."):
#                 retries =3
#                 response = get_response_with_retries(chain, user_input.strip(), chat_context, retries=retries)
#                 if response:
#                     entry = {
#                         'question': user_input.strip(),
#                         'answer': response,
#                         'timestamp': datetime.now().isoformat(),
#                         'model_name': model_name 
#                     }
#                     chat_history.add_entry(current_session_id, user_input.strip(), response,model_name)
#                     st.session_state.chat_histories[current_session_id].append(entry)
#                     with st.chat_message("user", avatar=user_avatar_url):
#                         st.write(user_input.strip())
#                     with st.chat_message("assistant", avatar=assistant_avatar_url):
#                         st.write(response)
#                         st.write(f"*Response generated using model: {entry['model_name']}*")


#                     st.rerun()

# def show_email_drafting_page():
#     if 'email_drafts' not in st.session_state:
#         st.session_state.email_drafts = {}
#     st.title("Email Generator")

#     # Sidebar button for navigating back to the initial input fields
#     with st.sidebar:
#         if st.button("Back to Chat", key="back_to_chat"):
#             st.session_state.on_email_page = False
#             st.rerun()

#         new_model = st.selectbox("Choose a model:", list(available_models.keys()), key="model_select")
#         if new_model != st.session_state.selected_model:
#             st.session_state.selected_model = new_model
#         st.sidebar.header("Saved Drafts")
            
#         # Display saved drafts in sidebar with 'View Draft' and 'Delete' buttons
#         for draft_id, draft_entry in list(st.session_state.email_drafts.items()):
#             if 'subject' in draft_entry:
#                 with st.sidebar.expander(f"{draft_entry['subject']}"):
#                     col1, col2 = st.columns([3, 1])
#                     with col1:
#                         if st.button("View Draft", key=f"view_{draft_id}"):
#                             st.session_state.current_email_draft_id = draft_id  # Store the current draft ID
#                             st.session_state.is_email_draft_generated = False  # Ensure that the generated draft gets refreshed
#                             st.rerun()  # Refresh to show the selected draft in the main section
#                     with col2:
#                         if st.button("Delete", key=f"delete_{draft_id}"):
#                             del st.session_state.email_drafts[draft_id]
#                             chat_history.delete_email_draft(draft_id)
#                             st.success(f"Draft '{draft_entry['subject']}' deleted.")
#                             st.rerun()

#     # Initialize email drafts storage in session state if it doesn't exist
#     if 'email_drafts' not in st.session_state:
#         st.session_state.email_drafts = {}

#     # Check if a specific draft was selected for viewing
#     if 'current_email_draft_id' in st.session_state and st.session_state.current_email_draft_id:
#         draft_id = st.session_state.current_email_draft_id
#         draft_entry = st.session_state.email_drafts.get(draft_id)
        
#         if draft_entry:
#             st.markdown("### Drafted Email:")
#             st.markdown(f"**Subject:** {draft_entry['subject']}")
#             st.markdown(f"**Recipient:** {draft_entry['recipient']}")
#             st.markdown(f"**Content:** {draft_entry['content']}")
#             st.markdown(f"**Draft:** {draft_entry['draft']}")
            
#             st.markdown("### Not satisfied? Add more instructions to refine the email:")
#             additional_instructions = st.chat_input("Additional Instructions", key="additional_instructions")

#             if additional_instructions:
#                 model_name = available_models[st.session_state.selected_model]
#                 model = load_model(model_name)
#                 prompt_template = get_prompt_template()
#                 prompt = ChatPromptTemplate.from_template(prompt_template)
#                 chain = prompt | model

#                 refined_email_prompt = f"Refine this email based on the following instructions:\n\nOriginal Email:\n{draft_entry['draft']}\n\nInstructions: {additional_instructions}"
                
#                 with st.spinner("Refining email..."):
#                     refined_response = get_response_with_retries(chain, refined_email_prompt, "")
#                     if refined_response:
#                         st.markdown("### Refined Email:")
#                         st.markdown(refined_response)
#                         st.session_state.current_email_draft = refined_response  # Replace with refined draft
#                         st.session_state.email_drafts[draft_id] = {
#                             'subject': draft_entry['subject'],
#                             'recipient': draft_entry['recipient'],
#                             'content': draft_entry['content'],
#                             'draft': refined_response
#                         }
#                         st.rerun()  # Refresh to show the refined draft
#         return  # Exit the function early to prevent further processing
#     else:
#         # Display the form to create a new draft
#         if not st.session_state.get('is_email_draft_generated', False):
#             subject = st.text_input("Email Subject", key="email_subject")
#             recipient = st.text_input("Recipient Email", key="email_recipient")
#             content = st.text_area("Email Content", placeholder="Provide details for the email...", key="email_content")

#             if st.button("Generate Email", key="generate_email"):
#                 email_prompt = f"Write a professional email with the following details:\n\nSubject: {subject}\nRecipient: {recipient}\nContent: {content}"
#                 model_name = available_models[st.session_state.selected_model]
#                 model = load_model(model_name)

#                 if model:
#                     prompt_template = get_prompt_template()
#                     prompt = ChatPromptTemplate.from_template(prompt_template)
#                     chain = prompt | model

#                     with st.spinner("Generating email..."):
#                         response = get_response_with_retries(chain, email_prompt, "")
#                         if response:
#                             st.session_state.is_email_draft_generated = True
#                             st.session_state.current_email_draft = response
#                             draft_id = f"{st.session_state.selected_session_id}_{len(st.session_state.email_drafts) + 1}"
#                             st.session_state.email_drafts[draft_id] = {
#                                 'subject': subject,
#                                 'recipient': recipient,
#                                 'content': content,
#                                 'draft': response
#                             }
#                             st.session_state.current_email_draft_id = draft_id
#                             chat_history.save_email_draft(st.session_state.selected_session_id, subject, recipient, content, response)
#                             st.rerun()
                            




# if __name__ == "__main__":
#     main()

# main_chatbot.py
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from chat_history import ChatHistory
from utils import load_model, get_prompt_template, get_response_with_retries, format_date_label
import time
from datetime import datetime, timedelta

# Create table if not exists
from snow_db import create_table_if_not_exists
create_table_if_not_exists()

chat_history = ChatHistory()

# Available models
available_models = {
    "Llama 3": "llama3",
    "Llama 3.2": "llama3.2",
}

def main():
    if 'on_email_page' not in st.session_state:
        st.session_state.on_email_page = False
    if 'selected_session_id' not in st.session_state:
        st.session_state.selected_session_id = None
    if 'chat_histories' not in st.session_state:
        st.session_state.chat_histories = {}
    if 'selected_model' not in st.session_state:
        st.session_state.selected_model = list(available_models.keys())[0]

    st.sidebar.title("Navigation")

    if st.sidebar.button("Automated Professional Communication", key="communication_page"):
        st.session_state.on_email_page = True
        st.session_state.is_email_draft_generated = False
        st.session_state.current_email_draft_id = None
        st.rerun()

    if st.session_state.on_email_page:
        from email_drafting import show_email_drafting_page
        show_email_drafting_page()
    else:
        st.title("Chatbot")

        with st.sidebar:
            new_model = st.selectbox("Choose a model:", list(available_models.keys()), key="model_select")
            if new_model != st.session_state.selected_model:
                st.session_state.selected_model = new_model

            if st.button("Start New Chat"):
                session_name = "New Chat"
                session_id = chat_history.create_chat_session(session_name)
                if session_id:
                    st.session_state.selected_session_id = session_id
                    st.session_state.chat_histories[session_id] = []
            st.header("Chat Sessions")
            sessions = chat_history.load_sessions()

            # Iterate over sessions and display session button with delete and edit options beside it
            for session_id, session_name, created_at in sessions:
                created_date = format_date_label(datetime.fromisoformat(created_at))
                col1, col2, col3 = st.columns([4, 1, 1])

                with col1:
                    if st.button(f"{session_name} - {created_date}", key=f"session_{session_id}"):
                        st.session_state.selected_session_id = session_id
                        chat_history.current_session_id = session_id
                        if session_id not in st.session_state.chat_histories:
                            st.session_state.chat_histories[session_id] = chat_history.load_history(session_id) or []
                        st.rerun()

                with col2:
                    if st.button(f"🗑️", key=f"delete_{session_id}"):
                        chat_history.delete_session(session_id)
                        if session_id in st.session_state.chat_histories:
                            del st.session_state.chat_histories[session_id]
                        st.rerun()

                with col3:
                    if st.button(f"🖊️", key=f"edit_{session_id}"):
                        new_session_name = st.text_input(f"Edit session name for {session_name}", value=session_name)
                        if st.button(f"Save Changes", key=f"save_{session_id}"):
                            chat_history.update_session_name(session_id, new_session_name)
                            if session_id in st.session_state.chat_histories:
                                st.session_state.chat_histories[session_id] = [history for history in st.session_state.chat_histories[session_id]]
                            st.rerun()

        model_name = available_models[st.session_state.selected_model]
        model = load_model(model_name)
        if model is None:
            st.stop()

        prompt_template = get_prompt_template()
        prompt = ChatPromptTemplate.from_template(prompt_template)
        chain = prompt | model

        current_session_id = st.session_state.selected_session_id
        if current_session_id not in st.session_state.chat_histories:
            st.session_state.chat_histories[current_session_id] = []

        current_chat_history = st.session_state.chat_histories.get(current_session_id, [])
        user_avatar_url = "https://www.w3schools.com/w3images/avatar5.png"
        assistant_avatar_url = "https://as1.ftcdn.net/v2/jpg/05/88/95/30/1000_F_588953042_01Hrsog5OuZobKdMXf9GVpB6e6XiIhBa.webp"

        if current_chat_history:
            for entry in current_chat_history:
                with st.chat_message("user", avatar=user_avatar_url):
                    st.write(entry['question'])
                with st.chat_message("assistant", avatar=assistant_avatar_url):
                    st.write(entry['answer'])
                    st.write(f"*Response generated using model: {entry['model_name']}*")  

        input_placeholder = st.empty()
        user_input = input_placeholder.chat_input("Type your question here...", key="user_input")

        chat_context = "\n".join([f"Q: {entry['question']}\nA: {entry['answer']}" for entry in current_chat_history])

        if user_input and current_session_id is not None:
            with st.spinner("Getting response..."):
                retries = 3
                response = get_response_with_retries(chain, user_input.strip(), chat_context, retries=retries)
                if response:
                    entry = {
                        'question': user_input.strip(),
                        'answer': response,
                        'timestamp': datetime.now().isoformat(),
                        'model_name': model_name 
                    }
                    chat_history.add_entry(current_session_id, user_input.strip(), response, model_name)
                    st.session_state.chat_histories[current_session_id].append(entry)
                    with st.chat_message("user", avatar=user_avatar_url):
                        st.write(user_input.strip())
                    with st.chat_message("assistant", avatar=assistant_avatar_url):
                        st.write(response)
                        st.write(f"*Response generated using model: {entry['model_name']}*")

                    st.rerun()

if __name__ == "__main__":
    main()
