# marimo_rheofit

Rheology flow curve fitting tool with marimo notebook deployed on github pages!

Rheology is the study of the flow and deformation of materials under applied stress. The viscosity is one key parameter that describes the flow behavior of a material. The flow can be described as the continuous deformation of the a material ove time under applied stress. The viscosity is a measure of the resistance the material to flow:

$$\eta=\frac{\sigma}{\dot\gamma}$$

where $\eta$ is the viscosity measured in $pa s$, $\sigma$ is the shear stress measured in $pa$, and $\dot\gamma$ is the shear rate measured in $1/s$ deformation per unit time.

For Newtonian fluids, like water or glycerin, the viscosity is constant and does not depend on the shear rate. For non-Newtonian fluids, the viscosity depends on the shear rate.

The flow curve of a material is the plot of viscosity as a function of shear rate. The flow curve can be fitted to a model to extract parameters that describe the flow behavior of the material. This tool allows you to fit (perform non linear regression) a flow curve to a range of rheologycal models and extract the parameters.


# Functionality

* Load rheology data from a xls file
    * example file provided here [Flow_curve_example.xls](./Flow_curve_example.xls) download it to test the app.
    * After parsing the file a dropdown menu will appear with the list of steps in the measurement procedure
    * Selecting the step and the fitting model will show the model equation, the fitting curve and the estimated parameters


# Example flow curve file

[Flow_curve_example.xls](./Flow_curve_example.xls)

The example file is the measurement of the flow curve for a mayonaise sample to represent "yield stress fluid", able to sstand as a solid at rest and flow under applied stress.

The flow curve is measured 2 time:
* Flow sweep 1 starting at low shear rate
* Flow sweep 2 starting at high shear rate

# Try the marimo app

WASM based app hosted on github pages: 

[https://caggionim.github.io/marimo_rheofit/](https://caggionim.github.io/marimo_rheofit/?show-code=false)
