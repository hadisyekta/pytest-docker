import pytest
from scripts import data_processor, map_population_update

POPULATION_DICT = {
        'Andorra': 77142,
        'Argentina': 44780677,
        'Cape Verde': 546388,
        'Germany': 83670653,
        'Greece': 10473455,
        'India': 1366417754,
        'Japan': 128860301,
        'Morocco': 36471769,
        'Senegal': 16296364,
        'United States': 329064917
}


def test_data_populateion_field_update(prep_transform_data):
    "Happy Path"
    map_data = prep_transform_data
    map_data.add_population(POPULATION_DICT)
    for row in map_data.get_data():
        assert 'Population' in row
        assert 'Updated' in row


def test_data_populateion_field_no_update(prep_transform_data):
    "Sad path"
    map_data = prep_transform_data
    map_data.add_population(POPULATION_DICT)

    with pytest.raises(Exception) as e:
        map_data.add_population(POPULATION_DICT)
        assert(str(e.value) == 'You cannot transform the data twice')


@pytest.fixture(scope='session')
def get_my_file_location():
    yield 'tests/resources/cities/clean_map.csv'


@pytest.fixture(scope='function')
def prep_transform_data(get_my_file_location):
    data = data_processor.mycsv_reader(get_my_file_location)
    map_data = map_population_update.MapData(data, False)
    yield map_data


# def test_data_population_update():
#     """
#     Happy Path test
#     """
#     map_data_location = 'tests/resources/cities/clean_map.csv'
#     data = data_processor.csv_reader(map_data_location)
#     data_to_transform = map_population_update.MapData(data, False)

#     data_to_transform.add_population(population_dict)   # transform object in place

#     for row in data_to_transform.get_data():
#         assert 'Population' in row
#         assert 'Updated' in row


# def test_data_population_no_update():
#     """
#     Sad Path test: We don't want the data transformed twice

#     """

#     map_data_location = 'tests/resources/cities/clean_map.csv'
#     data = data_processor.csv_reader(map_data_location)
#     data_to_transform = map_population_update.MapData(data, False)

#     population_dict = {
#             'Andorra': 77142,
#             'Argentina': 44780677,
#             'Cape Verde': 546388,
#             'Germany': 83670653,
#             'Greece': 10473455,
#             'India': 1366417754,
#             'Japan': 128860301,
#             'Morocco': 36471769,
#             'Senegal': 16296364,
#             'United States': 329064917
#     }

#     data_to_transform.add_population(population_dict)   # transform object in place
#     # Try calling the function again
#     with pytest.raises(Exception) as e:
#         data_to_transform.add_population(population_dict)
#     assert str(e.value) == 'You cannot transform the data twice'
