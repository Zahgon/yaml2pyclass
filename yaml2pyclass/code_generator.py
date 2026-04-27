import inspect
import os
import re
from dataclasses import dataclass
from inspect import getmembers
from pathlib import Path
from typing import Any, Dict, List

import yaml


@dataclass
class CodeGenerator:
    @classmethod
    def from_yaml(cls, config_file: str) -> "CodeGenerator":
        pass

    @classmethod
    def _update_data(cls, obj: object, data: Dict[str, Any]) -> object:

        pass

    @classmethod
    def _update_code(cls, data: Dict[str, Any]) -> None:
        pass

    @classmethod
    def _add_import(cls, lines: List[str]) -> None:
        pass

    @classmethod
    def _create_code(cls, data: Dict[str, Any], indentation: str) -> List[str]:
        pass

    @staticmethod
    def _to_class_name(key: str) -> str:
        pass
