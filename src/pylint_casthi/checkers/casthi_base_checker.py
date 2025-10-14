from __future__ import annotations

import warnings

import pylint
from pylint.checkers import BaseChecker

from .. import misc


class CasThiBaseChecker(BaseChecker):
    # checks_maxmin_casthi_version = {
    #   check-code: {
    #       "casthi_minversion": "14.0",
    #       "casthi_maxversion": "15.0",
    #   }
    checks_maxmin_casthi_version: dict[str, str] = {}

    def msgid_or_symbol2symbol(self, msgid_or_symbol):
        try:
            msgid = self.linter.msgs_store.message_id_store.get_active_msgids(msgid_or_symbol)[0]
            return self.linter.msgs_store.message_id_store.get_symbol(msgid)
        except (pylint.exceptions.UnknownMessageError, IndexError):
            return None

    def is_casthi_message_enabled(self, msgid):
        valid_casthi_versions = self.linter.config.valid_casthi_versions
        if len(valid_casthi_versions) != 1:
            # It should be defined only one version
            return True
        msg_symbol = self.msgid_or_symbol2symbol(msgid)
        if msg_symbol is None:
            return True
        casthi_version = valid_casthi_versions[0]
        casthi_version_tuple = misc.version_parse(casthi_version)
        if not casthi_version_tuple:
            warnings.warn(
                f"Invalid manifest versions format {casthi_version}. "
                "It was not possible to supress checks based on particular casthi version",
                UserWarning,
                stacklevel=2,
            )
            return True
        required_casthi_versions = self.checks_maxmin_casthi_version.get(msg_symbol) or {}
        casthi_minversion = required_casthi_versions.get("casthi_minversion") or misc.DFTL_VALID_CASTHI_VERSIONS[0]
        casthi_maxversion = required_casthi_versions.get("casthi_maxversion") or misc.DFTL_VALID_CASTHI_VERSIONS[-1]
        return (
            misc.version_parse(casthi_minversion)
            <= misc.version_parse(casthi_version)
            <= misc.version_parse(casthi_maxversion)
        )

    def add_message(self, msgid, *args, **kwargs):
        """Emit translation-not-lazy instead of logging-not-lazy"""
        if not self.is_casthi_message_enabled(msgid):
            return
        return super().add_message(msgid, *args, **kwargs)
