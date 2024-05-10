__author__ = "Nigel Abrera"
__date__ = "May 7th, 2024"

import pytest
import json

pytestmark = pytest.mark.django_db

# End to end testing

class TestCategoryEndpoints:

  endpoint = '/api/category/'

  def test_category_get(self, category_factory, api_client):
    # Arrange
    # For single entry
    # category_factory()
    # For multiple entrees
    category_factory.create_batch(5)

    # Act
    response = api_client().get(self.endpoint)

    # Assert
    assert response.status_code == 200

    # Counting the length of the list
    assert len(json.loads(response.content)) == 5


class TestBrandEndpoints:

  endpoint = '/api/brand/'

  def test_brand_get(self, brand_factory, api_client):
    # Arrange
    # For single entry
    # brand_factory()
    # For multiple entrees
    brand_factory.create_batch(5)

    # Act
    response = api_client().get(self.endpoint)

    # Assert
    assert response.status_code == 200

    # Counting the length of the list
    assert len(json.loads(response.content)) == 5


class TestProductEndpoints:

  endpoint = '/api/product/'

  def test_product_get(self, product_factory, api_client):
    # Arrange
    # For single entry
    # product_factory()
    # For multiple entrees
    product_factory.create_batch(5)

    # Act
    response = api_client().get(self.endpoint)

    # Assert
    assert response.status_code == 200

    # Counting the length of the list
    assert len(json.loads(response.content)) == 5