from scripts.chp2.mapmaker_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4650)
    assert p1.get_lat_long() == (14.7167, 17.4650)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Boenos Aires", 12.11386, -555.08269)
    assert str(exp.value) == 'Invalid Latitude or Longitude'
    # breakpoint()

    with pytest.raises(TypeError) as exp:
        Point(2, 12.11386, -555.08269)
    assert str(exp.value) == 'City name must be String'
    # breakpoint()
