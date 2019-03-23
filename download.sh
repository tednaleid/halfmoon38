# original from: https://search.library.wisc.edu/digital/AA24CYFM2LYA248K/full

for FIRST in $(seq 0 17); do for SECOND in $(seq 0 17); do
DOWNLOAD_FILE="${FIRST}_${SECOND}.jpg"
curl -L "https://asset.library.wisc.edu/dz/1711.dl/YB3BMLI5G2HHF85/M/tiles.tif_files/13/${DOWNLOAD_FILE}" -H 'Accept: image/webp,*/*' --compressed > "${SECOND}_${FIRST}.jpg"
done
done