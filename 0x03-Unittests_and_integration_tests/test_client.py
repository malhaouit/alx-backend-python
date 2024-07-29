#!/usr/bin/env python3
""""This module include tests for client.GithubOrgClient class."""

import unittest
from parameterized import parameterized
from unittest.mock import patch

GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test Case for client.GithubOrgClient class.
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    def test_org(self, org_name):
        """Test that GithubOrgClient.org method returns the correct value.
        """
        with patch('client.get_json') as mock_get_json:
            github_org_client = GithubOrgClient(org_name)
            response = github_org_client.org
            expected_url = GithubOrgClient.ORG_URL.format(org=org_name)
            mock_get_json.assert_called_once_with(expected_url)
