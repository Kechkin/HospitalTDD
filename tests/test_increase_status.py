from Hospital import Hospital
import pytest


def test_increase_status():
    entity = Hospital([1, 0, 1])
    entity.increase_status(patient_id=2)
    assert entity._list_of_patient == [1, 1, 1]
