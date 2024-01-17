from Hospital import Hospital
import pytest


def test_get_status_name_by_patient_id():
    entity = Hospital([1, 0, 1])
    assert entity.get_status_name_by_patient_id(patient_id=2) == 'Тяжело болен'


def test_get_all_statuses_name_by_patient_id():
    entity = Hospital([0, 1, 2, 3])
    assert entity.get_status_name_by_patient_id(patient_id=1) == 'Тяжело болен'
    assert entity.get_status_name_by_patient_id(patient_id=2) == 'Болен'
    assert entity.get_status_name_by_patient_id(patient_id=3) == 'Слегка болен'
    assert entity.get_status_name_by_patient_id(patient_id=4) == 'Готов к выписке'


def test_if_patient_id_is_not_on_the_list():
    entity = Hospital([0, 1, 2])
    with pytest.raises(IndexError):
        entity.get_status_name_by_patient_id(patient_id=5)
