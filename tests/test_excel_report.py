"""Tests for excel-report."""

import pytest
from excel_report import report


class TestReport:
    """Test suite for report."""

    def test_basic(self):
        """Test basic usage."""
        result = report("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            report("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = report(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
