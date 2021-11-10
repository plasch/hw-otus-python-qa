import random

import requests
import pytest

"""
Tests for REST API - https://www.openbrewerydb.org/
Open Brewery DB is a free dataset and API with public information on breweries, cideries, brewpubs, and bottleshops.
"""


@pytest.fixture()
def brewery_id():
    response = requests.get("https://api.openbrewerydb.org/breweries")
    ids = []
    for i in response.json():
        ids.append(i['id'])
    return random.choice(ids)


def test_get_all_breweries_list():
    response = requests.get("https://api.openbrewerydb.org/breweries")
    data = response.json()
    assert response.status_code == 200
    assert not len(data) == 0, "List of all breweries is empty."


@pytest.mark.parametrize("filter_by, value", [
    ("by_city", "san_diego"),
    ("by_dist", "38.8977,77.0365"),
    ("by_name", "cooper"),
    ("by_state", "ohio"),
    ("by_postal", "44107")
])
def test_filter_brewery_by(filter_by, value):
    params = {filter_by: value}
    response = requests.get("https://api.openbrewerydb.org/breweries", params=params)
    assert response.status_code == 200
    data = response.json()
    assert not len(data) == 0, f"List of breweries filtering {filter_by} is empty."


@pytest.mark.parametrize("btype", ["large", "micro", "brewpub"])
def test_filter_by_type_of_brewery(btype):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_type={btype}")
    assert response.status_code == 200
    data = response.json()
    assert not len(data) == 0, "List of breweries filtering by type is empty."
    for i in data:
        assert i["brewery_type"] == btype, f"Type of brewery = {i['brewery_type']} doesn't match with filter by {btype}."


def test_get_brewery(brewery_id):
    response = requests.get(f"https://api.openbrewerydb.org/breweries/{brewery_id}")
    assert response.status_code == 200
    data = response.json()
    assert brewery_id == data["id"], "ID's doesn't match"


def test_search_brewery():
    query = "dog"
    response = requests.get(f"https://api.openbrewerydb.org/breweries/search?query={query}")
    assert response.status_code == 200
    data = response.json()
    assert not len(data) == 0, f"List of search results by query '{query}' is empty."
