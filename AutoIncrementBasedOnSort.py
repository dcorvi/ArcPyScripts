import arcpy

from itertools import count
cntr = count()

# path to feature class
featureClass = arcpy.GetParameterAsText(0)
sortField = arcpy.GetParameterAsText(1)
autoIncrementField = arcpy.GetParameterAsText(2)

SQL = " \"ORDER BY sortField\" "

with arcpy.da.UpdateCursor(featureClass,[autoIncrementField, sortField],sql_clause=(None,SQL)) as cur:
    for i, j in cur:
        cur.updateRow([next(cntr), j])
