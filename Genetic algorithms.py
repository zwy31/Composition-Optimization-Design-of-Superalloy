# -*- coding: utf-8 -*-
import geatpy as ea  # import geatpy
import numpy as np





class MyProblem(ea.Problem):
    def __init__(self, M=2):
        name = 'MyProblem'
        Dim = 10#Dimension of decision variable
        maxormins = [-1] * M
        varTypes = [1] * Dim
        lb = [0] * Dim # Lower bound of decision variable
        ub = [200] * Dim # Upper bound of decision variable
        lbin = [1] * Dim# Lower boundary of decision variable (0 means the lower boundary excluding the variable, 1 means including)
        ubin = [1] * Dim# Upper boundary of decision variable (0 represents the lower boundary excluding the variable, 1 represents the included)
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop):
        Vars = pop.Phen # Decision variable matrix
        x1 = Vars[:, [0]]
        x2 = Vars[:, [1]]
        x3 = Vars[:, [2]]
        x4 = Vars[:, [3]]
        x5 = Vars[:, [4]]
        x6 = Vars[:, [5]]
        x7 = Vars[:, [6]]
        x8 = Vars[:, [7]]
        x9 = Vars[:, [8]]
        x10 = Vars[:, [9]]

        strength = (b1 * x1 + b2 * x2 + b3 * x3 + b4 * x4 + b5 * x5 + b6 * x6 + b7 * x7 + b8 * x8 + b9 * x9 + b10 * x10 + b11 * (1000 - x1 - x2 - x3 - x4 - x5 - x6 - x7 - x8 - x9 - x10))
        #b1 (2,3..) Represents the strength coefficient of each element, see in the article
        density = -((x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + (1000-x1-x2-x3-x4-x5-x6-x7-x8-x9-x10))/(x1/2.7 + x2/8.9 + x3/7.19 + x4/7.874 + x5/10.28 + x6/8.57 + x7/4.506 + x8/19.25 + x9/2.34 + x10/2.281 + (1000-x1-x2-x3-x4-x5-x6-x7-x8-x9-x10)/8.908))
        
        pop.CV = np.hstack([x1 - 50,
                            0 - x1,
                            x2 - 150,
                            50 - x2,
                            x3 - 150,
                            100 - x3,
                            x4 - 10,
                            0 - x4,
                            x5 - 50,
                            0 - x5,
                            x6 - 50,
                            0 - x6,
                            x7 - 50,
                            0 - x7,
                            x8 - 50,
                            0 - x8,
                            x9 - 1,
                            0 - x9,
                            x10 - 1,
                            0 - x10,
                            x1 + x6 + x7 - 100,
                            0 - x1 - x6 - x7,
                            ]) # Constraints of feature value requirements
        pop.ObjV = np.hstack([strength, density])

if __name__ == '__main__':
    problem = MyProblem()
    Encoding = 'RI'
    NIND = 20 # Number of optimal solutions
    Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders)
    population = ea.Population(Encoding, Field, NIND)
    myAlgorithm = ea.moea_awGA_templet(problem, population)
    myAlgorithm.MAXGEN = 2000 # Iterations
    myAlgorithm.logTras = 0
    myAlgorithm.verbose = False
    myAlgorithm.drawing = 0
    prophetPop, pop = myAlgorithm.run() # Conduct population evolution
    myAlgorithm = ea.moea_NSGA2_templet(problem, population)
    myAlgorithm.MAXGEN = 2000
    myAlgorithm.logTras = 1
    myAlgorithm.verbose = True
    myAlgorithm.drawing = 1
    [NDSet, population] = myAlgorithm.run(prophetPop)
    NDSet.save()
    print('time：%s ' % myAlgorithm.passTime)
    print('Number of individuals：%d ' % NDSet.sizes) if NDSet.sizes != 0 else print('No feasible solution found!')
