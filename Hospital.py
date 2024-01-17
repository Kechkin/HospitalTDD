class Hospital:
    def __init__(self, list_of_patient):
        self._list_of_patient = list_of_patient

    def increase_status(self, patient_id):
        self._list_of_patient[patient_id - 1] += 1

    def get_status_name_by_patient_id(self, patient_id):
        patient_statuses = {
            0: 'Тяжело болен',
            1: 'Болен',
            2: 'Слегка болен',
            3: 'Готов к выписке',
        }
        status_patient = self.list_of_patient[patient_id - 1]
        return patient_statuses.get(status_patient)
