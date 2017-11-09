[b_pks_wavelength b_locs_wavelength  b_w_wavelength b_proms_wavelength] = findpeaks(blue_smooth, wavelength);
[g_pks_wavelength g_locs_wavelength g_w_wavelength g_proms_wavelength] = findpeaks(green_smooth, wavelength);
[y_pks_wavelength y_locs_wavelength y_w_wavelength y_proms_wavelength] = findpeaks(yellow_smooth, wavelength);
[r_pks_wavelength r_locs_wavelength r_w_wavelength r_proms_wavelength] = findpeaks(red_smooth, wavelength);
%[f_pks_wavelength f_locs_wavelength f_w_wavelength f_proms_wavelength] = findpeaks(flour_smooth, wavelength);

data_wavelength_v2 = [467;525;585;635];

data_wavelength_v2(1,2) = b_locs_wavelength(find(b_proms_wavelength==max(b_proms_wavelength)));
data_wavelength_v2(2,2) = g_locs_wavelength(find(g_proms_wavelength==max(g_proms_wavelength)));
data_wavelength_v2(3,2) = y_locs_wavelength(find(y_proms_wavelength==max(y_proms_wavelength)));
data_wavelength_v2(4,2) = r_locs_wavelength(find(r_proms_wavelength==max(r_proms_wavelength)));