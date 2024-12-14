# rheology models
import lmfit
import matplotlib.pyplot as plt 


def Newtonian(x, eta=0.1):
    return eta * x

Newtonian_model = lmfit.Model(Newtonian)

Newtonian_model.set_param_hint("eta", min=0)

def zhang(x, mu=10, G0=100, beta=0.01):
    return (x * mu) / (1 + (mu * x / (2 * (G0 + beta * mu * x)) ** 2))


zhang_model = lmfit.Model(zhang)

zhang_model.set_param_hint("mu", min=0)
zhang_model.set_param_hint("G0", min=0, vary=True)
zhang_model.set_param_hint("beta", min=0)


def carreau(x, eta_0=1.0, gammadot_crit=1.0, n=0.5):
    return x * eta_0 * (1 + (x / gammadot_crit) ** 2) ** ((n - 1) / 2)


carreau_model = lmfit.Model(carreau)

carreau_model.set_param_hint("eta_0", min=0)
carreau_model.set_param_hint("gammadot_crit", min=0, vary=True)
carreau_model.set_param_hint("n", min=0, max=1)


def cross(x, eta_0=1, eta_inf=0.01, k=5, n=0.5):
    return x * (eta_inf + ((eta_0 - eta_inf) / (1 + (k * x) ** n)))


cross_model = lmfit.Model(cross)
cross_model.set_param_hint("k", min=0)
cross_model.set_param_hint("n", min=0, max=1)
cross_model.set_param_hint("eta_0", min=0)
cross_model.set_param_hint("eta_inf", min=0)


def TC(x, ystress=0.05, eta_bg=10, gammadot_crit=0.01):
    return ystress + ystress * (x / gammadot_crit) ** 0.5 + eta_bg * x


TC_model = lmfit.Model(TC)
TC_model.set_param_hint("ystress", min=0, vary=True)
TC_model.set_param_hint("eta_bg", min=0, vary=True)
TC_model.set_param_hint("gammadot_crit", min=0)


def TC_partial(x, ystress=0.05, gammadot_crit=0.01):
    return ystress + ystress * (x / gammadot_crit) ** 0.5


TC_partial_model = lmfit.Model(TC_partial)
TC_partial_model.set_param_hint("ystress", min=0, vary=True)
TC_partial_model.set_param_hint("gammadot_crit", min=0)


def TCC(
    x,
    ystress=0.05,
    eta_bg_0=10,
    gammadot_crit_TC=0.01,
    gammadot_crit_carreau=100,
    n=0,
):
    return (
        ystress
        + ystress * (x / gammadot_crit_TC) ** 0.5
        + x
        * eta_bg_0
        * (1 + (x / gammadot_crit_carreau) ** 2) ** ((n - 1) / 2)
    )


TCC_model = lmfit.Model(TCC)
TCC_model.set_param_hint("ystress", min=0, value=0.001, vary=True)
TCC_model.set_param_hint("gammadot_crit_TC", min=0, value=0.1, vary=True)
TCC_model.set_param_hint("gammadot_crit_carreau", min=0, value=100, vary=True)
TCC_model.set_param_hint("eta_bg_0", min=0, value=10, vary=True)
TCC_model.set_param_hint("n", min=0, max=1, value=0, vary=True)


def TCCross(
    x, ystress=0.05, eta_0=10, gammadot_crit_TC=0.01, eta_inf=0.01, k=0.1, n=0
):
    return (
        ystress
        + ystress * (x / gammadot_crit_TC) ** 0.5
        + x * (eta_inf + ((eta_0 - eta_inf) / (1 + (k * x) ** n)))
    )


TCCross_model = lmfit.Model(TCCross)
TCCross_model.set_param_hint("ystress", min=0, value=0.001, vary=True)
TCCross_model.set_param_hint("gammadot_crit_TC", min=0, value=0.1, vary=True)
TCCross_model.set_param_hint("k", min=0, value=0.1, vary=True)
TCCross_model.set_param_hint("eta_0", min=0, value=10, vary=True)
TCCross_model.set_param_hint("eta_inf", min=0, value=0.01, vary=True)
TCCross_model.set_param_hint("n", min=0, max=1, value=0, vary=True)


def TCZhang(
    x, ystress=0.05, eta_0=10, gammadot_crit_TC=0.01, mu=10, G0=100, beta=0.5
):
    return (
        ystress
        + ystress * (x / gammadot_crit_TC) ** 0.5
        + (x * mu) / (1 + (mu * x / (2 * (G0 + beta * mu * x)) ** 2))
    )


TCZhang_model = lmfit.Model(TCZhang)
TCZhang_model.set_param_hint("ystress", min=0, value=0.001, vary=True)
TCZhang_model.set_param_hint("gammadot_crit_TC", min=0, value=0.1, vary=True)
TCZhang_model.set_param_hint("mu", min=0)
TCZhang_model.set_param_hint("G0", min=0, vary=True)
TCZhang_model.set_param_hint("beta", min=0)

double_carreau_model = lmfit.Model(carreau, prefix="a_") + lmfit.Model(
    carreau, prefix="b_"
)
TCCC_model = double_carreau_model + TC_partial_model


model_dict = {
    "Newtonian": Newtonian_model,
    "TC": TC_model,
    "Carreau": carreau_model,
    "TCC": TCC_model,
    #"double_carreau": double_carreau_model,
    #"TCCC": TCCC_model,
    "cross": cross_model,
    #"TCCross": TCCross_model,
    "zhang": zhang_model,
    #"TCZhang": TCZhang_model,
}

def plot_fit_res(
    fit_res, filename=None, show_par_values=True, exp_err=0.05, min_shear_rate=None, max_shear_rate=None
):

    fig, (ax1, ax3) = plt.subplots(2, 1, sharex=True)
    ax2 = ax1.twinx()

    ax1.plot(
        fit_res.userkws["x"],
        fit_res.data,
        "o",
        color="red",
        mfc="none",
        label="data",
    )
    ax1.plot(
        fit_res.userkws["x"],
        fit_res.eval(x=fit_res.userkws["x"]),
        "-",
        color="black",
        label="best fit",
    )

    ax2.plot(
        fit_res.userkws["x"],
        fit_res.data / fit_res.userkws["x"],
        "o",
        color="blue",
        mfc="none",
    )
    ax2.plot(
        fit_res.userkws["x"],
        fit_res.eval(x=fit_res.userkws["x"]) / fit_res.userkws["x"],
        "-",
        color="black",
    )

    ax3.plot(
        fit_res.userkws["x"],
        (fit_res.data - fit_res.eval(x=fit_res.userkws["x"])) / fit_res.data,
        "o",
        color="blue",
        mfc="none",
    )
    ax3.fill_between(
        fit_res.userkws["x"],
        -exp_err,
        exp_err,
        color="blue",
        alpha=0.2,
        label="estimated exp error",
    )

    ax1.set_title(filename)
    ax1.set_yscale("log")
    ax1.set_xscale("log")
    ax2.set_yscale("log")

    ax1.set_ylabel(r"$\sigma [Pa]$")
    ax3.set_xlabel(r"$\dot\gamma [1/s]$")
    ax2.set_ylabel(r"$\eta [Pa s]$")
    ax3.set_ylabel(r"relative residuals")

    ax3.set_ylim(-0.2, 0.2)

    ax3.legend()
    ax1.axvspan(
        float(min_shear_rate),
        float(max_shear_rate),
        color="blue",
        alpha=0.2,
    )

    if show_par_values:
        mod_par_text = ""
        for item in fit_res.params:
            mod_par_text += f"{item} : {fit_res.params[item].value:.2E} \n"

        mod_par_text += f"Red chi square: {fit_res.redchi:.2E} \n"

        plt.text(
            -1,
            0.95,
            mod_par_text,
            transform=plt.gca().transAxes,
            fontsize=14,
            verticalalignment="top",
        )
        fig.suptitle(fit_res.model)

    return fig
