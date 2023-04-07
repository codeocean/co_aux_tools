from glob import glob
from pathlib import Path

# local imports
from .get_logger import LOGGER

FASTA_EXTENSIONS = [".fa", ".fna", ".ffn", ".frn", ".fasta", ".faa"]
ALL_SUFFIXES = FASTA_EXTENSIONS + [".gz", ".bgz"]


def find_extension(input_file: Path):
    suffixes = input_file.suffixes
    LOGGER.debug(f"Suffixes {suffixes}")
    mismatch_suffix = set(suffixes) - set(ALL_SUFFIXES)
    if len(mismatch_suffix):  # check that all suffixes are allowed
        LOGGER.info(f"Suffix {mismatch_suffix} not allowed.")
    else:
        matching_suffix = set(suffixes) & set(FASTA_EXTENSIONS)
        if len(matching_suffix) == 1:
            LOGGER.info(f"Matched fasta file {input_file}")
            return input_file
    return ""


def find_fasta_file(input_path: Path):
    input_files = glob(str(input_path / "**/*.f*"), recursive=True)
    LOGGER.debug(f"Found possible fasta matches: {input_files}")

    matched_files = []

    for input_file in input_files:
        LOGGER.debug(f"Input file {input_file}")
        fasta_file = find_extension(Path(input_file))
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
