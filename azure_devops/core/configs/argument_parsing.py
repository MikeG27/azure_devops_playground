from __future__ import annotations

import typing
from typing import TypeVar

from azure_devops.core.configs.base import ConfigBase
from azure_devops.utils.logging import get_logger

if typing.TYPE_CHECKING:
    import argparse

_logger = get_logger(__name__)
T = TypeVar("T", bound=ConfigBase)


def parse_args(parser: argparse.ArgumentParser, cfg_cls: type[T]) -> T:
    """Parses Command Line arguments and returns the script config model.

    Args:
        parser: The instance of :class:`argparse.ArgumentParser` to use.
        cfg_cls: The class of the config to use.
            Anything inheriting from :class:`azure_devops.core.configs.base.ConfigBase` will work.

    Returns:
         A config instance of type given by `cfg_cls`.

    """
    known_args, unknown_args = parser.parse_known_args()
    _logger.info("Unknown args: %(unknown_args)", extra={"unknown_args": unknown_args})
    cfg = cfg_cls(**vars(known_args))
    _logger.info("Running with following config: %(cfg)", extra={"cfg": cfg})
    return cfg
