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

