import streamlit as st
from pathlib import Path
from PIL import Image


def renderApp():
    st.markdown(
        """<h3 class="stT">Team Member's</h3>
                """,
        unsafe_allow_html=True,
    )
    current_dir = Path(__file__).parent if "_file__" in locals() else Path.cwd()
    css_file = current_dir / "style.css"

    # Kanak Sharma
    resume_kanak = current_dir / "Assest" / "kcv.pdf"
    photo_kanak = current_dir / "Assest" / "kpic.png"

    # Gourav Sharma
    resume_gourav = current_dir / "Assest" / "gcv.pdf"
    photo_gourav = current_dir / "Assest" / "img.png"

    # Harsh Dad
    resume_harshd = current_dir / "Assest" / "hcv.pdf"
    photo_harshd = current_dir / "Assest" / "hcv.png"

    # Harsh Jaiswal
    resume_harshj = current_dir / "Assest" / "jascv.pdf"
    photo_harshj = current_dir / "Assest" / "jasimg.png"

    KNAME = "Kanak Sharma"
    KDES = "Team Lead (UI Designer)"
    KEMAIL = "kanaksharma20724@acropolis.in"

    GNAME = "Gourav Sharma"
    GDES = "FrontEnd Developer(Python-Streamlit)"
    GEMAIL = "gouravsharma20702@acropolis.in"

    HNAME = "Harsh Dad"
    HDES = "FrontEnd Developer(Python)"
    HEMAIL = "harshdad20186@acropolis.in"

    JNAME = "Harsh Jaiswal"
    JDES = "Researcher & Documentation"
    JEMAIL = "harshjaiswal20527@acropolis.in"

    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(resume_kanak, "rb") as pdf_kanak:
        PDFkanak = pdf_kanak.read()
    with open(resume_gourav, "rb") as pdf_gourav:
        pdf_gourav = pdf_gourav.read()
    with open(resume_harshd, "rb") as pdf_harsh:
        PDFharsh = pdf_harsh.read()
    with open(resume_harshj, "rb") as pdf_jasiwal:
        PDFjasiwal = pdf_jasiwal.read()

    kanak_pic = Image.open(photo_kanak)
    gourav_pic = Image.open(photo_gourav)
    harshdad_pic = Image.open(photo_harshd)
    harshjaiswal_pic = Image.open(photo_harshj)

    col7, col8 = st.columns(2, gap="small")
    with col7:
        st.image(kanak_pic, width=230)
    with col8:
        st.title(KNAME)
        st.write(KDES)
        st.download_button(
            label="📄 Download Resume",
            data=PDFkanak,
            file_name=resume_kanak.name,
            mime="application/octet-stream",
        )
        st.write("📫", KEMAIL)

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(gourav_pic, width=230)
    with col2:
        st.title(GNAME)
        st.write(GDES)
        st.download_button(
            label="📄 Download Resume",
            data=pdf_gourav,
            file_name=resume_gourav.name,
            mime="application/octet-stream",
        )
        st.write("📫", GEMAIL)

    # Harsh Dad
    col3, col4 = st.columns(2, gap="small")
    with col3:
        st.image(harshdad_pic, width=230)
    with col4:
        st.title(HNAME)
        st.write(HDES)
        st.download_button(
            label="📄 Download Resume",
            data=PDFharsh,
            file_name=resume_harshd.name,
            mime="application/octet-stream",
        )
        st.write("📫", HEMAIL)

    # Harsh Jaiswal
    col5, col6 = st.columns(2, gap="small")
    with col5:
        st.image(harshjaiswal_pic, width=230)
    with col6:
        st.title(JNAME)
        st.write(JDES)
        st.download_button(
            label="📄 Download Resume",
            data=PDFjasiwal,
            file_name=resume_harshj.name,
            mime="application/octet-stream",
        )
        st.write("📫", JEMAIL)
