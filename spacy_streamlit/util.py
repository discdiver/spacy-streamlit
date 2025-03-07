import streamlit as st
import spacy
import base64


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_model(name: str) -> spacy.language.Language:
    """Load a spaCy model."""
    return spacy.load(name)


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def process_text(model_name: str, text: str) -> spacy.tokens.Doc:
    """Process a text and create a Doc object."""
    nlp = load_model(model_name)
    return nlp(text)


def get_svg(svg: str, style: str = "", wrap: bool = True):
    """Convert an SVG to a base64-encoded image."""
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}" style="{style}"/>'
    return get_html(html) if wrap else html


def get_html(html: str):
    """Convert HTML so it can be rendered."""
    WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""
    # Newlines seem to mess with the rendering
    html = html.replace("\n", " ")
    return WRAPPER.format(html)


LOGO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 900 500 175" width="150" height="53"><path fill="#09A3D5" d="M64.8 970.6c-11.3-1.3-12.2-16.5-26.7-15.2-7 0-13.6 2.9-13.6 9.4 0 9.7 15 10.6 24.1 13.1 15.4 4.7 30.4 7.9 30.4 24.7 0 21.3-16.7 28.7-38.7 28.7-18.4 0-37.1-6.5-37.1-23.5 0-4.7 4.5-8.4 8.9-8.4 5.5 0 7.5 2.3 9.4 6.2 4.3 7.5 9.1 11.6 21 11.6 7.5 0 15.3-2.9 15.3-9.4 0-9.3-9.5-11.3-19.3-13.6-17.4-4.9-32.3-7.4-34-26.7-1.8-32.9 66.7-34.1 70.6-5.3-.3 5.2-5.2 8.4-10.3 8.4zm81.5-28.8c24.1 0 37.7 20.1 37.7 44.9 0 24.9-13.2 44.9-37.7 44.9-13.6 0-22.1-5.8-28.2-14.7v32.9c0 9.9-3.2 14.7-10.4 14.7-8.8 0-10.4-5.6-10.4-14.7v-95.6c0-7.8 3.3-12.6 10.4-12.6 6.7 0 10.4 5.3 10.4 12.6v2.7c6.8-8.5 14.6-15.1 28.2-15.1zm-5.7 72.8c14.1 0 20.4-13 20.4-28.2 0-14.8-6.4-28.2-20.4-28.2-14.7 0-21.5 12.1-21.5 28.2.1 15.7 6.9 28.2 21.5 28.2zm59.8-49.3c0-17.3 19.9-23.5 39.2-23.5 27.1 0 38.2 7.9 38.2 34v25.2c0 6 3.7 17.9 3.7 21.5 0 5.5-5 8.9-10.4 8.9-6 0-10.4-7-13.6-12.1-8.8 7-18.1 12.1-32.4 12.1-15.8 0-28.2-9.3-28.2-24.7 0-13.6 9.7-21.4 21.5-24.1 0 .1 37.7-8.9 37.7-9 0-11.6-4.1-16.7-16.3-16.7-10.7 0-16.2 2.9-20.4 9.4-3.4 4.9-2.9 7.8-9.4 7.8-5.1 0-9.6-3.6-9.6-8.8zm32.2 51.9c16.5 0 23.5-8.7 23.5-26.1v-3.7c-4.4 1.5-22.4 6-27.3 6.7-5.2 1-10.4 4.9-10.4 11 .2 6.7 7.1 12.1 14.2 12.1zM354 909c23.3 0 48.6 13.9 48.6 36.1 0 5.7-4.3 10.4-9.9 10.4-7.6 0-8.7-4.1-12.1-9.9-5.6-10.3-12.2-17.2-26.7-17.2-22.3-.2-32.3 19-32.3 42.8 0 24 8.3 41.3 31.4 41.3 15.3 0 23.8-8.9 28.2-20.4 1.8-5.3 4.9-10.4 11.6-10.4 5.2 0 10.4 5.3 10.4 11 0 23.5-24 39.7-48.6 39.7-27 0-42.3-11.4-50.6-30.4-4.1-9.1-6.7-18.4-6.7-31.4-.4-36.4 20.8-61.6 56.7-61.6zm133.3 32.8c6 0 9.4 3.9 9.4 9.9 0 2.4-1.9 7.3-2.7 9.9l-28.7 75.4c-6.4 16.4-11.2 27.7-32.9 27.7-10.3 0-19.3-.9-19.3-9.9 0-5.2 3.9-7.8 9.4-7.8 1 0 2.7.5 3.7.5 1.6 0 2.7.5 3.7.5 10.9 0 12.4-11.2 16.3-18.9l-27.7-68.5c-1.6-3.7-2.7-6.2-2.7-8.4 0-6 4.7-10.4 11-10.4 7 0 9.8 5.5 11.6 11.6l18.3 54.3 18.3-50.2c2.7-7.8 3-15.7 12.3-15.7z" /> </svg>"""
LOGO = get_svg(LOGO_SVG, wrap=False, style="max-width: 100%; margin-bottom: 25px")


def get_color_styles(color: str) -> str:
    """Compile some hacky CSS to override the theme color."""
    # fmt: off
    color_selectors = ["a", "a:hover", "*:not(textarea).st-ex:hover", ".st-en:hover"]
    bg_selectors = [".st-da", "*:not(button).st-en:hover"]
    border_selectors = [".st-ft", ".st-fs", ".st-fr", ".st-fq", ".st-ex:hover", ".st-en:hover"]
    # fmt: on
    css_root = "#root { --primary: %s }" % color
    css_color = ", ".join(color_selectors) + "{ color: %s !important }" % color
    css_bg = ", ".join(bg_selectors) + "{ background-color: %s !important }" % color
    css_border = ", ".join(border_selectors) + "{ border-color: %s !important }" % color
    other = ".decoration { background: %s !important }" % color
    return f"<style>{css_root}{css_color}{css_bg}{css_border}{other}</style>"
