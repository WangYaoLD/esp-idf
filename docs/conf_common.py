# -*- coding: utf-8 -*-
#
# Common (non-language-specific) configuration for Read The Docs & Sphinx
#
# Based on a Read the Docs Template documentation build configuration file,
# created by sphinx-quickstart on Tue Aug 26 14:19:49 2014.
#
# This file is imported from a language-specific conf.py (ie en/conf.py or
# zh_CN/conf.py)
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from __future__ import print_function
from __future__ import unicode_literals
import sys
import os
import os.path
import re
import subprocess
from sanitize_version import sanitize_version
from idf_extensions.util import download_file_if_missing
from get_github_rev import get_github_rev


# build_docs on the CI server sometimes fails under Python3. This is a workaround:
sys.setrecursionlimit(3500)

config_dir = os.path.abspath(os.path.dirname(__file__))

# http://stackoverflow.com/questions/12772927/specifying-an-online-image-in-sphinx-restructuredtext-format
#
suppress_warnings = ['image.nonlocal_uri']

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['breathe',

              'sphinx.ext.todo',
              'sphinx_idf_theme',
              'sphinxcontrib.blockdiag',
              'sphinxcontrib.seqdiag',
              'sphinxcontrib.actdiag',
              'sphinxcontrib.nwdiag',
              'sphinxcontrib.rackdiag',
              'sphinxcontrib.packetdiag',

              'extensions.html_redirects',
              'extensions.toctree_filter',
              'extensions.list_filter',

              'idf_extensions.include_build_file',
              'idf_extensions.link_roles',
              'idf_extensions.build_system',
              'idf_extensions.esp_err_definitions',
              'idf_extensions.gen_toolchain_links',
              'idf_extensions.gen_version_specific_includes',
              'idf_extensions.kconfig_reference',
              'idf_extensions.run_doxygen',
              'idf_extensions.gen_idf_tools_links',
              'idf_extensions.format_idf_target',
              'idf_extensions.latex_builder',
              'idf_extensions.gen_defines',
              'idf_extensions.exclude_docs',

              # from https://github.com/pfalcon/sphinx_selective_exclude
              'sphinx_selective_exclude.eager_only',
              # TODO: determine if we need search_auto_exclude
              # 'sphinx_selective_exclude.search_auto_exclude',
              ]

# sphinx.ext.todo extension parameters
# If the below parameter is True, the extension
# produces output, else it produces nothing.
todo_include_todos = False

# Enabling this fixes cropping of blockdiag edge labels
seqdiag_antialias = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = ['.rst', '.md']

source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser',
                  }

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

# This is the full exact version, canonical git version description
# visible when you open index.html.
version = subprocess.check_output(['git', 'describe']).strip().decode('utf-8')

# The 'release' version is the same as version for non-CI builds, but for CI
# builds on a branch then it's replaced with the branch name
release = sanitize_version(version)

print('Version: {0}  Release: {1}'.format(version, release))

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['**/inc/**', '_static', '**/_build']


BT_DOCS = ['api-guides/blufi.rst',
           'api-guides/esp-ble-mesh/**',
           'api-reference/bluetooth/**']

SDMMC_DOCS = ['api-reference/peripherals/sdmmc_host.rst',
              'api-reference/peripherals/sd_pullup_requirements.rst']

SDIO_SLAVE_DOCS = ['api-reference/peripherals/sdio_slave.rst',
                   'api-reference/peripherals/esp_slave_protocol.rst',
                   'api-reference/protocols/esp_serial_slave_link.rst']

MCPWM_DOCS = ['api-reference/peripherals/mcpwm.rst']

LEGACY_DOCS = ['api-guides/build-system-legacy.rst',
               'gnu-make-legacy.rst',
               'api-guides/ulp-legacy.rst',
               'api-guides/unit-tests-legacy.rst',
               'get-started-legacy/**']

ESP32_DOCS = ['api-guides/ulp_instruction_set.rst',
              'api-guides/jtag-debugging/configure-wrover.rst',
              'api-reference/system/himem.rst',
              'api-guides/RF_calibration.rst',
              'api-reference/system/ipc.rst',
              'security/secure-boot-v1.rst',
              'security/secure-boot-v2.rst',
              'api-reference/peripherals/secure_element.rst',
              'hw-reference/esp32/**'] + LEGACY_DOCS

ESP32S2_DOCS = ['esp32s2.rst',
                'hw-reference/esp32s2/**',
                'api-guides/ulps2_instruction_set.rst',
                'api-guides/dfu.rst',
                'api-reference/peripherals/hmac.rst',
                'api-reference/peripherals/ds.rst',
                'api-reference/peripherals/temp_sensor.rst'
                '']

# format: {tag needed to include: documents to included}, tags are parsed from sdkconfig and peripheral_caps.h headers
conditional_include_dict = {'SOC_BT_SUPPORTED':BT_DOCS,
                            'SOC_SDMMC_HOST_SUPPORTED':SDMMC_DOCS,
                            'SOC_SDIO_SLAVE_SUPPORTED':SDIO_SLAVE_DOCS,
                            'SOC_MCPWM_SUPPORTED':MCPWM_DOCS,
                            'esp32':ESP32_DOCS,
                            'esp32s2':ESP32S2_DOCS}

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# Extra options required by sphinx_idf_theme
project_slug = 'esp-idf'
versions_url = 'https://dl.espressif.com/dl/esp-idf/idf_versions.js'

idf_targets = ['esp32', 'esp32s2']
languages = ['en', 'zh_CN']

project_homepage = "https://github.com/espressif/esp-idf"

# -- Options for HTML output ----------------------------------------------

# Custom added feature to allow redirecting old URLs
#
# Redirects should be listed in page_redirects.xt
#
with open("../page_redirects.txt") as f:
    lines = [re.sub(" +", " ", line.strip()) for line in f.readlines() if line.strip() != "" and not line.startswith("#")]
    for line in lines:  # check for well-formed entries
        if len(line.split(' ')) != 2:
            raise RuntimeError("Invalid line in page_redirects.txt: %s" % line)
html_redirect_pages = [tuple(line.split(' ')) for line in lines]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'sphinx_idf_theme'

# context used by sphinx_idf_theme
html_context = {
    "display_github": True,  # Add 'Edit on Github' link instead of 'View page source'
    "github_user": "espressif",
    "github_repo": "esp-idf",
    "github_version": get_github_rev(),
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "../_static/espressif-logo.svg"


# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'ReadtheDocsTemplatedoc'

# -- Options for LaTeX output ---------------------------------------------

latex_template_dir = os.path.join(config_dir, 'latex_templates')

preamble = ''
with open(os.path.join(latex_template_dir, 'preamble.tex')) as f:
    preamble = f.read()

titlepage = ''
with open(os.path.join(latex_template_dir, 'titlepage.tex')) as f:
    titlepage = f.read()


latex_elements = {
    'papersize': 'a4paper',

    # Latex figure (float) alignment
    'figure_align':'htbp',

    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'fncychap': '\\usepackage[Sonny]{fncychap}',

    'preamble': preamble,

    'maketitle': titlepage,
}

# The name of an image file (relative to this directory) to place at the bottom of
# the title page.
latex_logo = "../_static/espressif2.pdf"
latex_engine = 'xelatex'
latex_use_xindy = False

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'readthedocstemplate', u'Read the Docs Template Documentation',
     [u'Read the Docs'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'ReadtheDocsTemplate', u'Read the Docs Template Documentation',
     u'Read the Docs', 'ReadtheDocsTemplate', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# Override RTD CSS theme to introduce the theme corrections
# https://github.com/rtfd/sphinx_rtd_theme/pull/432
def setup(app):
    app.add_stylesheet('theme_overrides.css')

    # these two must be pushed in by build_docs.py
    if "idf_target" not in app.config:
        app.add_config_value('idf_target', None, 'env')
        app.add_config_value('idf_targets', None, 'env')

    app.add_config_value('conditional_include_dict', None, 'env')
    app.add_config_value('docs_to_build', None, 'env')

    # Breathe extension variables (depend on build_dir)
    # note: we generate into xml_in and then copy_if_modified to xml dir
    app.config.breathe_projects = {"esp32-idf": os.path.join(app.config.build_dir, "xml_in/")}
    app.config.breathe_default_project = "esp32-idf"

    setup_diag_font(app)

    # Config values pushed by -D using the cmdline is not available when setup is called
    app.connect('config-inited',  setup_config_values)
    app.connect('config-inited',  setup_html_context)


def setup_config_values(app, config):
    # Sets up global config values needed by other extensions
    idf_target_title_dict = {
        'esp32': 'ESP32',
        'esp32s2': 'ESP32-S2'
    }

    app.add_config_value('idf_target_title_dict', idf_target_title_dict, 'env')

    pdf_name = "esp-idf-{}-{}-{}".format(app.config.language, app.config.version, app.config.idf_target)
    app.add_config_value('pdf_file', pdf_name, 'env')


def setup_html_context(app, config):
    # Setup path for 'edit on github'-link
    config.html_context['conf_py_path'] = "/docs/{}/".format(app.config.language)


def setup_diag_font(app):
    # blockdiag and other tools require a font which supports their character set
    # the font file is stored on the download server to save repo size

    font_name = {
        'en': 'DejaVuSans.ttf',
        'zh_CN': 'NotoSansSC-Regular.otf',
    }[app.config.language]

    font_dir = os.path.join(config_dir, '_static')
    assert os.path.exists(font_dir)

    print("Downloading font file %s for %s" % (font_name, app.config.language))
    download_file_if_missing('https://dl.espressif.com/dl/esp-idf/docs/_static/{}'.format(font_name), font_dir)

    font_path = os.path.abspath(os.path.join(font_dir, font_name))
    assert os.path.exists(font_path)

    app.config.blockdiag_fontpath = font_path
    app.config.seqdiag_fontpath = font_path
    app.config.actdiag_fontpath = font_path
    app.config.nwdiag_fontpath = font_path
    app.config.rackdiag_fontpath = font_path
    app.config.packetdiag_fontpath = font_path
