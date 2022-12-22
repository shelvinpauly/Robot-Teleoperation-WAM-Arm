# -*- coding: utf-8 -*-
"""ik.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q3opxGd21dfiZpkT8lQ6GkBNhxLwBk68
"""

from fk import*

z0= sym.Matrix([0,0,1])
z1= sym.Matrix(T01[0:3,2])
z2= sym.Matrix(T02[0:3,2])
z3= sym.Matrix(T03[0:3,2])
z4= sym.Matrix(T04[0:3,2])
z5= sym.Matrix(T05[0:3,2])
z6= sym.Matrix(T06[0:3,2])
z7= sym.Matrix(T07[0:3,2])
z8= sym.Matrix(T08[0:3,2])
z8

p0= sym.Matrix([0,0,0])
p1= sym.Matrix(T01[0:3,3])
p2= sym.Matrix(T02[0:3,3])
p4= sym.Matrix(T04[0:3,3])
p5= sym.Matrix(T05[0:3,3])
p6= sym.Matrix(T06[0:3,3])
p7= sym.Matrix(T07[0:3,3])
p= sym.Matrix(T08[0:3,3])
p

pj1 = diff(p,theta1)
pj1 = pj1.col_insert(1,sym.diff(p,theta2))
pj1 = pj1.col_insert(2,sym.diff(p,theta3))
pj1 = pj1.col_insert(3,sym.diff(p,theta4))
pj1 = pj1.col_insert(4,sym.diff(p,theta5))
pj1 = pj1.col_insert(5,sym.diff(p,theta6))
pj1 = pj1.col_insert(6,sym.diff(p,theta7))
pj1 = pj1.col_insert(7,sym.diff(p,theta8))
pj1

pj2 = z1
pj2 = pj2.col_insert(1,z2)
pj2 = pj2.col_insert(2,z3)
pj2 = pj2.col_insert(3,z4)
pj2 = pj2.col_insert(4,z5)
pj2 = pj2.col_insert(5,z6)
pj2 = pj2.col_insert(6,z7)
pj2 = pj2.col_insert(7,z8)
pj2

J = pj1.row_insert(3,pj2)
J

J_VAL = J.evalf(3, subs={theta1:tj[0],theta2:tj[1],theta3:tj[2],theta4:tj[3],theta5:tj[4],theta6:tj[5],theta7:tj[6],theta8:tj[7]})
J_VAL

#Jacobian Inverse
JI = J.evalf(3, subs={theta1:tj[0],theta2:tj[1],theta3:tj[2],theta4:tj[3],theta5:tj[4],theta6:tj[5],theta7:tj[6],theta8:tj[7]}).pinv()
JI