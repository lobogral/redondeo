from decimal import Decimal
from decimal import getcontext
from decimal import ROUND_HALF_UP
from decimal import ROUND_HALF_EVEN


def redondear(numero, decimales):
    context = getcontext()
    context.rounding = ROUND_HALF_UP
    redondeo = round(Decimal(str(numero)), decimales)
    context.rounding = ROUND_HALF_EVEN
    return redondeo
