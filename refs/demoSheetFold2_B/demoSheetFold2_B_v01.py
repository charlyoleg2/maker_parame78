# freecad-python generated by Parametrix
# run the script with:
# freecad.cmd myScript.py

import FreeCAD as App
import Part

#print(sys.argv)
outFileName = "demoSheetFold2"
if (len(sys.argv) == 3):
    outFileName = sys.argv[2]
print(f"outFileName: {outFileName}")

def ctr_face_demoSheetFold2_facePattern_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(200.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(200.0000, 100.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(0.0000, 100.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(0.0000, 0.0000, 0)
	S003 = Part.LineSegment(P003, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_demoSheetFold2_facePattern_Fa0_Ctr1():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(100.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(96.1618, 103.1209, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(0.0000, 0.0000, 0)
	S002 = Part.LineSegment(P002, P000)
	aShape = Part.Shape([S000, S001, S002])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_demoSheetFold2_facePattern_Fa0_Ctr2():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(82.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(31.7181, 137.3862, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(0.0000, 0.0000, 0)
	S002 = Part.LineSegment(P002, P000)
	aShape = Part.Shape([S000, S001, S002])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_demoSheetFold2_facePattern_Fa0_Ctr3():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(82.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(65.4940, 44.1762, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(0.0000, 0.0000, 0)
	S002 = Part.LineSegment(P002, P000)
	aShape = Part.Shape([S000, S001, S002])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def ctr_face_demoSheetFold2_facePattern_Fa0_Ctr4():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(100.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(100.0000, 79.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(0.0000, 79.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(0.0000, 0.0000, 0)
	S003 = Part.LineSegment(P003, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_demoSheetFold2_facePattern_Fa0():
	FC000 = ctr_face_demoSheetFold2_facePattern_Fa0_Ctr0()
	FC001 = ctr_face_demoSheetFold2_facePattern_Fa0_Ctr1()
	FC002 = ctr_face_demoSheetFold2_facePattern_Fa0_Ctr2()
	FC003 = ctr_face_demoSheetFold2_facePattern_Fa0_Ctr3()
	FC004 = ctr_face_demoSheetFold2_facePattern_Fa0_Ctr4()
	rOneFace = FC000.cut([FC001, FC002, FC003, FC004])
	rOneFace.check()
	return rOneFace

def demoSheetFold2_facePattern():
	FA000 = face_demoSheetFold2_facePattern_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_demoSheetFold2_SFG_f00_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(200.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(200.0000, 100.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(0.0000, 100.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(0.0000, 0.0000, 0)
	S003 = Part.LineSegment(P003, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_demoSheetFold2_SFG_f00_Fa0():
	FC000 = ctr_face_demoSheetFold2_SFG_f00_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def demoSheetFold2_SFG_f00():
	FA000 = face_demoSheetFold2_SFG_f00_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_demoSheetFold2_SFG_f01_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 100.0000, 0)
	P001 = App.Vector(0.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(103.1209, 3.8382, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(0.0000, 100.0000, 0)
	S002 = Part.LineSegment(P002, P000)
	aShape = Part.Shape([S000, S001, S002])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_demoSheetFold2_SFG_f01_Fa0():
	FC000 = ctr_face_demoSheetFold2_SFG_f01_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def demoSheetFold2_SFG_f01():
	FA000 = face_demoSheetFold2_SFG_f01_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_demoSheetFold2_SFG_f02_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(79.8983, 18.4460, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(0.0000, 141.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(0.0000, 0.0000, 0)
	S002 = Part.LineSegment(P002, P000)
	aShape = Part.Shape([S000, S001, S002])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_demoSheetFold2_SFG_f02_Fa0():
	FC000 = ctr_face_demoSheetFold2_SFG_f02_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def demoSheetFold2_SFG_f02():
	FA000 = face_demoSheetFold2_SFG_f02_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_demoSheetFold2_SFG_f03_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 82.0000, 0)
	P001 = App.Vector(0.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(44.1762, 16.5060, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(0.0000, 82.0000, 0)
	S002 = Part.LineSegment(P002, P000)
	aShape = Part.Shape([S000, S001, S002])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_demoSheetFold2_SFG_f03_Fa0():
	FC000 = ctr_face_demoSheetFold2_SFG_f03_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def demoSheetFold2_SFG_f03():
	FA000 = face_demoSheetFold2_SFG_f03_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_demoSheetFold2_SFG_f04_Fa0_Ctr0():
	P000 = App.Vector(-0.0000, 0.0000, 0)
	P001 = App.Vector(100.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(100.0000, 79.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-0.0000, 79.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-0.0000, 0.0000, 0)
	S003 = Part.LineSegment(P003, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_demoSheetFold2_SFG_f04_Fa0():
	FC000 = ctr_face_demoSheetFold2_SFG_f04_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def demoSheetFold2_SFG_f04():
	FA000 = face_demoSheetFold2_SFG_f04_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_demoSheetFold2_SFG_fj00_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(19.5652, 9.4371, 0)
	P002 = App.Vector(24.3593, 30.6238, 0)
	S000 = Part.Arc(P000, P001, P002)
	P003 = App.Vector(14.6156, 28.3743, 0)
	S001 = Part.LineSegment(P002, P003)
	P004 = App.Vector(11.7391, 15.6623, 0)
	P005 = App.Vector(0.0000, 10.0000, 0)
	S002 = Part.Arc(P003, P004, P005)
	P006 = App.Vector(0.0000, 0.0000, 0)
	S003 = Part.LineSegment(P005, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_demoSheetFold2_SFG_fj00_Fa0():
	FC000 = ctr_face_demoSheetFold2_SFG_fj00_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def demoSheetFold2_SFG_fj00():
	FA000 = face_demoSheetFold2_SFG_fj00_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_demoSheetFold2_SFG_fj01_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(5.1303, -0.9046, 0)
	P002 = App.Vector(9.6418, -3.5093, 0)
	S000 = Part.Arc(P000, P001, P002)
	P003 = App.Vector(16.0697, 4.1511, 0)
	S001 = Part.LineSegment(P002, P003)
	P004 = App.Vector(8.5505, 8.4923, 0)
	P005 = App.Vector(0.0000, 10.0000, 0)
	S002 = Part.Arc(P003, P004, P005)
	P006 = App.Vector(0.0000, 0.0000, 0)
	S003 = Part.LineSegment(P005, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_demoSheetFold2_SFG_fj01_Fa0():
	FC000 = ctr_face_demoSheetFold2_SFG_fj01_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def demoSheetFold2_SFG_fj01():
	FA000 = face_demoSheetFold2_SFG_fj01_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_demoSheetFold2_SFG_fj02_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(17.5227, 7.1687, 0)
	P002 = App.Vector(24.9962, 24.5637, 0)
	S000 = Part.Arc(P000, P001, P002)
	P003 = App.Vector(14.9977, 24.7382, 0)
	S001 = Part.LineSegment(P002, P003)
	P004 = App.Vector(10.5136, 14.3012, 0)
	P005 = App.Vector(0.0000, 10.0000, 0)
	S002 = Part.Arc(P003, P004, P005)
	P006 = App.Vector(0.0000, 0.0000, 0)
	S003 = Part.LineSegment(P005, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_demoSheetFold2_SFG_fj02_Fa0():
	FC000 = ctr_face_demoSheetFold2_SFG_fj02_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def demoSheetFold2_SFG_fj02():
	FA000 = face_demoSheetFold2_SFG_fj02_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_demoSheetFold2_SFG_fj03_Fa0_Ctr0():
	P000 = App.Vector(0.0000, 0.0000, 0)
	P001 = App.Vector(12.3619, -6.5039, 0)
	P002 = App.Vector(14.0037, -20.3755, 0)
	S000 = Part.Arc(P000, P001, P002)
	P003 = App.Vector(23.3395, -23.9592, 0)
	S001 = Part.LineSegment(P002, P003)
	P004 = App.Vector(20.6032, -0.8398, 0)
	P005 = App.Vector(0.0000, 10.0000, 0)
	S002 = Part.Arc(P003, P004, P005)
	P006 = App.Vector(0.0000, 0.0000, 0)
	S003 = Part.LineSegment(P005, P000)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_demoSheetFold2_SFG_fj03_Fa0():
	FC000 = ctr_face_demoSheetFold2_SFG_fj03_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def demoSheetFold2_SFG_fj03():
	FA000 = face_demoSheetFold2_SFG_fj03_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def fex_subpax_SFG_f00():
	FIG = demoSheetFold2_SFG_f00()
	VEX = FIG.extrude(App.Vector(0, 0, 10))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(0.0000, 0.0000, 0.0000))
	return VFP
subpax_SFG_f00 = fex_subpax_SFG_f00()

def fex_subpax_SFG_f01():
	FIG = demoSheetFold2_SFG_f01()
	VEX = FIG.extrude(App.Vector(0, 0, 10))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -180.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), -77.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 180.0000)
	VFP = VR3.translate(App.Vector(224.3593, -0.0000, 30.6238))
	return VFP
subpax_SFG_f01 = fex_subpax_SFG_f01()

def fex_subpax_SFG_f02():
	FIG = demoSheetFold2_SFG_f02()
	VEX = FIG.extrude(App.Vector(0, 0, 10))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -70.3235)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), -40.8171)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 47.7559)
	VFP = VR3.translate(App.Vector(203.1023, 10.8898, 138.2983))
	return VFP
subpax_SFG_f02 = fex_subpax_SFG_f02()

def fex_subpax_SFG_f03():
	FIG = demoSheetFold2_SFG_f03()
	VEX = FIG.extrude(App.Vector(0, 0, 10))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 150.3370)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), -15.6326)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 151.4237)
	VFP = VR3.translate(App.Vector(181.1993, 8.9771, 165.5890))
	return VFP
subpax_SFG_f03 = fex_subpax_SFG_f03()

def fex_subpax_SFG_f04():
	FIG = demoSheetFold2_SFG_f04()
	VEX = FIG.extrude(App.Vector(0, 0, 10))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 17.8892)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), -37.2765)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), -81.6566)
	VFP = VR3.translate(App.Vector(146.3535, 40.5554, 209.2706))
	return VFP
subpax_SFG_f04 = fex_subpax_SFG_f04()

def fex_subpax_SFG_fj00():
	FIG = demoSheetFold2_SFG_fj00()
	VEX = FIG.extrude(App.Vector(0, 0, 100))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 90.0000)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0.0000)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0.0000)
	VFP = VR3.translate(App.Vector(200.0000, 100.0000, 0.0000))
	return VFP
subpax_SFG_fj00 = fex_subpax_SFG_fj00()

def fex_subpax_SFG_fj01():
	FIG = demoSheetFold2_SFG_fj01()
	VEX = FIG.extrude(App.Vector(0, 0, 141))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -17.5195)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), -41.6454)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 101.8472)
	VFP = VR3.translate(App.Vector(224.3593, 100.0000, 30.6238))
	return VFP
subpax_SFG_fj01 = fex_subpax_SFG_fj01()

def fex_subpax_SFG_fj02():
	FIG = demoSheetFold2_SFG_fj02()
	VEX = FIG.extrude(App.Vector(0, 0, 82))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 151.8677)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), -57.2865)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), -94.8667)
	VFP = VR3.translate(App.Vector(246.7884, 68.2329, 177.3788))
	return VFP
subpax_SFG_fj02 = fex_subpax_SFG_fj02()

def fex_subpax_SFG_fj03():
	FIG = demoSheetFold2_SFG_fj03()
	VEX = FIG.extrude(App.Vector(0, 0, 79))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), -106.2829)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), -29.3343)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 117.5488)
	VFP = VR3.translate(App.Vector(224.8854, 66.3203, 204.6695))
	return VFP
subpax_SFG_fj03 = fex_subpax_SFG_fj03()

def fvol_pax_demoSheetFold2():
	V000 = subpax_SFG_f00
	V001 = V000.fuse(subpax_SFG_f01)
	V002 = V001.fuse(subpax_SFG_f02)
	V003 = V002.fuse(subpax_SFG_f03)
	V004 = V003.fuse(subpax_SFG_f04)
	V005 = V004.fuse(subpax_SFG_fj00)
	V006 = V005.fuse(subpax_SFG_fj01)
	V007 = V006.fuse(subpax_SFG_fj02)
	V008 = V007.fuse(subpax_SFG_fj03)
	VFC = V008.removeSplitter()
	return VFC
pax_demoSheetFold2 = fvol_pax_demoSheetFold2()


pax_demoSheetFold2.check()
#pax_demoSheetFold2.exportBrep(f"{outFileName}.brep")
#pax_demoSheetFold2.exportIges(f"{outFileName}.igs")
#pax_demoSheetFold2.exportStep(f"{outFileName}.stp")
pax_demoSheetFold2.exportStl(f"{outFileName}.stl")

