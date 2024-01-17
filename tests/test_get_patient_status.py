
def test_get_status_name_by_patient_id():
    entity = Hospital([1, 0, 1])
    assert entity.get_status_name_by_patient_id(patient_id=2) == 'Тяжело болен'
