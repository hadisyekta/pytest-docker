import pytest

from scripts import data_processor


def test_csv_reader_header_fields(process_data_function):
    """
    Happy Path test to make sure the processed data
    contains the right header fields
    """
    # helper function imported from conftest.py to import file data with our csv reader
    data = process_data_function
    header_fields = list(data[0].keys())
    assert header_fields == [
            'Country',
            'City',
            'State_Or_Province',
            'Lat',
            'Long',
            'Altitude'
            ]


def test_csv_reader_data_contents(process_data_function):
    """
    Happy Path Test to examine that each row
    has the appropriate data type per field
    """
    data = process_data_function
    # breakpoint()

    # Check row types
    for row in data:
        assert(isinstance(row['Country'], str))
        assert(isinstance(row['City'], str))
        assert(isinstance(row['State_Or_Province'], str))
        assert(isinstance(row['Lat'], float))
        assert(isinstance(row['Long'], float))
        assert(isinstance(row['Altitude'], float))

    assert len(data) == 180
    assert data[0]['Country'] == 'Andorra'
    assert data[179]['Country'] == 'United States'

    # Basic data checks


@pytest.fixture(scope="module")
def city_list_location():
    # return 'tests/resources/cities/clean_map.csv'
    return 'tests/resources/cities/malformed_map.csv'


@pytest.fixture(scope="module")
def process_data_function(city_list_location):
    yield data_processor.csv_reader(city_list_location)


def test_myread_csv(my_data_processor_function):
    data = my_data_processor_function
    for row in data:
        assert(isinstance(row['Country'], str))
        assert(isinstance(row['City'], str))
        assert(isinstance(row['State_Or_Province'], str))
        assert(isinstance(row['Lat'], float))
        assert(isinstance(row['Long'], float))
        assert(isinstance(row['Altitude'], float))
    assert len(data) == 180


@pytest.fixture(scope="module")
def get_city_file_location():
    return 'tests/resources/cities/clean_map.csv'


@pytest.fixture(scope="module")
def my_data_processor_function(get_city_file_location):
    yield data_processor.mycsv_reader(get_city_file_location)
