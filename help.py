import streamlit as st
from pathlib import Path
from PIL import Image


def renderApp():
    st.markdown(
        """<h3 class="stT">Project Related Document's</h3>
                """,
        unsafe_allow_html=True,
    )
    current_dir = Path(__file__).parent if "_file__" in locals() else Path.cwd()
    synopsis = current_dir / "documents" / "Synopsis.pdf"
    firstppt = current_dir / "documents" / "firstppt.pptx"
    surveypaper = current_dir / "documents" / "survey.pdf"
    researchppr = current_dir / "documents" / "researchpaper.pdf"
    report = current_dir / "documents" / "report.pdf"
    design = current_dir / "documents" / "design.pdf"
    vedio = current_dir / "documents" / "vedio.webm"
    css_file = current_dir / "style.css"
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    with open(synopsis, "rb") as sys:
        majorsynopsis = sys.read()

    with open(firstppt, "rb") as ppt1:
        majorppt = ppt1.read()

    with open(surveypaper, "rb") as survey:
        majorsurveypaper = survey.read()

    with open(researchppr, "rb") as rppr:
        majoresearchpaper = rppr.read()

    with open(report, "rb") as rp:
        majorreport = rp.read()

    with open(design, "rb") as ds:
        majordesign = ds.read()

    with open(vedio, "rb") as vd:
        majorvedio = vd.read()
    col1, col2 = st.columns(2, gap="small")

    with col1:
        st.write("🔴 PROJECT SYNOPSIS ")
        st.download_button(
            label="📄 Download Synopsis",
            data=majorsynopsis,
            file_name=synopsis.name,
            mime="application/octet-stream",
        )
    with col2:
        st.write("🔴 PROJECT STARTING PPT")
        st.download_button(
            label="📄 Download Project PPT",
            data=majorppt,
            file_name=firstppt.name,
            mime="application/octet-stream",
        )

    col3, col4 = st.columns(2, gap="small")

    with col3:
        st.write("🔴 PROJECT SURVEY PAPER")
        st.download_button(
            label="📄 Download Survey Paper",
            data=majorsurveypaper,
            file_name=surveypaper.name,
            mime="application/octet-stream",
        )

    with col4:
        st.write("🔴 PROJECT RESEARCH PAPER")
        st.download_button(
            label="📄 Download Research Paper",
            data=majoresearchpaper,
            file_name=researchppr.name,
            mime="application/octet-stream",
        )
    col5, col6 = st.columns(2, gap="small")
    with col5:
        st.write("🔴 PROJECT REPORT")
        st.download_button(
            label="📄 Download REPORT",
            data=majorreport,
            file_name=report.name,
            mime="application/octet-stream",
        )
    with col6:
        st.write("🔴 PROJECT DESIGN DIAGRAM")
        st.download_button(
            label="📄 Download Design Diagram",
            data=majordesign,
            file_name=design.name,
            mime="application/octet-stream",
        )

    col7, col8 = st.columns(2, gap="small")
    with col7:
        st.write("🔴 PROJECT Vedio")
        st.download_button(
            label="📄 Download Vedio",
            data=majorvedio,
            file_name=vedio.name,
            mime="application/octet-stream",
        )
