import marimo as mo

def make_ui_parameters(params):
    model_params = {}
    for key, param in params.items():
        model_params[key] = mo.ui.dictionary(
            {
                "max": mo.ui.text(label="max", value=str(param.max)),
                "min": mo.ui.text(label="min", value=str(param.min)),
                "value": mo.ui.text(label="value", value=str(param.value)),
                "vary": mo.ui.checkbox(label="vary", value=param.vary),
            },
            label=key,
        )
    return mo.ui.dictionary(model_params)

def make_parameters_from_ui(model, ui_parameter):
  params = model.make_params()

  for par_name, par_ui_dict in ui_parameter.elements.items():
      params[par_name].max = float(par_ui_dict["max"].value)
      params[par_name].min = float(par_ui_dict["min"].value)
      params[par_name].value = float(par_ui_dict["value"].value)
      params[par_name].vary = par_ui_dict["vary"].value
  return params