import json
from dataclasses import dataclass
from typing import List, Optional

import pycld2 as cld2
from iso639 import Lang
from websocket import create_connection


@dataclass
class Translation:
    error: Optional[str] = None
    translation: Optional[List[str]] = None


def detect_language(msg) -> str:

    isReliable, textBytesFound, details = cld2.detect(msg, bestEffort=True)
    return str(Lang(details[0][1]).pt3)


def translate(msg: str, client_name: Optional[str] = None) -> Translation:

    # lang = 'detect'
    lang = detect_language(msg)

    isReliable, textBytesFound, details = cld2.detect(msg, bestEffort=True)
    lang = Lang(details[0][1]).pt3

    ws = create_connection("ws://86.50.168.81:8080/translate")
    data = {"text": msg, "source": lang, "target": "ukr"}
    ws.send(json.dumps(data))
    result = ws.recv()
    ws.close()

    j = json.loads(result)
    return Translation(translation=j["result"])
