x_pixel = 0:639;
x_pixel = x_pixel';

wavelength = (x_pixel+1087.3)./2.4791;
wavelength = wavelength(3:end);
spec_30uM_smooth = smooth(spec_30uM,50);
spec_30uM_smooth =  rhod_30uM_smooth(3:end)-12
[f_pks_30uM f_locs_30uM f_w_30uM f_proms_30uM] = findpeaks(spec_30uM_smooth, wavelength);

peak_intensity = f_pks_30uM(find(f_proms_30uM == max(f_proms_30uM)));
peak_loc = f_locs_30uM(find(f_proms_30uM == max(f_proms_30uM)));
for i = 1:find(spec_30uM_smooth == peak_intensity);
    diff_1(i) = abs(spec_30uM_smooth(i)-peak_intensity/2);
end
bw1_loc = wavelength(find(diff_1 == min(diff_1)));
bw1_intensity = spec_30uM_smooth(find(diff_1 == min(diff_1)));


for i = find(spec_30uM_smooth == peak_intensity):length(spec_30uM_smooth)
    diff_2(i-find(spec_30uM_smooth == peak_intensity)+1) = abs(spec_30uM_smooth(i)-peak_intensity/2);
end
bw2_loc = wavelength(find(spec_30uM_smooth == peak_intensity)+find(diff_2 == min(diff_2)));
bw2_intensity = spec_30uM_smooth(find(spec_30uM_smooth == peak_intensity)+find(diff_2 == min(diff_2)));

bandwidth = abs(bw1_loc - bw2_loc)/2;


    

