import re
from glob import glob
from pathlib import Path
from pathlib import PurePath

# local imports
from .get_logger import LOGGER

FASTA_EXTENSIONS = [".fa", ".fna", ".ffn", ".frn", ".fasta", ".faa"]
ALL_SUFFIXES = FASTA_EXTENSIONS + [".gz", ".bgz"]


def find_extension(input_file: str):
    if isinstance(input_file, PurePath):
        LOGGER.error(f"input_path {input_file} must not be a pathlib.PurePath object")
        return ""
    input_file_ext = re.sub(r".*\.f", r"\.f", input_file)
    suffixes = Path(input_file_ext).suffixes
    LOGGER.debug(f"Suffixes: {suffixes}")
    if mismatch_suffix := set(suffixes) - set(ALL_SUFFIXES):
        LOGGER.info(f"Suffix {mismatch_suffix} not allowed.")
    else:
        matching_suffix = set(suffixes) & set(FASTA_EXTENSIONS)
        if len(matching_suffix) == 1:
            LOGGER.info(f"Matched fasta file {input_file}")
            return input_file
    return ""


def find_fasta_file(input_path: str):
    if isinstance(input_path, PurePath):
        LOGGER.error(f"input_path {input_path} must not be a pathlib.PurePath object")
        return ""
    input_files = glob(f"{input_path}/**/*.f*", recursive=True)
    LOGGER.debug(f"Found possible fasta matches: {input_files}")

    matched_files = []

    for input_file in input_files:
        LOGGER.debug(f"Input file: {input_file}")
        fasta_file = find_extension(input_file)
        if fasta_file:
            matched_files.append(fasta_file)
    if len(matched_files) > 1:
        LOGGER.warning(
            f"More than one fasta file matched! Returning {matched_files[0]}"
        )
        return matched_files[0]
    elif len(matched_files) == 1:
        LOGGER.info(f"Matched {matched_files[0]}")
        return matched_files[0]
    else:
        LOGGER.warning("Unable to find matching fasta file.")
        return ""
