from Hospital import Hospital
import pytest


def test_increase_status():
    entity = Hospital([1, 0, 1])
    entity.increase_status(patient_id=2)
    assert entity._list_of_patient == [1, 1, 1]


def test_if_patient_id_is_not_on_the_list():
    entity = Hospital([1, 1, 1])
    with pytest.raises(IndexError):
        entity.increase_status(patient_id=5)
