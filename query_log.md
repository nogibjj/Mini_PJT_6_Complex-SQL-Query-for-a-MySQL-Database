```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=63, TotalAttrition=12), Row(Department='Research & Development', TotalEmployees=961, TotalAttrition=133), Row(Department='Sales', TotalEmployees=446, TotalAttrition=92)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=567, TotalAttrition=108), Row(Department='Research & Development', TotalEmployees=8649, TotalAttrition=1197), Row(Department='Sales', TotalEmployees=4014, TotalAttrition=828)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=1008, TotalAttrition=192), Row(Department='Research & Development', TotalEmployees=15376, TotalAttrition=2128), Row(Department='Sales', TotalEmployees=7136, TotalAttrition=1472)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=1575, TotalAttrition=300), Row(Department='Research & Development', TotalEmployees=24025, TotalAttrition=3325), Row(Department='Sales', TotalEmployees=11150, TotalAttrition=2300)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=2268, TotalAttrition=432), Row(Department='Research & Development', TotalEmployees=34596, TotalAttrition=4788), Row(Department='Sales', TotalEmployees=16056, TotalAttrition=3312)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=3087, TotalAttrition=588), Row(Department='Research & Development', TotalEmployees=47089, TotalAttrition=6517), Row(Department='Sales', TotalEmployees=21854, TotalAttrition=4508)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=4032, TotalAttrition=768), Row(Department='Research & Development', TotalEmployees=61504, TotalAttrition=8512), Row(Department='Sales', TotalEmployees=28544, TotalAttrition=5888)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=5103, TotalAttrition=972), Row(Department='Research & Development', TotalEmployees=77841, TotalAttrition=10773), Row(Department='Sales', TotalEmployees=36126, TotalAttrition=7452)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=14112, TotalAttrition=2688), Row(Department='Research & Development', TotalEmployees=215264, TotalAttrition=29792), Row(Department='Sales', TotalEmployees=99904, TotalAttrition=20608)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=16065, TotalAttrition=3060), Row(Department='Research & Development', TotalEmployees=245055, TotalAttrition=33915), Row(Department='Sales', TotalEmployees=113730, TotalAttrition=23460)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=20349, TotalAttrition=3876), Row(Department='Research & Development', TotalEmployees=310403, TotalAttrition=42959), Row(Department='Sales', TotalEmployees=144058, TotalAttrition=29716)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=22680, TotalAttrition=4320), Row(Department='Research & Development', TotalEmployees=345960, TotalAttrition=47880), Row(Department='Sales', TotalEmployees=160560, TotalAttrition=33120)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=25137, TotalAttrition=4788), Row(Department='Research & Development', TotalEmployees=383439, TotalAttrition=53067), Row(Department='Sales', TotalEmployees=177954, TotalAttrition=36708)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=27720, TotalAttrition=5280), Row(Department='Research & Development', TotalEmployees=422840, TotalAttrition=58520), Row(Department='Sales', TotalEmployees=196240, TotalAttrition=40480)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=36225, TotalAttrition=6900), Row(Department='Research & Development', TotalEmployees=552575, TotalAttrition=76475), Row(Department='Sales', TotalEmployees=256450, TotalAttrition=52900)]
```

```sql

SELECT 
    a.Department, 
    COUNT(p.EmployeeNumber) AS TotalEmployees, 
    SUM(CASE WHEN a.Attrition = 'Yes' THEN 1 ELSE 0 END) AS TotalAttrition
FROM 
    hr_personal_data AS p
LEFT JOIN 
    hr_attrition_data AS a
ON 
    p.EmployeeNumber = a.EmployeeNumber
GROUP BY 
    a.Department
ORDER BY 
    a.Department ASC;

```

```response from databricks
[Row(Department='Human Resources', TotalEmployees=39312, TotalAttrition=7488), Row(Department='Research & Development', TotalEmployees=599664, TotalAttrition=82992), Row(Department='Sales', TotalEmployees=278304, TotalAttrition=57408)]
```

