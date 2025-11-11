use yasin;
select*from std;
select PatientID,PatientName,Age,Gender
from std;
SELECT PatientName, COUNT(*) AS patient_frequency 
FROM std GROUP BY PatientName ORDER BY patient_frequency DESC;
SELECT ROUND((SUM(CASE WHEN CanceledAppointment = 1 THEN 1 ELSE 0 END) / COUNT(*)) * 100,2) AS CanceledAppointment FROM std;