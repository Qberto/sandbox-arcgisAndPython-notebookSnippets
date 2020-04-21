# Generate Unique ID fields and Unique ID values for a feature class

arcpy.AddField_management('IHSZone_AddressPoints', "Unique_ID_Str", 'TEXT')

arcpy.AddField_management('IHSZone_AddressPoints', "Unique_ID_Int", 'LONG')

counter = 0
with arcpy.da.UpdateCursor('IHSZone_AddressPoints', ["Unique_ID_Str", "Unique_ID_Int"]) as cursor:
    for row in cursor:
        counter += 1
        row[0] = str(counter)
        row[1] = counter
        cursor.updateRow(row)