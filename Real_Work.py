import arcpy
import os
arcpy.env.workspace = r"H:\PythonGIS\Zhou\10_22_2019\geoportal.gdb" #set the input workspace.
arcpy.CreateFileGDB_management(r"H:\PythonGIS\Zhou\10_22_2019", "Output.gdb") #creat a gdb for all outputs.
outWorkspace = r"H:\PythonGIS\Zhou\10_22_2019\Output.gdb" #set the output workspace.
arcpy.env.overwriteOutput = True #set output workspace always overwrite.

try:
    fclist = arcpy.ListFeatureClasses(feature_type = "Point") #find all points in the vector files.
    for item in fclist:
        featureClassName = arcpy.ValidateFieldName(item + "_Clip", outWorkspace) #Set the name for outputs.
        outFC = os.path.join(outWorkspace, featureClassName)
        if item != os.path.basename("Area"): #clip each items.
            arcpy.Clip_analysis(item, "Area", outFC)

except:
    arcpy.GetMessages()
