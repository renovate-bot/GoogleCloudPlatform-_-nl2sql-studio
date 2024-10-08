"""Page for DBAI chat agent"""
from dbai_src.dbai import DBAI
import streamlit as st


PROJ_ID = "sl-test-project-363109"
DATASET_ID = "nl2sql_spider"
TABLES_LIST = ""


def set_page_layout():
    """ """
    st.set_page_config(
        page_title="Database AI",
        layout="wide",
    )


def draw_sidebar():
    """ """
    markdown = """This is an Autonomous Assistant which understands
      all your questions and can intelligently find anything on your DB.
### Capabilities:
- Multi-turn conversation allows followup questions.
- Provide holistic insights and ideas about your Dataset.
- Understand and implement human feedback
- Debug generated code by observing error
- Plot charts smartly by indetifying the best suit chart-type.
    """

    st.sidebar.title("About")
    url = "go/nl2sql-studio-demo"
    st.sidebar.markdown(f"Demo Video: [{url}](//{url})")

    st.sidebar.info(markdown)
    # st.sidebar.image( "https://i.imgur.com/UbOXYAU.png")


def show_past_chat():
    """ """
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"].replace("$", r"\$"))  # noqa: W605
            try:
                if message["backend_details"]:
                    with st.expander("Intermediate Steps:"):
                        st.markdown(message["backend_details"])
            except KeyError:
                pass


if __name__ == '__main__':
    set_page_layout()
    draw_sidebar()

    col1, col2 = st.columns([7, 1])
    with col1:
        st.title("Autonomus NL2SQL Bot for your Database 💬")
    with col2:
        clear_button = st.button("New Chat",
                                 help="Deletes the conversation history, which\
                                      makes your new chat better and faster.",
                                 type="primary",
                                 use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        with st.expander("Click for Sample Questions", expanded=False):
            st.write("""
                - What all can you do? what tools/functions do you have \
                     access to?
                - guide me as best as you can, on how to use you and ask \
                     questions on you
                - Give a detailed insight about all the tables in this DB.
                - What agreements are going to expire in next 5 years?
                - what time period of data exists in the agreement table?
                - Give me interesting ideas of plots which can be drawn on \
                     this database
                - Show me a chart of most common months of effective_end_date
                - Show me a chart of the years and how many contracts expire \
                     that year
            """,)
    with col2:
        with st.expander("Click to Configure your DB searches"):
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                project_id = st.text_input(label='Project id',
                                           value=PROJ_ID)
            with col2:
                dataset_id = st.text_input(label='Dataset id',
                                           value=DATASET_ID)
            with col3:
                tables_list = st.text_input(label='List of tables to analyze',
                                            value=TABLES_LIST)
                tables_list = tables_list.split(',')

    dbai = DBAI(
            proj_id=project_id,
            dataset_id=dataset_id,
            tables_list=tables_list
        )

    if "chat" not in st.session_state:
        st.session_state.chat = dbai.agent.start_chat()
    if "messages" not in st.session_state:
        st.session_state.messages = []

    prompt = st.chat_input(
        "Ask me anything about the database... \
        Make sure to click New Chat for a new conversation.")

    if clear_button:
        st.session_state.chat = dbai.agent.start_chat()
        st.session_state.messages = []

    show_past_chat()
    print(len(st.session_state.chat.history))

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()

            with st.spinner('I am working. Please wait...'):
                response = dbai.ask(prompt, st.session_state.chat)
            # time.sleep(1)

            full_response = response.text
            interims = dbai.format_interim_steps(response.interim_steps)
            with message_placeholder.container():
                st.markdown(full_response.replace("$", r"\$"))  # noqa: W605
                if interims:
                    with st.expander("Intermediate Steps:"):
                        st.markdown(interims)

        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response,
            "backend_details": interims,
        })
