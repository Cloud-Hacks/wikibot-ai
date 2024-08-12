import streamlit as st

# Display the sidebar with additional information and settings
def side_info():
    with st.sidebar:
        # Display logo and an image
        st.image("src/assets/wikibot.png", width=250)

        # Display an informational card
        card_html = """
        <div style="background-color: #0E1117; border: 2px solid #DE834D; border-radius: 10px; padding: 0px 8px; width: 100%; box-sizing: border-box; color: white; text-align: center; font-family: 'Arial', sans-serif; font-size: 14px; color: #FAFAFA;">
            <p>🌟 Your WikiBot AI assistant! Whether you need quick facts, detailed explanations, or summaries of complex topics, Enjoy a seamless and informative experience in no time</p>
        </div>
        """

        st.components.v1.html(card_html, height=100, scrolling=False)

        # Check and input Gemini AI API Key
        if "GEMINI_API_KEY" not in st.secrets:
            st.text_input(
                "Gemini AI API Key",
                type="password",
                placeholder="Enter your Gemini AI API key",
                help="Provide your Gemini AI API key for embedding models",
                key="gemini_api_key"
            )

        # Additional settings in a popover
        with st.popover("More settings", use_container_width=True):
            st.slider(
                "Temperature", min_value=0.0, max_value=2.0, step=0.1, value=0.1, key="temperature"
            )
            st.slider(
                "Max Tokens", min_value=0, max_value=8000, value=2500, key="max_tokens"
            )

        # Divider and link button
        st.markdown("---")
        st.link_button("🔗 Source Code", "https://github.com/Cloud-Hacks/wikibot-ai", use_container_width=True)
