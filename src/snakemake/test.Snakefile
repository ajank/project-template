configfile: "config/config.yml"

genome = config["genome"]["symbol"]

#
#  Default targets
#

rule all:
  input:
    "results/test_" + genome + ".pdf",
    "results/test.txt"

#
#  A test rule
#

rule test:
  output:
    "results/test_txt"
  conda:
    "../../env/samtools.yaml"
  shell:
    """
    samtools --help > {output}
    """
