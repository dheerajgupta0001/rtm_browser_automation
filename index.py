from src.iex_Dam_import import iex_Dam_import
from src.iex_Gtam_import import iex_Gtam_import
from src.iex_Rtm_import import iex_Rtm_import
from src.pxi_Dam_import import pxi_Dam_import
from src.pxi_Rtm_import import pxi_Rtm_import
from src.wbes_Rtm_iex_import import wbes_Rtm_iex_import
from src.wbes_Rtm_pxi_import import wbes_Rtm_pxi_import

# try:
#     iex_Dam_import()
# except Exception as ex:
#     print(ex)
#     print("An exception occurred")

try:
    iex_Rtm_import()
except Exception as ex:
    print(ex)
    print("An exception occurred")

# try:
#     iex_Gtam_import()
# except Exception as ex:
#     print(ex)
#     print("An exception occurred")

# try:
#     pxi_Dam_import()
# except Exception as ex:
#     print(ex)
#     print("An exception occurred")

# try:
#     pxi_Rtm_import()
# except Exception as ex:
#     print(ex)
#     print("An exception occurred")

# try:
#     wbes_Rtm_iex_import()
# except Exception as ex:
#     print(ex)
#     print("An exception occurred")

# try:
#     wbes_Rtm_pxi_import()
# except Exception as ex:
#     print(ex)
#     print("An exception occurred")