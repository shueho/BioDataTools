#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2024/4/4 20:30
# @Author  : Hao Xue
# @E-mail  : studid@163.com
# @File    : BatchGenerationCodeML_CTL.py
#
# Batch generation of CodeML configuration files.


CTL = '''
      seqfile = $A  * sequence data filename
     treefile = $B  * tree file name

      outfile = $C           * main result file name
   
        noisy = 9  * 0,1,2,3,9: how much rubbish on the screen
      verbose = 2  * 0: concise; 1: detailed, 2: too much
      runmode = 0  * 0: user tree;  1: semi-automatic;  2: automatic
                   * 3: StepwiseAddition; (4,5):PerturbationNNI; -2: pairwise

      seqtype = 1  * 1:codons; 2:AAs; 3:codons-->AAs
    CodonFreq = 2 * 0 : 1/61 each, 1:F1X4, 2:F3X4, 3:codon table
                   * 4:F1x4MG, 5:F3x4MG, 6:FMutSel0, 7:FMutSel
        model = $D
                   * models for codons:
                      * 0:one, 1:b, 2:2 or more dN/dS ratios for branches, 6:FromCodon
                   * models for AAs or codon-translated AAs:
                      * 0:poisson, 1:proportional, 2:Empirical, 3:Empirical+F
                      * 6:FromCodon, 7:AAClasses, 8:REVaa_0, 9:REVaa(nr=189)

      NSsites = 0 * 23 24 25 26   * 23 24 25 26 * 0:one w; 1:NearlyNeutral; 2:PositiveSelection; 3:discrete;
                   * 4:freqs; 5:gamma; 6:2gamma; 7:beta; 8:beta&w+; 9:beta&gamma;
                   * 10:beta&gamma+1; 11:beta&normal>1; 12:0&2normal>1;
                   * 13:3normal>0; 
                   * 22:M2a_Old(M2a_rel); 
                   * 23:Tgamma; 24:Tinvgamma; 25:Tgamma+1; 26:Tinvgamma+1.

        clock = 0  * 0:no clock, 1:global clock; 2:local clock
       aaDist = 0  * 0:equal, +:geometric; -:linear, 1-6:G1974,Miyata,c,p,v,a
   aaRatefile = ../dat/wag.dat * for aa seqs under model = 3 (empirical+F)
                   * dayhoff.dat, jones.dat, wag.dat, mtmam.dat, or your own

    fix_kappa = 0  * 1: kappa fixed, 0: kappa to be estimated
        kappa = 3  * initial or fixed kappa
    fix_omega = 0  * 1: omega or omega_1 fixed, 0: estimate
        omega = 1  * initial or fIf yoixed omega, for codons or codon-based AAs

    fix_alpha = 1  * 0: estimate gamma shape parameter; 1: fix it at alpha
        alpha = 0. * initial or fixed alpha, 0:infinity (constant rate)
       Malpha = 0  * different alphas for genes
        ncatG = 10  * # of categories in dG of NSsites models

        getSE = 0  * 0: don't want them, 1: want S.E.s of estimates
 RateAncestor = 0  * (0,1,2): rates (alpha>0) or ancestral states (1 or 2)
   Small_Diff = 1e-8
*    cleandata = 1  * remove sites with ambiguity data (1:yes, 0:no)?
*  fix_blength = 1  * 0: ignore, -1: random, 1: initial, 2: fixed
*       method = 0  * Optimization method 0: simultaneous; 1: one branch a time

* Genetic codes: 0:universal, 1:mammalian mt., 2:yeast mt., 3:mold mt.,
* 4: invertebrate mt., 5: ciliate nuclear, 6: echinoderm mt., 
* 7: euplotid mt., 8: alternative yeast nu. 9: ascidian mt., 
* 10: blepharisma nu., 11: Yang's regularized code 
* These codes correspond to transl_table 1 to 11 of GenBank.
'''

import sys
dirpath = sys.argv[1] #"pamlfile"
tree = sys.argv[2] #"../codml.tree"
import os
p_list = os.listdir(dirpath)

try:
    os.makedirs("codemlnull")
except:
    pass

try:
    os.makedirs("codeml2")
except:
    pass


def trans(A,B,C,D):  #A:INPUT SEQ; B:TREE; C:OUTPUT; D:0ISNULL 2ISALT
    return CTL.replace("$A",A).replace("$B",B).replace("$C",C).replace("$D",D)

def cope_one(filename):
    with open("codemlnull/"+filename+".ctl","w") as f:
        f.write(trans("../"+dirpath+"/"+filename,tree,"./output0/"+filename+"/abc.txt","0"))
    with open("codeml2/"+filename+".ctl","w") as f:
        f.write(trans("../"+dirpath+"/"+filename,tree,"./output2/"+filename+"/abc.txt","2"))


for i in p_list:
    cope_one(i)

print("ok!")
