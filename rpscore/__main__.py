import sys
from os import makedirs as os_makedirs
from os import path as os_path

from brs_utils import (
    build_args_parser,
)
from brs_utils import (
    init as init_logger,
)
from rplibs import rpPathway

from ._version import __version__
from .args import add_arguments
from .rpscore import FBAError, ThermoError, predict_score


def entry_point():

    parser = build_args_parser(
        prog="rpscore",
        description="Calculate global score by combining all scores (rules, FBA, Thermo)",
        m_add_args=add_arguments,
    )
    args = parser.parse_args()

    logger = init_logger(parser, args, __version__)

    pathway = rpPathway(infile=args.infile, logger=logger)

    try:
        score = predict_score(
            pathway=pathway,
            # data_train_file=args.data_train_file,
            # models_path=models_path,
            no_of_rxns_thres=args.no_of_rxns_thres,
            logger=logger,
        )
    except ThermoError as e:
        logger.error(e)
        sys.exit(1)
    except FBAError as e:
        logger.error(e)
        sys.exit(2)

    # Write results into the pathway
    pathway.set_global_score(score)
    # Write pathway into file
    # Create the output directory if not exists
    os_makedirs(os_path.dirname(args.outfile), exist_ok=True)
    pathway.to_rpSBML().write_to_file(args.outfile)


if __name__ == "__main__":
    entry_point()
