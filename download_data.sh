
# download Human-GEM
wget \
	https://github.com/SysBioChalmers/Human-GEM/raw/refs/tags/v2.0.0/model/Human-GEM.xml \
	-O raw_data/Human-GEM.xml

# download table for cancer medium
wget \
  https://ars.els-cdn.com/content/image/1-s2.0-S2001037022002434-mmc3.xlsx \
  -O raw_data/mmc3_references.xlsx

# download reactions.tsv

wget https://github.com/SysBioChalmers/Human-GEM/raw/refs/tags/v2.0.0/model/reactions.tsv -O raw_data/reactions.tsv


