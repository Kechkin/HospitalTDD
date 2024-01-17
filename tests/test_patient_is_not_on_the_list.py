from Hospital import Hospital
import pytest


def test_if_patient_is_not_on_the_list():
    entity = Hospital([1, 1, 1])
    with pytest.raises(ExceptionNoPatientInHospital) as error:
        entity.check_if_patient_is_on_the_list(patient=5)
    assert error == 'Ошибка. В больнице нет пациента с таким ID'
