# This method does not affect the current code, only will customize the terminal report
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    terminalreporter.section("Custom Summary")
    passed = len(terminalreporter.stats.get("passed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    terminalreporter.write(f"Passed: {passed}\n")
    terminalreporter.write(f"Failed: {failed}\n")

# This method does not affect the current code, only will customize the html title report
def pytest_html_report_title(report):
    report.title = "Custom Title - Dourado API report"
