__author__ = "Nigel Abrera"
__date__ = "May 7th, 2024"

# Unit testing

import pytest

# A marker to let the test have access to the db
# Intentionally conf. globally
pytestmark = pytest.mark.django_db


class TestCategoryModel:

  def test_str_method(self, category_factory):
    # Arrange
    # Act
    # Mocked and created data, hard coding it using
    # the the fiels of the table.
    obj = category_factory(name="test_category")

    # Assert
    # We are trying to isolate the __str__ function as best as possible
    # in order to test it
    assert obj.__str__() == "test_category"



class TestBrandModel:

  def test_str_method(self, brand_factory):
    # Arrange
    # Act
    # Mocked and created data, hard coding it using
    # the the fiels of the table.
    obj = brand_factory(name="test_brand")

    # Assert
    # We are trying to isolate the __str__ function as best as possible
    # in order to test it
    assert obj.__str__() == "test_brand"



class TestProductModel:

  def test_str_method(self, product_factory):
    # Arrange
    # Act
    # Mocked and created data, hard coding it using
    # the the fiels of the table.
    obj = product_factory(name="test_product")

    # Assert
    # We are trying to isolate the __str__ function as best as possible
    # in order to test it
    assert obj.__str__() == "test_product"
