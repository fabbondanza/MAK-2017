[b_pks b_locs  b_w b_proms] = findpeaks(blue_smooth, x_pixel);
[g_pks g_locs g_w g_proms] = findpeaks(green_smooth, x_pixel);
[y_pks y_locs y_w y_proms] = findpeaks(yellow_smooth, x_pixel);
[r_pks r_locs r_w r_proms] = findpeaks(red_smooth, x_pixel);

data_wavelength = [467;525;585;635];

data_wavelength(1,2) = b_locs(find(b_proms==max(b_proms)));
data_wavelength(2,2) = g_locs(find(g_proms==max(g_proms)));
data_wavelength(3,2) = y_locs(find(y_proms==max(y_proms)));
data_wavelength(4,2) = r_locs(find(r_proms==max(r_proms)));