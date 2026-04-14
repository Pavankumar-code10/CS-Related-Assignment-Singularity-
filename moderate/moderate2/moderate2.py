import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt

search_result = lk.search_targetpixelfile("TIC 261136679", mission="TESS")

tpf = search_result[0].download()

lc_default = tpf.to_lightcurve()

flux = np.nanmean(tpf.flux, axis=0)
threshold = 0.7 * np.nanmax(flux)
custom_mask = flux > threshold

lc_custom = tpf.to_lightcurve(aperture_mask=custom_mask)

plt.plot(lc_default.time.value, lc_default.flux / np.nanmedian(lc_default.flux))
plt.plot(lc_custom.time.value, lc_custom.flux / np.nanmedian(lc_custom.flux))

plt.legend(["Default", "Custom"])
plt.grid()
plt.show()
