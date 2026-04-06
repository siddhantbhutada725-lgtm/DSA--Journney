select patient_id,patient_name,conditions
from Patients
where  conditions Like 'DIAB1%' OR conditions LIKE '%DIAB1%'