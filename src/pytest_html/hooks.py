# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


def pytest_html_report_title(report):
    """ Called before adding the title to the report """


def pytest_html_results_summary(prefix, summary, postfix):
    """ Called before adding the summary section to the report """


def pytest_html_results_table_header(cells):
    """ Called after building results table header. """


def pytest_html_results_table_row(report, cells):
    """ Called after building results table row. """


def pytest_html_results_table_html(report, data):
    """ Called after building results table additional HTML. """


def pytest_html_modify_section(name, data):
    """ Called after the html for each section is generated. """


def pytest_html_modify_all_sections(sections):
    """
    Called before adding sections to the HTML body.

    Sections list can be modified inplace.

    """
