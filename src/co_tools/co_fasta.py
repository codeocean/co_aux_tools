import os
import re
from glob import glob
from pathlib import Path, PurePath

if os.environ.get("CO_LOG", "false").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)

FASTA_EXTENSIONS = [".fa", ".fna", ".ffn", ".frn", ".fasta", ".faa"]
ALL_SUFFIXES = FASTA_EXTENSIONS + [".gz", ".bgz"]


def find_extension(input_file: str):
    if isinstance(input_file, PurePath):
        log.error(f"input_path {input_file} must not be a pathlib.PurePath object")
        return ""
    input_file_ext = re.sub(r".*\.f", r"\.f", input_file)
    suffixes = Path(input_file_ext).suffixes
    log.debug(f"Suffixes: {suffixes}")
    if mismatch_suffix := set(suffixes) - set(ALL_SUFFIXES):
        log.info(f"Suffix {mismatch_suffix} not allowed.")
    else:
        matching_suffix = set(suffixes) & set(FASTA_EXTENSIONS)
        if len(matching_suffix) == 1:
            log.info(f"Matched fasta file {input_file}")
            return input_file
    return ""


def find_fasta_file(input_path: str):
    if isinstance(input_path, PurePath):
        log.error(f"input_path {input_path} must not be a pathlib.PurePath object")
        return ""
    if input_files := glob(f"{input_path}/**/*.f*", recursive=True):
        log.debug(f"Found possible fasta matches: {input_files}")
    else:
        log.warning(f"No input files found in {input_path}")
        return ""

    matched_files = []

    for input_file in input_files:
        log.debug(f"Input file: {input_file}")
        fasta_file = find_extension(input_file)
        if fasta_file:
            matched_files.append(fasta_file)
    if len(matched_files) > 1:
        log.warning(f"More than one fasta file matched! Returning {matched_files[0]}")
        return matched_files[0]
    elif len(matched_files) == 1:
        log.info(f"Matched {matched_files[0]}")
        return matched_files[0]
    else:
        log.warning("Unable to find matching fasta file.")
        return ""
