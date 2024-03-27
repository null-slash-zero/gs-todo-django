import pytest
from rest_framework.test import APIClient

from common.tests import BaseApiTestCase

@pytest.fixture(scope="function")
def api_client():
    """
    Fixture to provide an API client
    :return: APIClient
    """
    base_test = BaseApiTestCase()

    if not hasattr(base_test, 'client'):
        base_test.client = APIClient()

    yield base_test

    base_test.tearDownClass()