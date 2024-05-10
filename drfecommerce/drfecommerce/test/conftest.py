from pytest_factoryboy import register
from rest_framework.test import APIClient
from .factories import CategoryFactory, BrandFactory, ProductFactory
import pytest

# Unit tests
# Registering the factories (Isolated structure)
register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)

# E2E tes
@pytest.fixture
def api_client():
  return APIClient