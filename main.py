import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "ec21cad9-ffbf-492f-918b-d97b41e9aee2")
    .replace("__vl__", "/vless")
    .replace("__vm__", "/vmess")
    .replace("__tr__", "/trojan")
)