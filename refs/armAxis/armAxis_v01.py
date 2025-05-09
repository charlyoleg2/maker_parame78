# freecad-python generated by Parametrix
# run the script with:
# freecad.cmd myScript.py

import FreeCAD as App
import Part

#print(sys.argv)
outFileName = "armAxis"
if (len(sys.argv) == 3):
    outFileName = sys.argv[2]
print(f"outFileName: {outFileName}")

def ctr_face_armAxis_faceAxis_Fa0_Ctr0():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(10.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def ctr_face_armAxis_faceAxis_Fa0_Ctr1():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(7.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def face_armAxis_faceAxis_Fa0():
	FC000 = ctr_face_armAxis_faceAxis_Fa0_Ctr0()
	FC001 = ctr_face_armAxis_faceAxis_Fa0_Ctr1()
	rOneFace = FC000.cut([FC001])
	rOneFace.check()
	return rOneFace

def armAxis_faceAxis():
	FA000 = face_armAxis_faceAxis_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_armAxis_faceHoleS_Fa0_Ctr0():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(5.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def face_armAxis_faceHoleS_Fa0():
	FC000 = ctr_face_armAxis_faceHoleS_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def armAxis_faceHoleS():
	FA000 = face_armAxis_faceHoleS_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_armAxis_faceHoleL_Fa0_Ctr0():
	# Radius, XYZ-position, orientation
	aCircle = Part.makeCircle(10.0000, App.Vector(0.0000, 0.0000, 0), App.Vector(0, 0, 1))
	aWire = Part.Wire(aCircle)
	rFace = Part.Face(aWire)
	return rFace

def face_armAxis_faceHoleL_Fa0():
	FC000 = ctr_face_armAxis_faceHoleL_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def armAxis_faceHoleL():
	FA000 = face_armAxis_faceHoleL_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def fex_subpax_armAxis_Axis():
	FIG = armAxis_faceAxis()
	VEX = FIG.extrude(App.Vector(0, 0, 50))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 0.0000, 0.0000))
	return VFP
subpax_armAxis_Axis = fex_subpax_armAxis_Axis()

def fex_subpax_armAxis_HoleS():
	FIG = armAxis_faceHoleS()
	VEX = FIG.extrude(App.Vector(0, 0, 40))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 90.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 0.0000, 25.0000))
	return VFP
subpax_armAxis_HoleS = fex_subpax_armAxis_HoleS()

def fex_subpax_armAxis_HoleL():
	FIG = armAxis_faceHoleL()
	VEX = FIG.extrude(App.Vector(0, 0, 40))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -90.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(-10.0000, -20.0000, 25.0000))
	return VFP
subpax_armAxis_HoleL = fex_subpax_armAxis_HoleL()

def fvol_pax_armAxis():
	V000 = subpax_armAxis_Axis
	V001 = V000.cut(subpax_armAxis_HoleS)
	V002 = V001.cut(subpax_armAxis_HoleL)
	VFC = V002.removeSplitter()
	return VFC
pax_armAxis = fvol_pax_armAxis()


pax_armAxis.check()
#pax_armAxis.exportBrep(f"{outFileName}.brep")
#pax_armAxis.exportIges(f"{outFileName}.igs")
#pax_armAxis.exportStep(f"{outFileName}.stp")
pax_armAxis.exportStl(f"{outFileName}.stl")

