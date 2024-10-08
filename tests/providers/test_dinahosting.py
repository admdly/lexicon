"""Integration tests for DigitalOcean"""

from unittest import TestCase

import pytest
from integration_tests import IntegrationTestsV2


# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from define_tests.TheTests
class DinahostingProviderTests(TestCase, IntegrationTestsV2):
    """Integration tests for Dinahosting provider"""

    provider_name = "dinahosting"
    domain = "itslikethesesweet.info"

    def _filter_headers(self):
        return ["Authorization", "Set-Cookie"]

    @pytest.mark.skip(reason="API does not expose record ttl")
    def test_provider_when_calling_list_records_after_setting_ttl(self):
        return
