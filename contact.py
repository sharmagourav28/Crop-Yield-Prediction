import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def renderPage():
    st.header("")
    st.markdown(
        """<h3 class="stT">Mail Get In Touch with Me!</h3>
                """,
        unsafe_allow_html=True,
    )
    contact_form = """
    <form action="https://formsubmit.co/sharmagouravdsa@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <label for="name">Name</label>
        <input type="text" name="name" placeholder="Your Name" required>
        <label for="email">Email</label>
        <input type="email" name="email" placeholder="Your Email" required>
        <label for="message">Message</label>
        <textarea name="message" placeholder="Your Message"></textarea>
        <button type="submit">Send</button>
    </form>
    <br>
    <h4>Thanks For Visting 😊 !!</h4>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    local_css("cstyle.css")
