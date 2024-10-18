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

