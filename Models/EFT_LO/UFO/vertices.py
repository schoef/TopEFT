# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 10.0 for Mac OS X x86 (64-bit) (September 10, 2014)
# Date: Thu 27 Jul 2017 17:29:36


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_9})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_74})

V_3 = Vertex(name = 'V_3',
             particles = [ P.g, P.g, P.G0, P.G0 ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.VVSS3 ],
             couplings = {(0,0):C.GC_27})

V_4 = Vertex(name = 'V_4',
             particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.VVSS3 ],
             couplings = {(0,0):C.GC_27})

V_5 = Vertex(name = 'V_5',
             particles = [ P.g, P.g, P.H, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.VVSS3 ],
             couplings = {(0,0):C.GC_27})

V_6 = Vertex(name = 'V_6',
             particles = [ P.g, P.g, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.VVS3 ],
             couplings = {(0,0):C.GC_76})

V_7 = Vertex(name = 'V_7',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV2, L.VVV3 ],
             couplings = {(0,1):C.GC_26,(0,0):C.GC_6})

V_8 = Vertex(name = 'V_8',
             particles = [ P.ghG, P.ghG__tilde__, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_6})

V_9 = Vertex(name = 'V_9',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV10, L.VVVV11, L.VVVV4, L.VVVV5, L.VVVV7, L.VVVV8 ],
             couplings = {(0,3):C.GC_42,(1,1):C.GC_42,(2,0):C.GC_42,(1,4):C.GC_8,(0,2):C.GC_8,(2,5):C.GC_8})

V_10 = Vertex(name = 'V_10',
              particles = [ P.g, P.g, P.g, P.G0, P.G0 ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVSS2 ],
              couplings = {(0,0):C.GC_43})

V_11 = Vertex(name = 'V_11',
              particles = [ P.g, P.g, P.g, P.G__minus__, P.G__plus__ ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVSS2 ],
              couplings = {(0,0):C.GC_43})

V_12 = Vertex(name = 'V_12',
              particles = [ P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVSS2 ],
              couplings = {(0,0):C.GC_43})

V_13 = Vertex(name = 'V_13',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS2 ],
              couplings = {(0,0):C.GC_82})

V_14 = Vertex(name = 'V_14',
              particles = [ P.g, P.g, P.g, P.g, P.G0, P.G0 ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVSS4, L.VVVVSS5, L.VVVVSS6 ],
              couplings = {(1,1):C.GC_49,(0,0):C.GC_49,(2,2):C.GC_49})

V_15 = Vertex(name = 'V_15',
              particles = [ P.g, P.g, P.g, P.g, P.G__minus__, P.G__plus__ ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVSS4, L.VVVVSS5, L.VVVVSS6 ],
              couplings = {(1,1):C.GC_49,(0,0):C.GC_49,(2,2):C.GC_49})

V_16 = Vertex(name = 'V_16',
              particles = [ P.g, P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVSS4, L.VVVVSS5, L.VVVVSS6 ],
              couplings = {(1,1):C.GC_49,(0,0):C.GC_49,(2,2):C.GC_49})

V_17 = Vertex(name = 'V_17',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS4, L.VVVVS5, L.VVVVS6 ],
              couplings = {(1,1):C.GC_84,(0,0):C.GC_84,(2,2):C.GC_84})

V_18 = Vertex(name = 'V_18',
              particles = [ P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-2,1,2)*f(-1,-2,3)*f(4,5,-1)', 'f(-2,1,2)*f(-1,-2,4)*f(3,5,-1)', 'f(-2,1,2)*f(-1,-2,5)*f(3,4,-1)', 'f(-2,1,3)*f(-1,-2,2)*f(4,5,-1)', 'f(-2,1,3)*f(-1,-2,4)*f(2,5,-1)', 'f(-2,1,3)*f(-1,-2,5)*f(2,4,-1)', 'f(-2,1,4)*f(-1,-2,2)*f(3,5,-1)', 'f(-2,1,4)*f(-1,-2,3)*f(2,5,-1)', 'f(-2,1,4)*f(-1,-2,5)*f(2,3,-1)', 'f(-2,1,5)*f(-1,-2,2)*f(3,4,-1)', 'f(-2,1,5)*f(-1,-2,3)*f(2,4,-1)', 'f(-2,1,5)*f(-1,-2,4)*f(2,3,-1)', 'f(-2,2,3)*f(-1,-2,1)*f(4,5,-1)', 'f(-2,2,3)*f(-1,-2,4)*f(1,5,-1)', 'f(-2,2,3)*f(-1,-2,5)*f(1,4,-1)', 'f(-2,2,4)*f(-1,-2,1)*f(3,5,-1)', 'f(-2,2,4)*f(-1,-2,3)*f(1,5,-1)', 'f(-2,2,4)*f(-1,-2,5)*f(1,3,-1)', 'f(-2,2,5)*f(-1,-2,1)*f(3,4,-1)', 'f(-2,2,5)*f(-1,-2,3)*f(1,4,-1)', 'f(-2,2,5)*f(-1,-2,4)*f(1,3,-1)', 'f(-2,3,4)*f(-1,-2,1)*f(2,5,-1)', 'f(-2,3,4)*f(-1,-2,2)*f(1,5,-1)', 'f(-2,3,4)*f(-1,-2,5)*f(1,2,-1)', 'f(-2,3,5)*f(-1,-2,1)*f(2,4,-1)', 'f(-2,3,5)*f(-1,-2,2)*f(1,4,-1)', 'f(-2,3,5)*f(-1,-2,4)*f(1,2,-1)', 'f(-2,4,5)*f(-1,-2,1)*f(2,3,-1)', 'f(-2,4,5)*f(-1,-2,2)*f(1,3,-1)', 'f(-2,4,5)*f(-1,-2,3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVV16, L.VVVVV17, L.VVVVV18, L.VVVVV19, L.VVVVV20, L.VVVVV21, L.VVVVV22, L.VVVVV23, L.VVVVV24, L.VVVVV25, L.VVVVV26, L.VVVVV27, L.VVVVV28, L.VVVVV29, L.VVVVV30 ],
              couplings = {(24,3):C.GC_48,(21,4):C.GC_47,(18,4):C.GC_48,(15,3):C.GC_47,(28,1):C.GC_48,(22,8):C.GC_48,(9,8):C.GC_47,(3,1):C.GC_47,(29,2):C.GC_48,(16,9):C.GC_48,(10,9):C.GC_47,(0,2):C.GC_47,(26,12):C.GC_47,(20,11):C.GC_47,(4,11):C.GC_48,(1,12):C.GC_48,(25,7):C.GC_48,(6,7):C.GC_47,(19,10):C.GC_48,(7,10):C.GC_47,(23,14):C.GC_47,(17,13):C.GC_47,(5,13):C.GC_48,(2,14):C.GC_48,(27,0):C.GC_48,(12,0):C.GC_47,(13,5):C.GC_48,(11,5):C.GC_47,(14,6):C.GC_47,(8,6):C.GC_48})

V_19 = Vertex(name = 'V_19',
              particles = [ P.g, P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-3,1,2)*f(-2,3,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,2)*f(-2,3,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,2)*f(-2,3,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,2)*f(-2,4,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,2)*f(-2,4,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,2)*f(-2,5,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,3)*f(-2,2,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,3)*f(-2,2,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,3)*f(-2,2,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,3)*f(-2,4,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,3)*f(-2,4,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,3)*f(-2,5,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,4)*f(-2,2,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,4)*f(-2,2,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,4)*f(-2,2,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,4)*f(-2,3,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,4)*f(-2,3,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,4)*f(-2,5,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,5)*f(-2,2,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,5)*f(-2,2,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,5)*f(-2,2,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,5)*f(-2,3,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,5)*f(-2,3,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,5)*f(-2,4,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,6)*f(-2,2,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,6)*f(-2,2,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,6)*f(-2,2,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,6)*f(-2,3,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,6)*f(-2,3,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,6)*f(-2,4,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,2,3)*f(-2,1,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,3)*f(-2,1,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,3)*f(-2,1,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,3)*f(-2,4,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,3)*f(-2,4,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,3)*f(-2,5,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,4)*f(-2,1,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,4)*f(-2,1,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,4)*f(-2,1,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,4)*f(-2,3,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,4)*f(-2,3,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,5)*f(-2,1,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,5)*f(-2,1,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,5)*f(-2,1,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,5)*f(-2,3,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,6)*f(-2,1,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,6)*f(-2,1,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,6)*f(-2,1,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,3,4)*f(-2,1,2)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,3,4)*f(-2,1,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,4)*f(-2,1,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,4)*f(-2,2,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,4)*f(-2,2,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,5)*f(-2,1,2)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,3,5)*f(-2,1,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,5)*f(-2,2,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,6)*f(-2,1,2)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,3,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,5)*f(-2,1,2)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,4,5)*f(-2,1,3)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,4,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,5)*f(-2,2,3)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,4,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,4,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,4,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,4,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,5,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,5,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,5,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,5,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,5,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,5,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVVV16, L.VVVVVV17, L.VVVVVV18, L.VVVVVV19, L.VVVVVV20, L.VVVVVV21, L.VVVVVV22, L.VVVVVV23, L.VVVVVV24, L.VVVVVV25, L.VVVVVV26, L.VVVVVV27, L.VVVVVV28, L.VVVVVV29, L.VVVVVV30 ],
              couplings = {(65,3):C.GC_51,(71,5):C.GC_50,(77,5):C.GC_51,(83,3):C.GC_50,(41,1):C.GC_51,(53,9):C.GC_51,(76,9):C.GC_50,(88,1):C.GC_50,(35,2):C.GC_51,(52,12):C.GC_51,(64,12):C.GC_50,(87,2):C.GC_50,(34,11):C.GC_50,(40,10):C.GC_50,(69,10):C.GC_51,(81,11):C.GC_51,(17,2):C.GC_50,(23,11):C.GC_51,(80,11):C.GC_50,(86,2):C.GC_51,(11,1):C.GC_50,(22,10):C.GC_51,(68,10):C.GC_50,(85,1):C.GC_51,(9,9):C.GC_50,(15,12):C.GC_50,(61,12):C.GC_51,(73,9):C.GC_51,(4,3):C.GC_50,(14,12):C.GC_51,(49,12):C.GC_50,(78,3):C.GC_51,(3,5):C.GC_51,(19,10):C.GC_50,(37,10):C.GC_51,(72,5):C.GC_50,(2,5):C.GC_50,(8,9):C.GC_51,(48,9):C.GC_50,(66,5):C.GC_51,(1,3):C.GC_51,(18,11):C.GC_50,(31,11):C.GC_51,(60,3):C.GC_50,(6,1):C.GC_51,(12,2):C.GC_51,(30,2):C.GC_50,(36,1):C.GC_50,(47,7):C.GC_51,(82,7):C.GC_50,(46,13):C.GC_51,(70,13):C.GC_50,(33,14):C.GC_50,(39,8):C.GC_50,(63,8):C.GC_51,(75,14):C.GC_51,(29,14):C.GC_51,(74,14):C.GC_50,(28,8):C.GC_51,(62,8):C.GC_50,(10,7):C.GC_50,(16,13):C.GC_50,(67,13):C.GC_51,(79,7):C.GC_51,(25,8):C.GC_50,(38,8):C.GC_51,(13,13):C.GC_51,(43,13):C.GC_50,(24,14):C.GC_50,(32,14):C.GC_51,(7,7):C.GC_51,(42,7):C.GC_50,(59,0):C.GC_51,(89,0):C.GC_50,(51,4):C.GC_51,(58,4):C.GC_50,(21,4):C.GC_50,(55,4):C.GC_51,(5,0):C.GC_50,(20,4):C.GC_51,(50,4):C.GC_50,(84,0):C.GC_51,(0,0):C.GC_51,(54,0):C.GC_50,(45,6):C.GC_50,(57,6):C.GC_51,(27,6):C.GC_51,(56,6):C.GC_50,(26,6):C.GC_50,(44,6):C.GC_51})

V_20 = Vertex(name = 'V_20',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_127,(0,1):C.GC_92})

V_21 = Vertex(name = 'V_21',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_94})

V_22 = Vertex(name = 'V_22',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_126,(0,1):C.GC_93})

V_23 = Vertex(name = 'V_23',
              particles = [ P.d__tilde__, P.t, P.t__tilde__, P.d ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF7, L.FFFF9 ],
              couplings = {(1,2):C.GC_12,(2,2):C.GC_10,(2,1):C.GC_24,(0,3):C.GC_15,(0,0):C.GC_16})

V_24 = Vertex(name = 'V_24',
              particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF7 ],
              couplings = {(1,1):C.GC_13,(2,1):C.GC_11,(0,0):C.GC_15})

V_25 = Vertex(name = 'V_25',
              particles = [ P.s__tilde__, P.t, P.t__tilde__, P.s ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF7, L.FFFF9 ],
              couplings = {(1,2):C.GC_12,(2,2):C.GC_10,(2,1):C.GC_24,(0,3):C.GC_15,(0,0):C.GC_16})

V_26 = Vertex(name = 'V_26',
              particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF7 ],
              couplings = {(1,1):C.GC_13,(2,1):C.GC_11,(0,0):C.GC_15})

V_27 = Vertex(name = 'V_27',
              particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF7, L.FFFF9 ],
              couplings = {(1,2):C.GC_13,(2,2):C.GC_11,(2,1):C.GC_25,(0,3):C.GC_16,(0,0):C.GC_17})

V_28 = Vertex(name = 'V_28',
              particles = [ P.b__tilde__, P.u, P.u__tilde__, P.b ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF7 ],
              couplings = {(1,1):C.GC_12,(2,1):C.GC_10,(0,0):C.GC_17})

V_29 = Vertex(name = 'V_29',
              particles = [ P.c__tilde__, P.t, P.t__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF7, L.FFFF9 ],
              couplings = {(1,2):C.GC_13,(2,2):C.GC_11,(2,1):C.GC_25,(0,3):C.GC_17,(0,0):C.GC_16})

V_30 = Vertex(name = 'V_30',
              particles = [ P.b__tilde__, P.c, P.c__tilde__, P.b ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF7 ],
              couplings = {(1,1):C.GC_12,(2,1):C.GC_10,(0,0):C.GC_17})

V_31 = Vertex(name = 'V_31',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_4})

V_32 = Vertex(name = 'V_32',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_52})

V_33 = Vertex(name = 'V_33',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_85})

V_34 = Vertex(name = 'V_34',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_5})

V_35 = Vertex(name = 'V_35',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_58})

V_36 = Vertex(name = 'V_36',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_53})

V_37 = Vertex(name = 'V_37',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV9 ],
              couplings = {(0,0):C.GC_59})

V_38 = Vertex(name = 'V_38',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_73})

V_39 = Vertex(name = 'V_39',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_91})

V_40 = Vertex(name = 'V_40',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_54})

V_41 = Vertex(name = 'V_41',
              particles = [ P.e__plus__, P.e__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_3})

V_42 = Vertex(name = 'V_42',
              particles = [ P.mu__plus__, P.mu__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_3})

V_43 = Vertex(name = 'V_43',
              particles = [ P.ta__plus__, P.ta__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_3})

V_44 = Vertex(name = 'V_44',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_2})

V_45 = Vertex(name = 'V_45',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_2})

V_46 = Vertex(name = 'V_46',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV4, L.FFV6 ],
              couplings = {(0,1):C.GC_2,(0,2):C.GC_168,(0,0):C.GC_89})

V_47 = Vertex(name = 'V_47',
              particles = [ P.d__tilde__, P.d, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_1})

V_48 = Vertex(name = 'V_48',
              particles = [ P.s__tilde__, P.s, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_1})

V_49 = Vertex(name = 'V_49',
              particles = [ P.b__tilde__, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_1})

V_50 = Vertex(name = 'V_50',
              particles = [ P.u__tilde__, P.u, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_7})

V_51 = Vertex(name = 'V_51',
              particles = [ P.c__tilde__, P.c, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_7})

V_52 = Vertex(name = 'V_52',
              particles = [ P.t__tilde__, P.t, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV10, L.FFV4, L.FFV6 ],
              couplings = {(0,1):C.GC_7,(0,2):C.GC_143,(0,0):C.GC_77})

V_53 = Vertex(name = 'V_53',
              particles = [ P.d__tilde__, P.d, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_7})

V_54 = Vertex(name = 'V_54',
              particles = [ P.s__tilde__, P.s, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_7})

V_55 = Vertex(name = 'V_55',
              particles = [ P.b__tilde__, P.b, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_7})

V_56 = Vertex(name = 'V_56',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_55})

V_57 = Vertex(name = 'V_57',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_55})

V_58 = Vertex(name = 'V_58',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5, L.FFV6 ],
              couplings = {(0,1):C.GC_163,(0,0):C.GC_55})

V_59 = Vertex(name = 'V_59',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_90})

V_60 = Vertex(name = 'V_60',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_55})

V_61 = Vertex(name = 'V_61',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_55})

V_62 = Vertex(name = 'V_62',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV5 ],
              couplings = {(0,0):C.GC_78,(0,1):C.GC_55})

V_63 = Vertex(name = 'V_63',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_106})

V_64 = Vertex(name = 'V_64',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_55})

V_65 = Vertex(name = 'V_65',
              particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_55})

V_66 = Vertex(name = 'V_66',
              particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_55})

V_67 = Vertex(name = 'V_67',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_55})

V_68 = Vertex(name = 'V_68',
              particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_55})

V_69 = Vertex(name = 'V_69',
              particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_55})

V_70 = Vertex(name = 'V_70',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5, L.FFV9 ],
              couplings = {(0,0):C.GC_57,(0,1):C.GC_67})

V_71 = Vertex(name = 'V_71',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5, L.FFV9 ],
              couplings = {(0,0):C.GC_57,(0,1):C.GC_67})

V_72 = Vertex(name = 'V_72',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV5, L.FFV6, L.FFV9 ],
              couplings = {(0,1):C.GC_57,(0,3):C.GC_67,(0,2):C.GC_164,(0,0):C.GC_79})

V_73 = Vertex(name = 'V_73',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_136})

V_74 = Vertex(name = 'V_74',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5, L.FFV7 ],
              couplings = {(0,0):C.GC_56,(0,1):C.GC_67})

V_75 = Vertex(name = 'V_75',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5, L.FFV7 ],
              couplings = {(0,0):C.GC_56,(0,1):C.GC_67})

V_76 = Vertex(name = 'V_76',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5, L.FFV7 ],
              couplings = {(0,0):C.GC_56,(0,1):C.GC_67})

V_77 = Vertex(name = 'V_77',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_135})

V_78 = Vertex(name = 'V_78',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_72})

V_79 = Vertex(name = 'V_79',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_72})

V_80 = Vertex(name = 'V_80',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV5 ],
              couplings = {(0,0):C.GC_72})

V_81 = Vertex(name = 'V_81',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV5, L.FFV8 ],
              couplings = {(0,0):C.GC_56,(0,1):C.GC_68})

V_82 = Vertex(name = 'V_82',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV5, L.FFV8 ],
              couplings = {(0,0):C.GC_56,(0,1):C.GC_68})

V_83 = Vertex(name = 'V_83',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV5, L.FFV8 ],
              couplings = {(0,0):C.GC_56,(0,1):C.GC_68})

V_84 = Vertex(name = 'V_84',
              particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
              lorentz = [ L.FFFF8 ],
              couplings = {(0,0):C.GC_14,(1,0):C.GC_23})

V_85 = Vertex(name = 'V_85',
              particles = [ P.s__tilde__, P.c, P.t__tilde__, P.b ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
              lorentz = [ L.FFFF8 ],
              couplings = {(0,0):C.GC_14,(1,0):C.GC_23})

V_86 = Vertex(name = 'V_86',
              particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
              lorentz = [ L.FFFF8 ],
              couplings = {(0,0):C.GC_14,(1,0):C.GC_23})

V_87 = Vertex(name = 'V_87',
              particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
              lorentz = [ L.FFFF8 ],
              couplings = {(0,0):C.GC_14,(1,0):C.GC_23})

V_88 = Vertex(name = 'V_88',
              particles = [ P.t__tilde__, P.t, P.G__minus__, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS5, L.FFSS6 ],
              couplings = {(0,0):C.GC_18,(0,1):C.GC_96})

V_89 = Vertex(name = 'V_89',
              particles = [ P.t__tilde__, P.b, P.G0, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS5, L.FFSS6 ],
              couplings = {(0,0):C.GC_21,(0,1):C.GC_98})

V_90 = Vertex(name = 'V_90',
              particles = [ P.t__tilde__, P.b, P.G__plus__, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS5, L.FFSS6 ],
              couplings = {(0,0):C.GC_97,(0,1):C.GC_22})

V_91 = Vertex(name = 'V_91',
              particles = [ P.b__tilde__, P.b, P.G__minus__, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS5, L.FFSS6 ],
              couplings = {(0,0):C.GC_19,(0,1):C.GC_95})

V_92 = Vertex(name = 'V_92',
              particles = [ P.t__tilde__, P.t, P.a, P.G__minus__, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS2 ],
              couplings = {(0,0):C.GC_112})

V_93 = Vertex(name = 'V_93',
              particles = [ P.b__tilde__, P.b, P.a, P.G__minus__, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS2 ],
              couplings = {(0,0):C.GC_111})

V_94 = Vertex(name = 'V_94',
              particles = [ P.t__tilde__, P.b, P.a, P.G0, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS2 ],
              couplings = {(0,0):C.GC_101})

V_95 = Vertex(name = 'V_95',
              particles = [ P.t__tilde__, P.b, P.a, P.G__plus__, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS2 ],
              couplings = {(0,0):C.GC_100})

V_96 = Vertex(name = 'V_96',
              particles = [ P.t__tilde__, P.b, P.a, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS4, L.FFVS6 ],
              couplings = {(0,1):C.GC_69,(0,0):C.GC_104})

V_97 = Vertex(name = 'V_97',
              particles = [ P.t__tilde__, P.t, P.G0, P.G0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS8 ],
              couplings = {(0,0):C.GC_108})

V_98 = Vertex(name = 'V_98',
              particles = [ P.t__tilde__, P.t, P.G0, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS7 ],
              couplings = {(0,0):C.GC_107})

V_99 = Vertex(name = 'V_99',
              particles = [ P.t__tilde__, P.t, P.G0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_125})

V_100 = Vertex(name = 'V_100',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS8 ],
               couplings = {(0,0):C.GC_108})

V_101 = Vertex(name = 'V_101',
               particles = [ P.b__tilde__, P.t, P.G0, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS5, L.FFSS6 ],
               couplings = {(0,0):C.GC_98,(0,1):C.GC_21})

V_102 = Vertex(name = 'V_102',
               particles = [ P.b__tilde__, P.t, P.G__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS5, L.FFSS6 ],
               couplings = {(0,0):C.GC_20,(0,1):C.GC_99})

V_103 = Vertex(name = 'V_103',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_75})

V_104 = Vertex(name = 'V_104',
               particles = [ P.b__tilde__, P.b, P.G0, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS8 ],
               couplings = {(0,0):C.GC_109})

V_105 = Vertex(name = 'V_105',
               particles = [ P.b__tilde__, P.b, P.G0, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS7 ],
               couplings = {(0,0):C.GC_110})

V_106 = Vertex(name = 'V_106',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_128})

V_107 = Vertex(name = 'V_107',
               particles = [ P.b__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS8 ],
               couplings = {(0,0):C.GC_109})

V_108 = Vertex(name = 'V_108',
               particles = [ P.b__tilde__, P.t, P.a, P.G0, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_37})

V_109 = Vertex(name = 'V_109',
               particles = [ P.b__tilde__, P.t, P.a, P.G__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_38})

V_110 = Vertex(name = 'V_110',
               particles = [ P.b__tilde__, P.t, P.a, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_160,(0,0):C.GC_80})

V_111 = Vertex(name = 'V_111',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS5, L.FFVS6 ],
               couplings = {(0,0):C.GC_162,(0,1):C.GC_70})

V_112 = Vertex(name = 'V_112',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_60})

V_113 = Vertex(name = 'V_113',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_115})

V_114 = Vertex(name = 'V_114',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.G__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_116})

V_115 = Vertex(name = 'V_115',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_130,(0,1):C.GC_33})

V_116 = Vertex(name = 'V_116',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_114})

V_117 = Vertex(name = 'V_117',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.G__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_113})

V_118 = Vertex(name = 'V_118',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_129})

V_119 = Vertex(name = 'V_119',
               particles = [ P.t__tilde__, P.t, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_114})

V_120 = Vertex(name = 'V_120',
               particles = [ P.t__tilde__, P.t, P.W__plus__, P.G__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_116})

V_121 = Vertex(name = 'V_121',
               particles = [ P.t__tilde__, P.t, P.W__plus__, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS5 ],
               couplings = {(0,0):C.GC_130,(0,1):C.GC_147})

V_122 = Vertex(name = 'V_122',
               particles = [ P.b__tilde__, P.b, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_115})

V_123 = Vertex(name = 'V_123',
               particles = [ P.b__tilde__, P.b, P.W__plus__, P.G__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_113})

V_124 = Vertex(name = 'V_124',
               particles = [ P.b__tilde__, P.b, P.W__plus__, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_129})

V_125 = Vertex(name = 'V_125',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.G0, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_60})

V_126 = Vertex(name = 'V_126',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_60})

V_127 = Vertex(name = 'V_127',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_146,(0,0):C.GC_86})

V_128 = Vertex(name = 'V_128',
               particles = [ P.t__tilde__, P.t, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_118})

V_129 = Vertex(name = 'V_129',
               particles = [ P.b__tilde__, P.b, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_119})

V_130 = Vertex(name = 'V_130',
               particles = [ P.t__tilde__, P.b, P.Z, P.G0, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_122})

V_131 = Vertex(name = 'V_131',
               particles = [ P.t__tilde__, P.b, P.Z, P.G__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_124})

V_132 = Vertex(name = 'V_132',
               particles = [ P.t__tilde__, P.b, P.Z, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_34,(0,0):C.GC_134})

V_133 = Vertex(name = 'V_133',
               particles = [ P.b__tilde__, P.t, P.Z, P.G0, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_123})

V_134 = Vertex(name = 'V_134',
               particles = [ P.b__tilde__, P.t, P.Z, P.G__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_121})

V_135 = Vertex(name = 'V_135',
               particles = [ P.b__tilde__, P.t, P.Z, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_148,(0,0):C.GC_133})

V_136 = Vertex(name = 'V_136',
               particles = [ P.t__tilde__, P.t, P.Z, P.G0, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_120})

V_137 = Vertex(name = 'V_137',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_120})

V_138 = Vertex(name = 'V_138',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS5, L.FFVS6 ],
               couplings = {(0,0):C.GC_132,(0,1):C.GC_150,(0,2):C.GC_35})

V_139 = Vertex(name = 'V_139',
               particles = [ P.b__tilde__, P.b, P.Z, P.G0, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_117})

V_140 = Vertex(name = 'V_140',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_117})

V_141 = Vertex(name = 'V_141',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_131})

V_142 = Vertex(name = 'V_142',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_103})

V_143 = Vertex(name = 'V_143',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.G__minus__, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_102})

V_144 = Vertex(name = 'V_144',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.G0, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_102})

V_145 = Vertex(name = 'V_145',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_102})

V_146 = Vertex(name = 'V_146',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_31,(0,0):C.GC_105})

V_147 = Vertex(name = 'V_147',
               particles = [ P.b__tilde__, P.t, P.g, P.G__minus__ ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS5 ],
               couplings = {(0,0):C.GC_137})

V_148 = Vertex(name = 'V_148',
               particles = [ P.t__tilde__, P.t, P.g, P.G0 ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS5, L.FFVS6 ],
               couplings = {(0,0):C.GC_138,(0,1):C.GC_30})

V_149 = Vertex(name = 'V_149',
               particles = [ P.t__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS5, L.FFVS6 ],
               couplings = {(0,0):C.GC_139,(0,1):C.GC_29})

V_150 = Vertex(name = 'V_150',
               particles = [ P.b__tilde__, P.t, P.g, P.g, P.G__minus__ ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS3 ],
               couplings = {(0,0):C.GC_140})

V_151 = Vertex(name = 'V_151',
               particles = [ P.t__tilde__, P.t, P.g, P.g, P.G0 ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS3, L.FFVVS4 ],
               couplings = {(0,0):C.GC_142,(0,1):C.GC_46})

V_152 = Vertex(name = 'V_152',
               particles = [ P.t__tilde__, P.t, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS3, L.FFVVS4 ],
               couplings = {(0,0):C.GC_141,(0,1):C.GC_45})

V_153 = Vertex(name = 'V_153',
               particles = [ P.t__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,0):C.GC_144,(0,1):C.GC_83})

V_154 = Vertex(name = 'V_154',
               particles = [ P.t__tilde__, P.t, P.a, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS5, L.FFVS6 ],
               couplings = {(0,0):C.GC_161,(0,1):C.GC_71})

V_155 = Vertex(name = 'V_155',
               particles = [ P.t__tilde__, P.t, P.Z, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS5, L.FFVS6 ],
               couplings = {(0,0):C.GC_149,(0,1):C.GC_36})

V_156 = Vertex(name = 'V_156',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS5 ],
               couplings = {(0,0):C.GC_145})

V_157 = Vertex(name = 'V_157',
               particles = [ P.t__tilde__, P.t, P.a, P.W__plus__, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS3 ],
               couplings = {(0,0):C.GC_153})

V_158 = Vertex(name = 'V_158',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS3 ],
               couplings = {(0,0):C.GC_151})

V_159 = Vertex(name = 'V_159',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS3 ],
               couplings = {(0,0):C.GC_152})

V_160 = Vertex(name = 'V_160',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3 ],
               couplings = {(0,0):C.GC_165})

V_161 = Vertex(name = 'V_161',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS3, L.FFVVS4 ],
               couplings = {(0,0):C.GC_155,(0,1):C.GC_63})

V_162 = Vertex(name = 'V_162',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS3, L.FFVVS4 ],
               couplings = {(0,0):C.GC_156,(0,1):C.GC_62})

V_163 = Vertex(name = 'V_163',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3, L.FFVV4 ],
               couplings = {(0,0):C.GC_166,(0,1):C.GC_87})

V_164 = Vertex(name = 'V_164',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.W__plus__, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS3 ],
               couplings = {(0,0):C.GC_154})

V_165 = Vertex(name = 'V_165',
               particles = [ P.t__tilde__, P.t, P.W__plus__, P.Z, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS3 ],
               couplings = {(0,0):C.GC_159})

V_166 = Vertex(name = 'V_166',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS3 ],
               couplings = {(0,0):C.GC_158})

V_167 = Vertex(name = 'V_167',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS3 ],
               couplings = {(0,0):C.GC_157})

V_168 = Vertex(name = 'V_168',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3 ],
               couplings = {(0,0):C.GC_167})

V_169 = Vertex(name = 'V_169',
               particles = [ P.t__tilde__, P.b, P.g, P.G__plus__ ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS6 ],
               couplings = {(0,0):C.GC_28})

V_170 = Vertex(name = 'V_170',
               particles = [ P.t__tilde__, P.b, P.g, P.g, P.G__plus__ ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_44})

V_171 = Vertex(name = 'V_171',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS6 ],
               couplings = {(0,0):C.GC_32})

V_172 = Vertex(name = 'V_172',
               particles = [ P.t__tilde__, P.t, P.a, P.W__minus__, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_41})

V_173 = Vertex(name = 'V_173',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_39})

V_174 = Vertex(name = 'V_174',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_40})

V_175 = Vertex(name = 'V_175',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_81})

V_176 = Vertex(name = 'V_176',
               particles = [ P.t__tilde__, P.b, P.W__minus__, P.W__plus__, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_61})

V_177 = Vertex(name = 'V_177',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.Z, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_66})

V_178 = Vertex(name = 'V_178',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_65})

V_179 = Vertex(name = 'V_179',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_64})

V_180 = Vertex(name = 'V_180',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_88})

