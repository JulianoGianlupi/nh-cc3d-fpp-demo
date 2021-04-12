"""
FocalPointPlasticity Plugin Demo
================================

Written by T.J. Sego, Ph.D.

Biocomplexity Institute

Indiana University

Bloomington, IN, U.S.A.

Description
===========

FocalPointPlasticity Plugin creates deformable links and attaches them to the center of mass of two cells.
A length constraint is imposed on each link according to its rigidity, such that tension and compression of the
links can affect motility of the attached cells and `vice versa`.

This simple demo shows basic functionality of FocalPointPlasticity and how link rigidity affects cell behaviors.
A layer of two cell types is placed in a chemical gradient such that cells of the lower half-layer try to chemotax
to the upper boundary, and cells of the upper half-layer try to chemotax to the lower boundary.
Links join neighboring cells in each half-layer.
Use the sliders to adjust the strength of chemotaxis and rigidity of the links, and observe their corresponding
effects on whether the layer collapses into migrating cells, and on how the collapse of the layer occurs.

"""

from cc3d import CompuCellSetup
from .FocalPointPlasticityDemoSteppables import FocalPointPlasticityDemoSteppable, SteeringPanelSteppable

CompuCellSetup.register_steppable(steppable=FocalPointPlasticityDemoSteppable(frequency=100))
CompuCellSetup.register_steppable(steppable=SteeringPanelSteppable(frequency=1))
CompuCellSetup.run()
