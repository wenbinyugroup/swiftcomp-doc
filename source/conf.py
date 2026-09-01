# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SwiftComp'
copyright = '2025, Wenbin Yu'
author = 'Wenbin Yu'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'myst_parser',
    "sphinx.ext.githubpages",
    'sphinxcontrib.bibtex',
    'sphinx_markdown_builder',
]

templates_path = ['_templates']
exclude_patterns = []

root_doc = 'index'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

numfig = True
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section'}

bibtex_bibfiles = ['refs.bib']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_book_theme'
html_theme = 'pydata_sphinx_theme'

html_title = 'SwiftComp Manual'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_theme_options = {
    # 'site_url': 'https://wenbinyugroup.github.io/sgio/',
    # 'repo_url': 'https://github.com/wenbinyugroup/sgio',
    # 'palette': {
    #     'primary': 'red'
    # },
    # # 'logo': {
    # #     'text': 'sgio',
    # # },
    # 'show_nav_level': 2,
    # # "path_to_docs": "doc/source",
    # # 'use_edit_page_button': True,
    # # "use_repository_button": True,
    # # "use_issues_button": True,
    # # 'collapse_navigation': True,
    # 'navigation_depth': 4,
    "announcement": "Documentation is under construction.",
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "dollarmath",
    "fieldlist",
]
