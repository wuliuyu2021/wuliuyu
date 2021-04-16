#!/usr/bin/python
# -*- coding = utf-8 -*-

import os
import sys
import re
from optparse import OptionParser

BASE_DIR = "/thinker/dstore/rawfq"


def parse_cmd():
    usage = (
        "Create upload rawdata csv for hapcloud project!\n"
        "CMD: python %prog <-i seqdir> <-y estimated_yield> <-o outdir>\n")
    version = "%prog 1.0"
    parser = OptionParser(usage=usage, version=version)
    parser.add_option(
        "-f", "--seqID", dest="seqID",
        help="the seq ID")

    return parser.parse_args()


def get_files(seqID):
    indir = os.path.join(BASE_DIR, seqID)

    undetermined = sorted(filter(
        lambda x: re.match(r'Undetermined(.+)(_R1_001.fastq|_R1_001.fastq.gz)', x), os.listdir(indir)))

    pattern = re.compile(
        r"(^S\d+)(.+)(.+)(_R1_001.fastq|_R1_001.fastq.gz)")

    srs = sorted(filter(lambda x: re.match(pattern, x), os.listdir(indir)))

    return undetermined + srs


def main():
    (options, args) = parse_cmd()
    seqID = options.seqID

    fs = get_files(seqID)
    print fs

    csv = "%s_upload_hapcloud.csv" % seqID
    if os.path.exists(csv):
        os.remove(csv)

    for r1 in fs:
        sid = r1.split("_R1_001.")[0]
        r1path = "hdfs:/%s/%s/%s" % (os.path.basename(BASE_DIR), seqID, r1)
        r2 = r1.replace("_R1_001.", "_R2_001.")
        r2path = "hdfs:/%s/%s/%s" % (os.path.basename(BASE_DIR), seqID, r2)

        with open(csv, "a") as w:
            w.write("%s,%s,,%s,,%s\n%s,%s,,%s,,%s\n" % (sid, sid, r1, r1path, sid, sid, r2, r2path))


if __name__ == "__main__":
    main()
